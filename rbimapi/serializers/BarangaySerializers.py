import constants
from rest_framework import serializers
from rbim.models import City, Municipality, Location, Profile, Users
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from rbimapi.utilities import calculate_age, random_password, remove_slug_in_role
from rbimapi.serializers.CommonSerializers import CitySerializer, MunicipalitySerializer, LocationSerializer
import emailConstants
from django.conf import settings
from rbimapi.serializers.NotificationHistorySerializers import NotificationHistorySerializer
import staticContent
class BarangayProfileSerializer(serializers.ModelSerializer):
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
class BarangaySerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField('get_profile')
    city    = CitySerializer(read_only = True)
    city_id = serializers.PrimaryKeyRelatedField(queryset=City.objects.all(), source='city')
    location = LocationSerializer(read_only = True)
    location_id = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), source='location')
    municipality = MunicipalitySerializer(read_only = True)
    municipality_id = serializers.PrimaryKeyRelatedField(queryset=Municipality.objects.all(), source='municipality')
    def get_profile(self, user):
        return BarangayProfileSerializer(Profile.objects.get(user_id=user.id)).data
    class Meta:
        model = Users
        fields = [
                    'id',
                    'first_name',
                    'email',
                    'role',
                    'profile',
                    'city_id',
                    'city',
                    'location_id',
                    'location',
                    'municipality_id',
                    'municipality',
                ]
        read_only_fields = [
            'id'
        ]
class BarangayRegisterSerializer(serializers.ModelSerializer):
    profile = BarangayProfileSerializer(required=False)
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
                    'profile',
                    'city',
                    'location',
                    'municipality',
                ]
    def validate_email(self, value):
        if not value:
            raise exceptions.ParseError(constants.EMAIL_MANDATORY_ERROR_MSG)
        if Users.objects.filter(email__iexact=value).count():
            raise exceptions.ParseError(constants.EMAIL_EXISTS_ERROR_MSG)
        return value
    
    def validate_city(self, value):
        if not value:
            raise exceptions.ParseError(constants.CITY_MANDATORY_ERROR_MSG)
        return value

    def validate_municipality(self, value):
        if not value:
            raise exceptions.ParseError(constants.MUNICIPALITY_MANDATORY_ERROR_MSG)
        return value

    def validate_location(self, value):
        if not value:
            raise exceptions.ParseError(constants.LOCATION_MANDATORY_ERROR_MSG)
        return value

    def validate_first_name(self, value):
        if not value:
            raise exceptions.ParseError(constants.FIRSTNAME_MANDATORY_ERROR_MSG)
        return value
    
    def create(self,data):
        password = random_password()
        data['password'] = password
        profile_request = data['profile']
        barangay_user_data = {
            'first_name':data['first_name'], 
            'email':data['email'],
            'city':data['city'],
            'municipality' :data['municipality'],
            'location' :data['location'],
            'password':password
        }
        if Profile.objects.filter(phone_no=profile_request['phone_no']).count():
            raise exceptions.ParseError(constants.PHONENO_EXISTS_ERROR_MSG)
        data['role'] = constants.USER_ROLES[1]
        barangay_user_obj = Users.objects.create_user(
            data = barangay_user_data,
            is_active =True,
            role = data['role']
        )
        if barangay_user_obj:
            token, created = Token.objects.get_or_create(user=barangay_user_obj)
        data['token'] = token
        data['id']=barangay_user_obj.id
        barangay_profile, created = Profile.objects.get_or_create(user=barangay_user_obj)
        barangay_profile.official_number = profile_request['official_number']
        barangay_profile.gender = profile_request['gender']
        barangay_profile.dob = profile_request['dob']
        barangay_profile.phone_no = profile_request['phone_no']
        barangay_profile.address = profile_request['address']
        barangay_profile.created_by = barangay_user_obj.id
        barangay_profile.save()
        data['profile'] = barangay_profile
        barangay_user_obj.dashboard_count_auto_update()
        role = remove_slug_in_role(role = barangay_user_obj.role)
        html_content = emailConstants.EMAIL_MESSAGE_ONBOARD.format(barangay_user_obj.first_name, role, barangay_user_obj.email, password, settings.HOST_URL)
        barangay_user_obj.welcome_email_for_onboard(title=emailConstants.SUBJECT_ONBOARD, email=barangay_user_obj.email, html_content=html_content)
        return data
class BarangayUpdateSerializer(serializers.ModelSerializer):
    profile = BarangayProfileSerializer(required=False)
    class Meta:
        model = Users
        fields = [
                    'id',
                    'first_name',
                    'email',
                    'profile',
                    'city',
                    'location',
                    'municipality',
                ]
        read_only_fields = [
            'id'
        ]
    def update(self,user,data):
        profile_request = data['profile']
        barangay_user_obj = Users.objects.get(id=user.id)
        if barangay_user_obj.email != data['email']:
            password = random_password()
            role = remove_slug_in_role(role = barangay_user_obj.role)
            html_content = emailConstants.EMAIL_MESSAGE_ONBOARD.format(data['first_name'], role, data['email'], password, settings.HOST_URL)
            barangay_user_obj.welcome_email_for_onboard(title=emailConstants.SUBJECT_ONBOARD, email=data['email'], html_content=html_content)
            user.set_password(password)
        user.email = data['email']
        user.first_name = data['first_name']
        user.city = data['city']
        user.location = data['location']
        user.municipality = data['municipality']
        barangay_profile = Profile.objects.get(user=user.id)
        barangay_profile.official_number = profile_request['official_number']
        barangay_profile.gender = profile_request['gender']
        barangay_profile.dob = profile_request['dob']
        barangay_profile.phone_no = profile_request['phone_no']
        barangay_profile.address = profile_request['address']
        barangay_profile.save()
        user.save()
        receiver_obj = Users.objects.filter(id=barangay_user_obj.id).first()
        nt_message = emailConstants.NT_MESSAGE_PROFILE_UPDATE.format(receiver_obj.first_name, receiver_obj.email)
        email_message = emailConstants.EMAIL_MESSAGE_PROFILE_UPDATE.format(receiver_obj.first_name, receiver_obj.email)
        sender=self.context.get('user_id')
        title = emailConstants.SUBJECT_PROFILE_UPDATE
        profile_update_param = staticContent.notification_param(sender=sender, receiver=receiver_obj.id, title=title, nt_message=nt_message, email_message=email_message, email=receiver_obj.email)
        nh_serializer = NotificationHistorySerializer(data=profile_update_param) 
        nh_serializer.is_valid(raise_exception = True)
        nh_serializer.save()
        data['profile'] = barangay_profile
        return data