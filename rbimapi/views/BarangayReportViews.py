import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rbimapi.mongoaggregate.reports import mdb_suvery_completed_reports
import pandas as pd
import staticContent
import constants
from django.http import HttpResponse
try:
    from io import BytesIO as IO # for modern python
except ImportError:
    from io import StringIO as IO # for legacy python

class BarangayCompletedSurveyReportsAPIView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        try:
            filename = str(request.user.id)+"excel.xlsx"
            survey_entry_ids = []
            for rr in request.data['survey_entry_ids']:
                survey_entry_ids.append(uuid.UUID(rr))
            
            if request.data['is_select_all']:
                param = staticContent.survey_report_select_all_param(survey_status=constants.SURVEY_STATUS[6], barangay_id=request.user.id)
            else:
                param = staticContent.survey_report_param(survey_entry_ids=survey_entry_ids, survey_status=constants.SURVEY_STATUS[6], barangay_id=request.user.id)

            reports_list = mdb_suvery_completed_reports(param=param)
            if reports_list:
                df_output = pd.DataFrame(reports_list[0])
                excel_file = IO()
                xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')
                df_output.to_excel(xlwriter, 'Reports', index=False)
                xlwriter.save()
                xlwriter.close()
                excel_file.seek(0)
                response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = 'attachment; filename='+filename
                response['Access-Control-Expose-Headers'] = 'Content-Disposition'
                return response
            else:
                return Response({"status": 0, "message": constants.SURVEY_REPORT_SELECT_ERROR_MSG}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
           return Response({"status": 0, "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

