from rest_framework import generics, status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
import constants
from rbimapi.permissions import IsSuperadminAuthenticated
from rbimapi.serializers.CommonSerializers import UserNameSerializer
from rbim.models import Users, Municipality, Location
from datetime import date

class BarangayNameListAPIViews(generics.ListAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsSuperadminAuthenticated,]
    serializer_class    = UserNameSerializer
    def get(self,request):
        try:
            user_obj     = Users.objects.filter(role = "barangay").filter(deleted_at__isnull=True)
            serializer = self.get_serializer(user_obj , many=True)
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

class DatareviewerNameListAPIViews(generics.ListAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsSuperadminAuthenticated,]
    serializer_class    = UserNameSerializer
    def get(self, request, barangay_id):
        try:
            user_obj     = Users.objects.filter(role = "data_reviewer").filter(barangay_id = barangay_id).filter(deleted_at__isnull=True)
            serializer = self.get_serializer(user_obj , many=True)
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

class UserRoleIDAPIView(APIView):
    permission_classes = [AllowAny,]

    def post(self,request):
        municipality = request.data.get('municipality')
        location = request.data.get('location')
        role = request.data.get('role')
        barangay = request.data.get('barangay')
        current_year = str(date.today().year)[-2:]
        if barangay:
            get_bo = Users.objects.filter(id=barangay).first()
            get_municipality = Municipality.objects.filter(id=get_bo.municipality_id).first().name
            get_location = Location.objects.filter(id=get_bo.location_id).first().name
            official_m = get_municipality[:2].upper()
            official_l = get_location[:3].upper()
        else:
            official_m = municipality[:2].upper()
            official_l = location[:3].upper()
        if role == constants.USER_ROLES[1]:
            get_barangay_count = Users.objects.filter(role=constants.USER_ROLES[1]).count()
            offcial_id = "{}{}BO{}{:02}".format(official_m, official_l, current_year[-2:], get_barangay_count+1)
        if role == constants.USER_ROLES[2]:
            get_dr_count = Users.objects.filter(role=constants.USER_ROLES[2]).count()
            offcial_id = "{}{}DR{}{:02}".format(official_m, official_l, current_year[-2:], get_dr_count+1)
        if role == constants.USER_ROLES[3]:
            get_dc_count = Users.objects.filter(role=constants.USER_ROLES[3]).count()
            offcial_id = "{}{}DC{}{:02}".format(official_m, official_l, current_year[-2:], get_dc_count+1)
        return Response(dict(status=1, message="Officail ID generated", offcial_id=offcial_id),status=status.HTTP_200_OK)




