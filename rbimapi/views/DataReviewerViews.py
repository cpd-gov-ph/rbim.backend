import constants
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rbimapi.validations import EmailValidation, PageValidation
from rbimapi.mongoaggregate.dataReviewer import mongo_query_data_reviewer_count, mongo_query_data_reviewer_list
from rbim.models import Users, Profile, SurveyEntry
from rbimapi.permissions import IsSuperadminAuthenticated, IsSuperAdminandBarangayAuthenticated
from rbimapi.serializers.DataReviewerSerializers import DatareviewerRegisterSerializer, DatareviewerSerializer, DataReviewerUpdateSerializer, NextSectionSerializer
from rbimapi.serializers.SurverySerializers import ReviewFinalSubmitSerializer, OcrFinalSubmitSerializer
from rbimapi.utilities import round_up
from rest_framework.permissions import IsAuthenticated
import staticContent
"""
Create DataReviewer 
"""
class DatareviewerRegisterView(generics.CreateAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperadminAuthenticated,]
    serializer_class = DatareviewerRegisterSerializer
    def create(self,request):
        try:
            serializer = self.get_serializer(data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                return Response({"status":1, "message":"Data-Reviewer created successfully","data":serializer.data},status=status.HTTP_201_CREATED)
            return Response({"status":0, "message":constants.REGISTRATION_FAILED_ERROR_MSG},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
class DatareviewerRetrieveAPIView(generics.RetrieveAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperAdminandBarangayAuthenticated,]
    serializer_class    = DatareviewerSerializer
    def get(self, request, id):
        try:
            data_reviewer = Users.objects.filter(id = id).first()
            data_reviewer = self.get_serializer(data_reviewer).data
            if not data_reviewer:
                return Response({"status":0,"message":constants.USER_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            return Response({"status":1,"message":"User data retrieved","data":data_reviewer},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
class UpdateDataReviewerAPIView(generics.UpdateAPIView):
    """
     Update Data Reviewer Here
    """
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperadminAuthenticated,]
    serializer_class = DataReviewerUpdateSerializer

    def update(self,request,id):
        try:
            email = request.data['email']
            EmailValidation.validate_email(email = email)
            d_reviewer_user = Users.objects.filter(id = id).first()
            if not d_reviewer_user:
                return Response({"status":0,"message":constants.USER_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            
            if Users.objects.filter(email__iexact = request.data['email']).exclude(email=d_reviewer_user.email).count():
                return Response({"status":0,"message":constants.EMAIL_EXISTS_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            
            d_reviewer_profile_info = Profile.objects.filter(user = d_reviewer_user).first()
            if Profile.objects.filter(phone_no = request.data['profile']['phone_no']).exclude(phone_no=d_reviewer_profile_info.phone_no).count():
                return Response({"status":0,"message":constants.PHONENO_EXISTS_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
                
            d_reviewer_serializer = self.get_serializer(d_reviewer_user,data = request.data,context={"user_id":request.user.id})
            if d_reviewer_serializer.is_valid(raise_exception = True):
                d_reviewer_serializer.save()
                return Response({"status":1, "message":"Data reviewer updated successfully","data":d_reviewer_serializer.data},status=status.HTTP_201_CREATED)
            return Response({"status":0, "message":d_reviewer_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class DatareviewerListView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsSuperAdminandBarangayAuthenticated,]
    def post(self,request):
        try:
            PageValidation.validate_page(data = request.data)
            page = request.data['page']
            page_size = request.data['page_size']

            if(page == 1):
                skip = 0
            else:
                skip = (page - 1) * page_size
            # Condition Added Here
            user_param = {}
            user_param['skip'] = skip
            user_param['page_size'] = page_size
            user_param['sort'] = {'created_at':-1}
            match = {}
            search_fields = ['first_name', 'email', 'profile.dob', 'profile.gender', 'profile.phone_no', 'profile.address', 'barangay.first_name']
            search_param = []
            if request.data["search"]:
                for sval in search_fields:
                    ar_prm = {
                       sval : {'$regex':request.data["search"], '$options':'i'}
                    }
                    search_param.append(ar_prm)
                match['$or'] = search_param
            # Search end
            if request.user.role == constants.USER_ROLES[1]:
                match['barangay_id'] = request.user.id  
            match['role'] = 'data_reviewer'
            match['deleted_at'] = None
            user_param['match'] = match

            user_info_count = {}
            user_info_count = mongo_query_data_reviewer_count(user_param)
            user_info = mongo_query_data_reviewer_list(user_param)
            total_records = user_info_count
            num_pages = (total_records / page_size)
            num_pages = round_up(num_pages)
            return Response({
                "status":1,
                "message":"Fetched",
                "paginator": staticContent.pagination_param(total_records=total_records, num_pages=num_pages, page=page, obj_info=user_info),  
                "data":user_info
            },status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status":0,
                "message":str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class SurveryEntryAPIView(generics.RetrieveAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    serializer_class = NextSectionSerializer
    def get(self, request, id):
        try:
            survey_entry_obj = SurveyEntry.objects.filter(id = id).first()
            survey_entry = self.get_serializer(survey_entry_obj).data
            if not survey_entry:
                return Response({"status":0,"message":constants.USER_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            return Response({"status":1,"message":"Data retrieved","data":survey_entry},status = status.HTTP_200_OK)            
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class SurveyReviewSubmitAPIView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        try:
            serializer = ReviewFinalSubmitSerializer(data=request.data, context={"user_id":request.user.id})
            if serializer.is_valid(raise_exception = True):
                return Response({"status":1, "message":"Review submit successfully", "data":serializer.validated_data},status=status.HTTP_201_CREATED)
            return Response({"status":0, "message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class OcrReviewSubmitAPIView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsAuthenticated,]
    def post(self, request):
        try:
            serializer = OcrFinalSubmitSerializer(data=request.data, context={"user_id":request.user.id})
            if serializer.is_valid(raise_exception = True):
                return Response({"status":1, "message":"Review submit successfully", "data":serializer.validated_data},status=status.HTTP_201_CREATED)
            return Response({"status":0, "message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
