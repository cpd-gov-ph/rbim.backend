import constants
from rest_framework import serializers
from rbim.models import Profile, Users, Location, Municipality, Tasks, City
from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from rbimapi.utilities import calculate_age, random_password, remove_slug_in_role
import emailConstants
from django.conf import settings
from rbimapi.serializers.NotificationHistorySerializers import NotificationHistorySerializer
import staticContent
from rbimapi.serializers.CommonSerializers import CitySerializer
class DataCollectorProfileSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(format="%Y-%m-%dT%H:%M:%S")
    age = serializers.SerializerMethodField('get_age')
    def get_age(self, user):
        user_obj = Profile.objects.filter(id=user.id).first()
        age = calculate_age(dob= user_obj.dob)
        return age
    class Meta:
        model = Profile
        fields = ['id', 'official_number','dob','age', 'gender', 'phone_no','address']
        read_only_fields = [
            'id'
        ]
class DatacollectorRegisterSerializer(serializers.ModelSerializer):
    profile = DataCollectorProfileSerializer(required=False)
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
                    'data_reviewer_id',
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
        dc_user_data = {
            'first_name':data['first_name'], 
            'email':data['email'],
            'barangay_id' :data['barangay_id'],
            'data_reviewer_id' :data['data_reviewer_id'],
            'password':password  
        }
        if Profile.objects.filter(phone_no=profile_request['phone_no']).count():
            raise exceptions.ParseError(constants.PHONENO_EXISTS_ERROR_MSG)
        data['role'] = constants.USER_ROLES[3]
        dc_user_obj = Users.objects.create_user(
            data = dc_user_data,
            is_active =True,
            role = data['role']
        )   
        if dc_user_obj:
            token, created = Token.objects.get_or_create(user=dc_user_obj)
        data['token'] = token
        data['id']=dc_user_obj.id
        dc_profile, created = Profile.objects.get_or_create(user=dc_user_obj)
        dc_profile.official_number = profile_request['official_number']
        dc_profile.gender = profile_request['gender']
        dc_profile.dob = profile_request['dob']
        dc_profile.phone_no = profile_request['phone_no']
        dc_profile.address = profile_request['address']
        dc_profile.created_by = dc_user_obj.id
        dc_profile.save()
        data['profile'] = dc_profile
        dc_user_obj.dashboard_count_auto_update()
        role = remove_slug_in_role(role = dc_user_obj.role)
        html_content = emailConstants.EMAIL_MESSAGE_ONBOARD.format(dc_user_obj.first_name, role, dc_user_obj.email, password, settings.DC_HOST_URL)
        dc_user_obj.welcome_email_for_onboard(title=emailConstants.SUBJECT_ONBOARD, email=dc_user_obj.email, html_content=html_content)
        return data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name']
        read_only_fields = [
            'id'
        ]
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id','name','code','municipality']  
        read_only_fields = [
            'id'
        ]
class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = ['id','name','code','city']  
        read_only_fields = [
            'id'
        ]
    def create(self,validated_data):
        return super().create(validated_data)
class DataCollectorSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField('get_profile')
    def get_profile(self, user):
        return DataCollectorProfileSerializer(Profile.objects.get(user_id=user.id)).data
    barangay = serializers.SerializerMethodField('get_barangay')
    def get_barangay(self, user):
        if user.barangay_id:
            return UserSerializer(Users.objects.get(id=user.barangay_id)).data
        return {}
    barangay_location = serializers.SerializerMethodField('get_barangay_location')
    def get_barangay_location(self, user):
        if user.barangay_id:
            barangay_info = Users.objects.filter(id=user.barangay_id).first()
            return LocationSerializer(Location.objects.get(id=barangay_info.location_id)).data
        return {}
    data_reviewer = serializers.SerializerMethodField('get_data_reviewer')
    def get_data_reviewer(self, user):
        if user.data_reviewer_id:
            return UserSerializer(Users.objects.get(id=user.data_reviewer_id)).data
        return {}
    municipality = serializers.SerializerMethodField('get_municipality')
    def get_municipality(self, user):
        if user.barangay_id:
            barangay_info = Users.objects.filter(id=user.barangay_id).first()
            return MunicipalitySerializer(Municipality.objects.get(id=barangay_info.municipality_id)).data
        return {}
    city = serializers.SerializerMethodField('get_city')
    def get_city(self, user):
        if user.barangay_id:
            barangay_info = Users.objects.filter(id=user.barangay_id).first()
            return CitySerializer(City.objects.get(id=barangay_info.city_id)).data
        return {}
    class Meta:
        model = Users
        fields = [
                    'id',
                    'first_name',
                    'email',
                    'role',
                    'barangay_id',
                    'data_reviewer_id',
                    'profile',
                    'municipality',
                    'barangay',
                    'barangay_location',
                    'data_reviewer',
                    'city'
                ]
        read_only_fields = [
            'id'
        ]
