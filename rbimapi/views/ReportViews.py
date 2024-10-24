from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rbim.models import ReportCategories, ReportHistory, Users, Location
from rbimapi.serializers.ReportSerializers import ReportCategorySerializer, ReportHistorySerializer
from rbimapi.mongoaggregate.report import barangay_list, location_barangay_list, location_list
import constants
import pandas as pd
try:
    from io import BytesIO as IO # for modern python
except ImportError:
    from io import StringIO as IO
from rbimapi.validations import PageValidation
import staticContent
from rbimapi.utilities import round_up
class ReportCategoryListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsAuthenticated,]
    serializer_class    = ReportCategorySerializer
    def get(self,request):
        try:
            category_obj     = ReportCategories.objects.filter(deleted_at__isnull=True)
            serializer = self.get_serializer(category_obj, many=True)
            return Response({
                "status":1,
                "message":"Fetched",
                "data":serializer.data
            },status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status":0,
                "message":str(e)
            })

class BarangayListAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def get(self,request):
        try:
            param = {}
            param['match'] = {
                "status":"survey_completed"
            }
            barangay_details = barangay_list(param)
            if barangay_details:
                return Response({"status":1, "data":barangay_details}, status=status.HTTP_200_OK)
            else:
                return Response({"status":0, "message":constants.DATA_NOT_FOUND_ERROR_MSG}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
           return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class GetReportAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsAuthenticated,]
    serializer_class    = ReportHistorySerializer
    def post(self,request):
        try:
            location_ids = request.data['location_id']
            if ReportHistory.objects.filter(location_id__in =location_ids,
                                                            report_category_id = request.data['category_id']).count():
                category_obj = ReportHistory.objects.filter(location_id__in= location_ids,
                                                                report_category_id = request.data['category_id'])
                serializer = self.get_serializer(category_obj, many=True)
                return Response({"status": 1, "message": "Fetched", "data": serializer.data},
                                status=status.HTTP_200_OK)
            else:
                return Response({"status": 0, "message": constants.DATA_NOT_FOUND_ERROR_MSG,
                                 "data": "No report available for selected location"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": 0,
                "message": str(e)
            })

class BarangayCompletedSurveyChartReportsAPIView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_location_name(self, location_id, index):
        if location_id is not None:
            location = Location.objects.filter(id=location_id).first()
            return f"{location.name}Sheet{index+1}"
        else:
            return f"Sheet{index}"


    def post(self, request):
        category_id = request.data.get('category_id')
        excel_response = []
        location_id = request.data['location_id']
        try:

            filter_rh = ReportHistory.objects.filter(location_id__in=location_id,
                                                     report_category_id=category_id)
            filter_rc = ReportCategories.objects.filter(id=category_id).first()
            filename = f"{filter_rc.category_name.replace(' ','_').replace(',','_').lower()}.xlsx"
            for report in filter_rh:
                excel_response.append(report.excel_response)
            excel_file = IO()
            xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')
            for i, d in enumerate(excel_response):
                location_name = self.get_location_name(location_id[i], i)
                df_output = pd.DataFrame(d)
                if filter_rc.category_slug == 'bar_marital_status_by_age':
                    df_output.to_excel(xlwriter, f"{location_name}", index_label='Age')
                elif filter_rc.category_slug == 'pie_common_disease' or filter_rc.category_slug == 'pie_primary_needs':
                    df_output.index = df_output.index + 1
                    df_output.to_excel(xlwriter, f"{location_name}", index_label='Sl.no')
                else:
                    df_output.to_excel(xlwriter, f"{location_name}", index=False)
            xlwriter.close()
            excel_file.seek(0)
            response = HttpResponse(excel_file.read(),
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Access-Control-Expose-Headers'] = 'Content-Disposition'
            return response

        except Exception as e:
            return Response({"status": 0, "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class LocationListAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]

    def post(self, request):
        try:
            PageValidation.validate_page(data = request.data) 
            page = request.data['page']
            page_size = request.data['page_size']
            if(page == 1):
                skip = 0
            else:
                skip = (page - 1) * page_size
            param ={}
            param['skip'] = skip
            param['page_size'] = page_size
            if request.user.role == constants.USER_ROLES[1]:
#                param['match'] ={
#                    "id":request.user.location_id
#                }
#                location_obj = location_list(param)
#                location_count = 1
#            else:
                match = {}
                search_fields = ['name']
                search_param = []
                if request.data["search"]:
                    for sval in search_fields:
                        ar_prm = {
                            sval: {'$regex': request.data["search"], '$options': 'i'}
                        }
                        search_param.append(ar_prm)
                    match['$or'] = search_param
                param['match'] = match
                location_obj = location_list(param)
                location_count = Location.objects.count()
            total_records = location_count
            num_pages = (total_records / page_size)
            num_pages = round_up(num_pages)
            return Response({
                "status": 1,
                "paginator": staticContent.pagination_param(total_records=total_records, num_pages=num_pages, page=page, obj_info=location_obj),
                "data": location_obj},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": 0, "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)