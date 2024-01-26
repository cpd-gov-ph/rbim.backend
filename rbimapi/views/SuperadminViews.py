from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rbimapi.validations import EmailValidation
from rbim.models import Users,Profile
from rbimapi.permissions import IsSuperadminAuthenticated
from rbimapi.serializers.SuperadminSerializers import SuperAdminRegisterSerializer, SuperAdminUpdateSerializer, DashboardSerializer
import constants

class CreateSuperAdminAPIView(generics.CreateAPIView):
    '''
    Create Static superadmin here
    '''
    serializer_class = SuperAdminRegisterSerializer
    def create(self,request):
        try:
            serializer = self.get_serializer(data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                return Response({"status":1, "message":"Superadmin created successfully", "data":serializer.data},status=status.HTTP_201_CREATED)
            return Response({"status":0, "message":constants.REGISTRATION_FAILED_ERROR_MSG},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class UpdateSuperAdminAPIView(generics.UpdateAPIView):
    """
     Update Superadmin Here
    """
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperadminAuthenticated,]
    serializer_class = SuperAdminUpdateSerializer

    def update(self,request,id):
        try:
            email = request.data['email']
            EmailValidation.validate_email(email = email)
            user = Users.objects.filter(id = id).first()
            if not user:
                return Response({"status":0,"message":constants.USER_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            if user.role =="superadmin":
                serializer = self.get_serializer(user,data = request.data)
                if serializer.is_valid(raise_exception = True):
                    serializer.save()
                    return Response({"status":1, "message":"Superadmin updated successfully","data":serializer.data},status=status.HTTP_201_CREATED)
                return Response({"status":0, "message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
            return Response({"status":0, "message":constants.USER_UNAUTHORIZED_ERROR_MSG},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class GetDashboardDetailsAPIVIEW(generics.RetrieveAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes = [IsSuperadminAuthenticated,]
    serializer_class = DashboardSerializer
    def get(self, request):
        try:
            profile_obj = Profile.objects.filter(user=request.user).first()
            dashboard_details = self.get_serializer(profile_obj).data
            if not profile_obj:
                return Response({"status":0,"message":constants.DATA_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            return Response({"status":1,"message":"User data retrieved","data":dashboard_details},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