class DataCollectorUpdateSerializer(serializers.ModelSerializer):
    profile = DataCollectorProfileSerializer(required=False)
    class Meta:
        model = Users
        fields = [
                    'id',
                    'first_name',
                    'email',
                    'barangay_id',
                    'data_reviewer_id',
                    'profile'
                ]
        read_only_fields = [
            'id'
        ]
    def update(self,user,data):
        profile_request = data['profile']
        dc_user_obj = Users.objects.get(id=user.id)
        if dc_user_obj.email != data['email']:
            password = random_password()
            role = remove_slug_in_role(role = dc_user_obj.role)
            html_content = emailConstants.EMAIL_MESSAGE_ONBOARD.format(data['first_name'], role, data['email'], password, settings.DC_HOST_URL)
            dc_user_obj.welcome_email_for_onboard(title=emailConstants.SUBJECT_ONBOARD, email=data['email'], html_content=html_content)
            user.set_password(password)
        user.email = data['email']
        user.first_name = data['first_name']
        user.barangay_id = data['barangay_id']
        user.data_reviewer_id = data['data_reviewer_id']
        dc_profile = Profile.objects.get(user=user.id)
        dc_profile.official_number = profile_request['official_number']
        dc_profile.gender = profile_request['gender']
        dc_profile.dob = profile_request['dob']
        dc_profile.phone_no = profile_request['phone_no']
        dc_profile.address = profile_request['address']
        dc_profile.save()
        user.save()
        receiver_obj = Users.objects.filter(id=dc_user_obj.id).first()
        nt_message = emailConstants.NT_MESSAGE_PROFILE_UPDATE.format(receiver_obj.first_name, receiver_obj.email)
        email_message = emailConstants.EMAIL_MESSAGE_PROFILE_UPDATE.format(receiver_obj.first_name, receiver_obj.email)
        sender=self.context.get('user_id')
        title = emailConstants.SUBJECT_PROFILE_UPDATE
        profile_update_param = staticContent.notification_param(sender=sender, receiver=receiver_obj.id, title=title, nt_message=nt_message, email_message=email_message, email=receiver_obj.email)
        nh_serializer = NotificationHistorySerializer(data=profile_update_param) 
        nh_serializer.is_valid(raise_exception = True)
        nh_serializer.save()
        data['profile'] = dc_profile
        return data
class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
                    'id',
                    'task_no',
                    'data_collector',
                    'title',
                    'description',
                    'created_by'
                ]
    def create(self,data):        
        total_task= Tasks.objects.filter(data_collector=data['data_collector']).count() + 1   
        if total_task:
            task_no = total_task
        else:
            task_no = 1 
        task = Tasks.objects.create(
            task_no = task_no,
            data_collector = data['data_collector'],
            title = data['title'],
            description = data['description'],
            created_by = data['created_by'],
        )      
        task.save()
        data['id'] = task.id
        data['task_no'] = task.task_no
        return data
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
                    'id',
                    'task_no',
                    'data_collector',
                    'title',
                    'description'
                ]
        read_only_fields = [
            'id'
        ]