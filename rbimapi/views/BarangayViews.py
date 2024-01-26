from rest_framework import generics, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rbimapi.permissions import IsSuperadminAuthenticated
from rbimapi.validations import EmailValidation, PageValidation
from rbimapi.utilities import round_up
from rbimapi.serializers.BarangaySerializers import BarangayRegisterSerializer, BarangaySerializer, BarangayUpdateSerializer
from rbimapi.serializers.CommonSerializers import CitySerializer, MunicipalitySerializer, LocationSerializer
from rbimapi.mongoaggregate.barangay import mongo_query_barangay_count, mongo_query_barangay_list
from rbim.models import Location, City, Municipality, Users, Profile
import constants
import staticContent
class LocationAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    '''
    Location CRUD
    '''
    model = Location
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsSuperadminAuthenticated,]
    serializer_class    = LocationSerializer
    def get_queryset(self):
        qs = Location.objects.all()
        query = self.request.GET.get("id")
        if query is not None:
            qs = qs.filter(Q(id=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CityAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    '''
    City CRUD
    '''
    model = City
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsSuperadminAuthenticated,]
    serializer_class    = CitySerializer
    def get_queryset(self):
        qs = City.objects.all()
        query = self.request.GET.get("id")
        if query is not None:
            qs = qs.filter(Q(id=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MunicipalityCreateAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    '''
    City CRUD
    '''
    model = Municipality
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsSuperadminAuthenticated,]
    serializer_class    = MunicipalitySerializer
    def get_queryset(self):
        qs = Municipality.objects.all()
        query = self.request.GET.get("id")
        if query is not None:
            qs = qs.filter(Q(id=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

"""
Create Barangay 
"""
class BarangayRegisterView(generics.CreateAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperadminAuthenticated,]
    serializer_class = BarangayRegisterSerializer
    def create(self,request):
        try:
            serializer = self.get_serializer(data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                return Response({"status":1, "message":"Barangay created successfully","data":serializer.data},status=status.HTTP_201_CREATED)
            return Response({"status":0, "message":constants.REGISTRATION_FAILED_ERROR_MSG},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class BarangayAPIView(generics.RetrieveAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperadminAuthenticated,]
    serializer_class    = BarangaySerializer
    def get(self, request, id):
        try:
            barangay = Users.objects.filter(id = id).first()
            barangay = self.get_serializer(barangay).data
            if not barangay:
                return Response({"status":0,"message":constants.USER_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            return Response({"status":1,"message":"User data retrieved","data":barangay},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class CityListAPIView(generics.ListAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperadminAuthenticated,]
    serializer_class    = CitySerializer
    def get(self, request):
        try:
            location_info = City.objects.filter(deleted_at__isnull = True)
            location_info = self.get_serializer(location_info, many=True).data
            if not location_info:
                return Response({"status":0,"message":constants.USER_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            return Response({"status":1,"message":"Success","data":location_info},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
            
class MunicipalityListAPIView(generics.ListAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperadminAuthenticated,]
    serializer_class    = MunicipalitySerializer
    def get(self, request, city):
        try:
            municipality_info = Municipality.objects.filter(city = city)
            municipality_info = self.get_serializer(municipality_info, many=True).data
            if not municipality_info:
                return Response({"status":0,"message":constants.USER_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            return Response({"status":1,"message":"Success","data":municipality_info},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
            
class MunicipalityToLocationsAPIView(generics.ListAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperadminAuthenticated,]
    serializer_class    = LocationSerializer
    def get(self, request, municipality):
        try:
            location_info = Location.objects.filter(municipality = municipality)
            location_info = self.get_serializer(location_info, many=True).data
            if not location_info:
                return Response({"status":0,"message":constants.USER_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            return Response({"status":1,"message":"Success","data":location_info},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
            
class BarangayListView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsSuperadminAuthenticated,]
    def post(self,request):
        try:
            PageValidation.validate_page(data = request.data) 
            page        = request.data['page']
            page_size   = request.data['page_size']
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
            search_fields = ['first_name', 'email', 'profile.phone_no', 'profile.official_number', 'location_info.name']
            search_param = []
            if request.data["search"]:
                for sval in search_fields:
                    ar_prm = {
                       sval : {'$regex':request.data["search"], '$options':'i'}
                    }
                    search_param.append(ar_prm)
                match['$or'] = search_param
            # Search end
            match['role'] = 'barangay'
            match['deleted_at'] = None
            user_param['match'] = match

            user_info_count = {}
            user_info_count = mongo_query_barangay_count(user_param)
            user_info       = mongo_query_barangay_list(user_param)
            total_records   = user_info_count
            num_pages       = (total_records / page_size)
            num_pages       = round_up(num_pages)
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

class UpdateBarangayAPIView(generics.UpdateAPIView):
    """
     Update Barangay Here
    """
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    serializer_class = BarangayUpdateSerializer

    def update(self,request,id):
        try:
            email = request.data['email']
            EmailValidation.validate_email(email = email)
            barangay_user = Users.objects.filter(id = id).first()
            
            if not barangay_user:
                return Response({"status":0,"message":constants.USER_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            if Users.objects.filter(email__iexact = request.data['email']).exclude(email=barangay_user.email).count():
                return Response({"status":0,"message":constants.EMAIL_EXISTS_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            
            barangay_profile_info = Profile.objects.filter(user = barangay_user).first()
            if Profile.objects.filter(phone_no = request.data['profile']['phone_no']).exclude(phone_no=barangay_profile_info.phone_no).count():
                return Response({"status":0,"message":constants.PHONENO_EXISTS_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
                
            if barangay_user.role =="barangay":
                barangay_serializer = self.get_serializer(barangay_user,data = request.data,context={"user_id":request.user.id})
                if barangay_serializer.is_valid(raise_exception = True):
                    barangay_serializer.save()
                    return Response({"status":1, "message":"Barangay updated successfully","data":barangay_serializer.data},status=status.HTTP_201_CREATED)
                return Response({"status":0, "message":barangay_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
            return Response({"status":0, "message":constants.USER_UNAUTHORIZED_ERROR_MSG},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)