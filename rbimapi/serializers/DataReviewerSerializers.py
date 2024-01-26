import constants
from rest_framework import serializers
from rbim.models import Users, Profile, SurveyEntry
from rest_framework.authtoken.models import Token
from rbimapi.utilities import calculate_age, random_password, remove_slug_in_role
from rest_framework import exceptions
import emailConstants
from django.conf import settings
from rbimapi.serializers.NotificationHistorySerializers import NotificationHistorySerializer
import staticContent
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name']
        read_only_fields = [
            'id'
        ]
class DataReviewerProfileSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(format="%Y-%m-%dT%H:%M:%S")
    age = serializers.SerializerMethodField('get_age')
    def get_age(self, user):
        user_obj = Profile.objects.filter(id=user.id).first()
        age = calculate_age(dob= user_obj.dob)
        return age
    class Meta:
        model = Profile
        fields = ['id', 'official_number','dob','age','gender', 'phone_no','address']
        read_only_fields = [
            'id'
        ]
class DatareviewerSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField('get_profile')
    def get_profile(self, user):
        return DataReviewerProfileSerializer(Profile.objects.get(user_id=user.id)).data
    barangay = serializers.SerializerMethodField('get_barangay')
    def get_barangay(self, user):
        if user.barangay_id:
            return UserSerializer(Users.objects.get(id=user.barangay_id)).data
        return {}
    class Meta:
        model = Users
        fields = [
                    'id',
                    'first_name',
                    'email',
                    'role',
                    'barangay_id',
                    'profile',
                    'barangay',
                ]
        read_only_fields = [
            'id'
        ]
class DatareviewerRegisterSerializer(serializers.ModelSerializer):
    profile = DataReviewerProfileSerializer(required=False)
    token = serializers.CharField(
        allow_blank=True,
        read_only=True
    )
    class Meta(object):
        model = Users
        fields = [
                    'id',
                    'first_name',
                    'email',
                    'password',
                    'token',
                    'role',
                    'barangay_id',
                    'profile'
                ]
    def validate_email(self, value):
        if not value:
            raise exceptions.ParseError(constants.EMAIL_MANDATORY_ERROR_MSG)
        if Users.objects.filter(email__iexact=value).count():
            raise exceptions.ParseError(constants.EMAIL_EXISTS_ERROR_MSG)
        return value
    
    def validate_first_name(self, value):
        if not value:
            raise exceptions.ParseError(constants.FIRSTNAME_MANDATORY_ERROR_MSG)
        return value
    
    def create(self,data):
        password = random_password()
        data['password'] = password
        profile_request = data['profile']
        dr_user_data = {
            'first_name':data['first_name'], 
            'email':data['email'],
            'barangay_id' :data['barangay_id'],
            'password':password          
        }
        if Profile.objects.filter(phone_no=profile_request['phone_no']).count():
            raise exceptions.ParseError(constants.PHONENO_EXISTS_ERROR_MSG)
        data['role'] = constants.USER_ROLES[2]
        dr_user_obj = Users.objects.create_user(
            data = dr_user_data,
            is_active =True,
            role = data['role']
        )
        if dr_user_obj:
            token, created = Token.objects.get_or_create(user=dr_user_obj)
        data['token'] = token
        data['id']=dr_user_obj.id
        dr_profile, created = Profile.objects.get_or_create(user=dr_user_obj)
        dr_profile.official_number = profile_request['official_number']
        dr_profile.gender = profile_request['gender']
        dr_profile.dob = profile_request['dob']
        dr_profile.phone_no = profile_request['phone_no']
        dr_profile.address = profile_request['address']
        dr_profile.created_by = dr_user_obj.id
        dr_profile.save()
        data['profile'] = dr_profile
        dr_user_obj.dashboard_count_auto_update()
        role = remove_slug_in_role(role = dr_user_obj.role)
        html_content = emailConstants.EMAIL_MESSAGE_ONBOARD.format(dr_user_obj.first_name, role, dr_user_obj.email, password, settings.HOST_URL)
        dr_user_obj.welcome_email_for_onboard(title=emailConstants.SUBJECT_ONBOARD, email=dr_user_obj.email, html_content=html_content)
        return data
class DataReviewerUpdateSerializer(serializers.ModelSerializer):
    profile = DataReviewerProfileSerializer(required=False)
    class Meta:
        model = Users
        fields = [
                    'id',
                    'first_name',
                    'email',
                    'barangay_id',
                    'profile'
                ]
        read_only_fields = [
            'id'
        ]
    def update(self,user,data):
        profile_request = data['profile']
        dr_user_obj = Users.objects.get(id=user.id)
        if dr_user_obj.email != data['email']:
            password = random_password()
            role = remove_slug_in_role(role = dr_user_obj.role)
            html_content = emailConstants.EMAIL_MESSAGE_ONBOARD.format(data['first_name'], role, data['email'], password, settings.HOST_URL)
            dr_user_obj.welcome_email_for_onboard(title=emailConstants.SUBJECT_ONBOARD, email=data['email'], html_content=html_content)
            user.set_password(password)
        user.email = data['email']
        user.first_name = data['first_name']
        user.barangay_id = data['barangay_id']
        dr_profile = Profile.objects.get(user=user.id)
        dr_profile.official_number = profile_request['official_number']
        dr_profile.gender = profile_request['gender']
        dr_profile.dob = profile_request['dob']
        dr_profile.phone_no = profile_request['phone_no']
        dr_profile.address = profile_request['address']
        dr_profile.save()
        user.save()
        receiver_obj = Users.objects.filter(id=dr_user_obj.id).first()
        nt_message = emailConstants.NT_MESSAGE_PROFILE_UPDATE.format(receiver_obj.first_name, receiver_obj.email)
        email_message = emailConstants.EMAIL_MESSAGE_PROFILE_UPDATE.format(receiver_obj.first_name, receiver_obj.email)
        sender=self.context.get('user_id')
        title = emailConstants.SUBJECT_PROFILE_UPDATE
        profile_update_param = staticContent.notification_param(sender=sender, receiver=receiver_obj.id, title=title, nt_message=nt_message, email_message=email_message, email=receiver_obj.email)
        nh_serializer = NotificationHistorySerializer(data=profile_update_param) 
        nh_serializer.is_valid(raise_exception = True)
        nh_serializer.save()
        data['profile'] = dr_profile
        return data
class NextSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyEntry
        fields = [
            "id",
            "next_section"
        ]
        read_only_fields = [
            'id'
        ]