from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rbimapi.permissions import IsSuperadminAuthenticated
from rbimapi.utilities import otp_generator
from rbimapi.serializers.SuperadminSerializers import UserLoginSerializer, DCLoginSerializer, ForgotPasswordSerializer, SuperadminSerializer, OptionSerializer
from rbimapi.serializers.BarangaySerializers import BarangaySerializer
from rbimapi.serializers.DataReviewerSerializers import DatareviewerSerializer
from rbimapi.serializers.DatacollectorSerializer import DataCollectorSerializer
from rbimapi.serializers.NotificationHistorySerializers import NotificationHistorySerializer
from rbimapi.mongoaggregate.dataCollector import mdb_user_email_by_id
from rbim.models import Users, Options
import constants
import emailConstants
import staticContent
class UserLoginAPIView(APIView):
    def post(self,request):
        try:
            #headers:
            mandatory_fields = ['email','password']
            #validation:
            for i in mandatory_fields:
                if i not in request.data.keys():
                    return Response({"status":0, "message":"{} - is request".format(i)},status=status.HTTP_400_BAD_REQUEST)
            if request.data['email'] == "":
                return Response({"status":0, "message":constants.EMAIL_MANDATORY_ERROR_MSG},status=status.HTTP_400_BAD_REQUEST)
            if request.data['password'] == "":
                return Response({"status":0, "message":constants.PASSWORD_MANDATORY_ERROR_MSG},status=status.HTTP_400_BAD_REQUEST)
            #process:
            serializer = UserLoginSerializer(data = request.data)
            if serializer.is_valid(raise_exception = True):   
                return Response({"status":1, "message":"Success", "data":serializer.validated_data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class DataCollectorLoginAPIView(APIView):
    """
    Data Collector Login
    """
    def post(self,request):
        try:
            #headers:
            mandatory_fields = ['email','password','fcm_token']
            #validation:
            for i in mandatory_fields:
                if i not in request.data.keys():
                    return Response({"status":0, "message":"{} - is request".format(i)},status=status.HTTP_400_BAD_REQUEST)
            if request.data['email'] == "":
                return Response({"status":0, "message":constants.EMAIL_MANDATORY_ERROR_MSG},status=status.HTTP_400_BAD_REQUEST)
            if request.data['password'] == "":
                return Response({"status":0, "message":constants.PASSWORD_MANDATORY_ERROR_MSG},status=status.HTTP_400_BAD_REQUEST)
            #process:
            serializer = DCLoginSerializer(data = request.data)
            if serializer.is_valid(raise_exception = True):   
                return Response({"status":1, "message":"Success", "data":serializer.validated_data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordAPIView(APIView):
    def post(self,request):
        try:
            email = request.data['email']
            param = {}
            param['match'] = {
                'str_email':email.upper()
            }
            user_id = mdb_user_email_by_id(param)
            if not user_id:
                return Response({"status":0, "message":constants.EMAIL_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            
            user = Users.objects.filter(id=user_id).first()
            generate_code = otp_generator()
            user_obj = Users.objects.filter(reset_code =generate_code).first()
            if user_obj:
                re_generate_code = otp_generator()
                user_obj.user_forgot_password_email(email = user.email,code = re_generate_code)
                request_data ={
                    "reset_code" : re_generate_code,
                    "is_reset_mail_send": True
                }
            else:
                user.user_forgot_password_email(email = user.email,code = generate_code)
                request_data ={
                    "reset_code" : generate_code,
                    "is_reset_mail_send": True
                }
            serializer = ForgotPasswordSerializer(user,data = request_data,partial =True)
            serializer.is_valid()
            serializer.save()              
            return Response({"status":1,"message":"Mail has been sent to registered mailID"},status = status.HTTP_200_OK)     
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class VerifyCodeAPIView(APIView):
    def post(self,request):
        try:
            email = request.data['email']
            param = {}
            param['match'] = {
                'str_email':email.upper()
            }
            user_id = mdb_user_email_by_id(param)
            if not user_id:
                return Response({"status":0, "message":"Email not found"},status = status.HTTP_404_NOT_FOUND)
            
            user = Users.objects.filter(id=user_id).first()
            if user:
                if user.reset_code == request.data['reset_code']:
                    return Response({"status":1,"message":"Verification code is valid"},status=status.HTTP_200_OK)           
                else:            
                    return Response({"status":0,"message":constants.VERIFICATION_CODE_INVALID_ERROR_MSG},status=status.HTTP_400_BAD_REQUEST)           
            else:
                return Response({"status":0,"message":constants.EMAIL_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordAPIView(APIView):
   
    def post(self,request):
        try:
            email = request.data['email']
            param = {}
            param['match'] = {
                'str_email':email.upper()
            }
            user_id = mdb_user_email_by_id(param)
            if not user_id:
                return Response({"status":0, "message":"Email not found"},status = status.HTTP_404_NOT_FOUND)
            
            user = Users.objects.filter(id=user_id).first()
            if user:
                if user.reset_code == request.data['reset_code']:
                    if request.data['new_password'] != request.data['reenter_password']:                                                       #password - confirm
                        return Response({"status":0,"message":"Password mismatch"}) 
                    user.set_password(request.data['new_password'])                  
                    user.save()
                    return Response({"status":1,"message":"Password updated successfully"},status = status.HTTP_200_OK)  
                else:            
                    return Response({"status":0,"message":constants.VERIFICATION_CODE_INVALID_ERROR_MSG},status=status.HTTP_400_BAD_REQUEST)           
            else:
                return Response({"status":0,"message":constants.EMAIL_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class ResendCodeAPIView(APIView):
   
    def post(self,request):
        try:
            user = Users.objects.filter(email__iexact = request.data['email']).first()
            if user:
                user.user_forgot_password_email(email = user.email,code =user.reset_code)
                return Response({"status":1,"message":"Mail has been sent to registered mailID"},status = status.HTTP_200_OK)               
            else:
                return Response({"status":0,"message":constants.EMAIL_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def get(self,request):
        try:
            if request.user.role == constants.USER_ROLES[3]:
                Users.objects.filter(id=request.user.id).update(fcm_token= None)
            request.user.auth_token.delete()
            return Response({"status":1,"message":"Logged out successfully"},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class TokenUserViewAPIView(generics.RetrieveAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def get(self, request):
        try:
            user_obj = Users.objects.filter(id = request.user.id).first()
            if user_obj.role == "superadmin":
                user_obj = SuperadminSerializer(user_obj).data
            elif user_obj.role == "barangay":
                user_obj = BarangaySerializer(user_obj).data
            elif user_obj.role == "data_reviewer":
                user_obj = DatareviewerSerializer(user_obj).data
            elif user_obj.role == "data_collector":
                user_obj = DataCollectorSerializer(user_obj).data
            if not user_obj:
                return Response({"status":0,"message":constants.USER_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            return Response({"status":1,"message":"User data retrieved","data":user_obj},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class LegalDocumentAgreeAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    def post(self, request):
        try:
            user = Users.objects.filter(id = request.user.id).first()
            user.is_agree = request.data['is_agree']
            user.save()
            if not user:
                return Response({"status":0,"message":constants.USER_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            
            nt_message = emailConstants.NT_MESSAGE_ACCOUNT_ACTIVE.format(user.first_name)
            email_message = emailConstants.EMAIL_MESSAGE_ACCOUNT_ACTIVE.format(user.first_name)
            title = emailConstants.SUBJECT_ACCOUNT_ACTIVE
            user_account_active_param = staticContent.notification_param(sender=user.id, receiver=user.id, title=title, nt_message=nt_message, email_message=email_message, email=user.email)
            serializer = NotificationHistorySerializer(data=user_account_active_param)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response({"status":1,"message":"User accepted the legal document"},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)


class OptionsCreateUpdateView(generics.CreateAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsSuperadminAuthenticated,]
    serializer_class = OptionSerializer
    def create(self,request):
        try:
            serializer = self.get_serializer(data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                return Response({"status":1, "message":"Updated Successfully","data":serializer.data},status=status.HTTP_201_CREATED)
            return Response({"status":0, "message":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)


class OptionsAPIView(generics.RetrieveAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    serializer_class    = OptionSerializer
    def get(self, request, meta_key):
        try:
            option_obj = Options.objects.filter(meta_key = meta_key).first()
            option_info = self.get_serializer(option_obj).data
            if not option_info:
                return Response({"status":0,"message":constants.DATA_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            return Response({"status":1,"message":"Data retrieved","data":option_info},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class LegalAndDocumentationAPIView(generics.RetrieveAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    serializer_class    = OptionSerializer
    def get(self, request):
        try:
            response_data ={}
            term_and_conditions = Options.objects.filter(meta_key = "term_and_conditions").first()
            term_and_conditions_info = self.get_serializer(term_and_conditions).data
            if term_and_conditions_info:
                response_data['term_and_conditions'] = term_and_conditions_info
            else:
                response_data['term_and_conditions'] = None
            privacy_and_policy = Options.objects.filter(meta_key = "privacy_and_policy").first()
            privacy_and_policy_info = self.get_serializer(privacy_and_policy).data
            if privacy_and_policy_info:
                response_data['privacy_and_policy'] = privacy_and_policy_info
            else:
                response_data['privacy_and_policy'] = None
            if not response_data:
                return Response({"status":0,"message":constants.DATA_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            return Response({"status":1,"message":"Data retrieved","data":response_data},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)