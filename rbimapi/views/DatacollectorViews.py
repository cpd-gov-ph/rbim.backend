import uuid
import constants
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rbimapi.validations import EmailValidation, PageValidation
import datetime
from rbim.models import Users, Profile, Tasks
from rbimapi.permissions import IsSuperadminAuthenticated, IsSuperAdminandBarangayAuthenticated, IsBarangayAuthenticated
from rbimapi.serializers.DatacollectorSerializer import DatacollectorRegisterSerializer, DataCollectorSerializer, DataCollectorUpdateSerializer, TaskCreateSerializer, TaskSerializer
from rbimapi.utilities import round_up
from rbimapi.mongoaggregate.dataCollector import mongo_query_data_collector_count, mongo_query_data_collector_list, mongo_query_task_count, mongo_query_task_list
import staticContent
"""
Create DataCollector 
"""
class DatacollectorRegisterView(generics.CreateAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperadminAuthenticated,]
    serializer_class = DatacollectorRegisterSerializer
    def create(self,request):
        try:
            serializer = self.get_serializer(data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                return Response({"status":1, "message":"Data-Collector created successfully","data":serializer.data},status=status.HTTP_201_CREATED)
            return Response({"status":0, "message":constants.REGISTRATION_FAILED_ERROR_MSG},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
class DatacollectorRetrieveAPIView(generics.RetrieveAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperAdminandBarangayAuthenticated,]
    serializer_class    = DataCollectorSerializer
    def get(self, request, id):
        try:
            data_reviewer = Users.objects.filter(id = id).first()
            data_reviewer = self.get_serializer(data_reviewer).data
            if not data_reviewer:
                return Response({"status":0,"message":constants.USER_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            return Response({"status":1,"message":"User data retrieved","data":data_reviewer},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
class UpdateDataCollectorAPIView(generics.UpdateAPIView):
    """
     Update Data Collector Here
    """
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperadminAuthenticated,]
    serializer_class = DataCollectorUpdateSerializer

    def update(self,request,id):
        try:
            email = request.data['email']
            EmailValidation.validate_email(email = email)
            d_collector_user = Users.objects.filter(id = id).first()
            if not d_collector_user:
                return Response({"status":0,"message":constants.USER_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            
            if Users.objects.filter(email__iexact = request.data['email']).exclude(email=d_collector_user.email).count():
                return Response({"status":0,"message":constants.EMAIL_EXISTS_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            
            d_collector_profile_info = Profile.objects.filter(user = d_collector_user).first()
            if Profile.objects.filter(phone_no = request.data['profile']['phone_no']).exclude(phone_no=d_collector_profile_info.phone_no).count():
                return Response({"status":0,"message":constants.PHONENO_EXISTS_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
                
            d_collector_serializer = self.get_serializer(d_collector_user,data = request.data,context={"user_id":request.user.id})
            if d_collector_serializer.is_valid(raise_exception = True):
                d_collector_serializer.save()
                return Response({"status":1, "message":"Data collector updated successfully","data":d_collector_serializer.data},status=status.HTTP_201_CREATED)
            return Response({"status":0, "message":d_collector_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
class DatacollectorListView(APIView):
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
            search_fields = ['first_name', 'email', 'profile.dob', 'profile.gender', 'profile.phone_no', 'profile.address', 'barangay.first_name','data_reviewer.first_name']
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
            match['role'] = 'data_collector'
            match['deleted_at'] = None
            user_param['match'] = match
            user_info_count = mongo_query_data_collector_count(user_param)
            user_info = mongo_query_data_collector_list(user_param)
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
class CreateTaskAPIView(generics.CreateAPIView):
    """
     Assign Task Here
    """
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsBarangayAuthenticated,]
    serializer_class = TaskCreateSerializer
    def create(self,request):
        try:    
            request_data ={
                "data_collector":request.data['data_collector'],
                "title":request.data['title'],
                "description":request.data['description'],
                "created_by":request.user.id
            }
            serializer = self.get_serializer(data = request_data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                return Response({"status":1, "message":"Task created successfully","data":serializer.data},status=status.HTTP_201_CREATED)
            return Response({"status":0, "message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
class ViewTaskAPIView(generics.RetrieveAPIView):
    """
     Retrieve Task Here
    """
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsBarangayAuthenticated,]
    serializer_class    = TaskSerializer
    def get(self, request,id):
        try:
            task = Tasks.objects.filter(id = id).first()
            if not task:
                return Response({"status":0,"message":constants.TASK_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND) 
            task = self.get_serializer(task).data
            return Response({"status":1,"message":"Tasks retrieved","data":task},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
class DeleteTaskAPIView(generics.DestroyAPIView):
    """
     Delete Task Here
    """
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsBarangayAuthenticated,]

    def destroy(self,request,id):
        try:
            task = Tasks.objects.filter(id = id).first()
            if not task:
                return Response({"status":0,"message":constants.TASK_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            task.deleted_at = datetime.date.today()
            task.save()
            return Response({"status":1, "message":"Task deleted successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
class HomeTaskDetailsAPIView(generics.RetrieveAPIView):
    """
     Retrieve Task Here
    """
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    serializer_class = TaskSerializer
    def get(self, request):
        try:
            task = Tasks.objects.filter(data_collector = request.user.id).filter(deleted_at__isnull = True).last()
            if not task:
                return Response({"status":0,"message":constants.TASK_NOT_FOUND_ERROR_MSG,"total_task_count":0,"recent_task":{}},status = status.HTTP_404_NOT_FOUND) 
            task_count = Tasks.objects.filter(data_collector = request.user.id).filter(deleted_at__isnull = True).count()
            tasks = self.get_serializer(task).data
            return Response({"status":1,"message":"Tasks retrieved","total_task_count":task_count,"recent_task":tasks},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
class DataCollectorTaskListView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsAuthenticated,]
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
            task_param = {}
            task_param['skip'] = skip
            task_param['page_size'] = page_size
            match = {}
            search_fields = ['task.task_no','task.data_collector','task.title','task.description']
            search_param = []
            if request.data["search"]:
                for sval in search_fields:
                    ar_prm = {
                        sval : {'$regex':request.data["search"], '$options':'i'}
                    }
                    search_param.append(ar_prm)
                match['$or'] = search_param
            # Search end
            match['data_collector_id'] = request.user.id
            if request.user.role == constants.USER_ROLES[1]:
                if (("data_collector_id" in request.data.keys()) and request.data['data_collector_id']):
                    match['data_collector_id'] = uuid.UUID(request.data['data_collector_id'])
                    match['created_by'] = request.user.id 
                else:
                    return Response({"status":0,"message":"Data_collector_id is required"},status = status.HTTP_400_BAD_REQUEST)
            match['deleted_at'] = None
            task_param['match'] = match
            task_param['sort'] = {'created_at':-1}
            user_info_count = mongo_query_task_count(task_param)
            user_info = mongo_query_task_list(task_param)
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
