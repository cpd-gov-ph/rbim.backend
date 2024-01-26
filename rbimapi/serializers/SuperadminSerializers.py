import constants
from rest_framework import serializers
from rbim.models import Profile, Users, Options
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from rbimapi.utilities import calculate_age
from rbimapi.serializers.CommonSerializers import JSONSerializerField
from rbimapi.mongoaggregate.dataCollector import mdb_user_email_by_id
class DObj(object):
    pass
class SuperAdminProfileSerializer(serializers.ModelSerializer):
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
class SuperAdminRegisterSerializer(serializers.ModelSerializer):
    profile = SuperAdminProfileSerializer(required=False)
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
                    'profile'
                ]
    def validate_email(self, value):
        if not value:
            raise exceptions.ParseError(constants.EMAIL_MANDATORY_ERROR_MSG)
        if Users.objects.filter(email__iexact=value).count():
            raise exceptions.ParseError(constants.EMAIL_EXISTS_ERROR_MSG)
        return value

    def validate_password(self, value):
        if not value:
            raise exceptions.ParseError(constants.PASSWORD_MANDATORY_ERROR_MSG)
        return value
    
    def validate_first_name(self, value):
        if not value:
            raise exceptions.ParseError(constants.FIRSTNAME_MANDATORY_ERROR_MSG)
        return value
    
    def create(self,data):
        profile_request = data['profile']
        user_data = {
            'first_name':data['first_name'], 
            'password':data['password'],
            'email':data['email']
        }
        data['role'] = constants.USER_ROLES[0]
        user_obj = Users.objects.create_user(  
            data = user_data, 
            is_active =True,
            role = data['role'],
        )
        if user_obj:
            token, created = Token.objects.get_or_create(user=user_obj)
        data['token'] = token
        profile, created = Profile.objects.get_or_create(user=user_obj)
        profile.official_number = profile_request['official_number']
        profile.gender = profile_request['gender']
        profile.dob = profile_request['dob']
        profile.phone_no = profile_request['phone_no']
        profile.address = profile_request['address']
        profile.created_by = user_obj.id
        profile.save()
        data['profile'] = profile
        return data
class UserLoginSerializer(serializers.Serializer):
    email  = serializers.CharField(max_length =255)
    password  = serializers.CharField(max_length = 255)
    def validate(self,data):
        email = data.get('email')
        password = data.get('password')
        param = {}
        param['match'] = {
            'str_email':email.upper()
        }
        user_id = mdb_user_email_by_id(param)
        if user_id:
            user = Users.objects.filter(id=user_id).first()
            if user.role == constants.USER_ROLES[3]:
                raise exceptions.ParseError(constants.NOT_ACCESS_ERROR_MSG)
            if user.check_password(password) == True:  
                token,created = Token.objects.get_or_create(user = user)
                data['id'] = user.id
                data['token'] = token.key
                data['email'] = user.email 
                data['first_name'] = user.first_name 
                data['role'] = user.role
                data['is_agree'] = user.is_agree
                data.pop('password')
                if ((data['is_agree'] == 0) and (data['role'] != "data_collector" or data['role'] != "superadmin")):
                    data['term_and_conditions'] = {"title":"", "meta_value":"", "updated_at":""}
                    term_and_conditions = Options.objects.filter(meta_key = "term_and_conditions").first()
                    if term_and_conditions:
                        data['term_and_conditions'] = {
                            "title":term_and_conditions.title,
                            "meta_value":term_and_conditions.meta_value,
                            "updated_at":term_and_conditions.updated_at
                        }
                return data
            else:
                raise exceptions.ParseError(constants.PASSWORD_WRONG_ERROR_MSG)
        else:
            raise exceptions.ParseError(constants.USER_NOT_FOUND_ERROR_MSG)
class DCLoginSerializer(serializers.Serializer):
    email  = serializers.CharField(max_length =255)
    password  = serializers.CharField(max_length = 255)
    fcm_token = serializers.CharField(max_length =255)
    def validate(self,data):
        email = data.get('email')
        password = data.get('password')
        fcm_token = data.get('fcm_token')
        param = {}
        param['match'] = {
            'str_email':email.upper()
        }
        user_id = mdb_user_email_by_id(param)
        if user_id:
            user = Users.objects.filter(id=user_id).first() 
            if user.role != constants.USER_ROLES[3]:
                raise exceptions.ParseError(constants.INVALID_ACCOUNT_ACCESS_ERROR_MSG)
            if user.check_password(password) == True:
                token,created = Token.objects.get_or_create(user = user)
                Token.objects.get(user=user).delete()
                token,created = Token.objects.get_or_create(user = user)
                user.fcm_token = fcm_token
                user.save()
                data['id'] = user.id
                data['token'] = token.key
                data['email'] = user.email 
                data['first_name'] = user.first_name 
                data['role'] = user.role
                data['is_agree'] = user.is_agree
                data.pop('password')
                data.pop('fcm_token')
                if (data['is_agree'] == 0) and (data['role'] == "data_collector"):
                    data['term_and_conditions'] = {"title":"", "meta_value":"", "updated_at":""}
                    term_and_conditions = Options.objects.filter(meta_key = "term_and_conditions").first()
                    if term_and_conditions:
                        data['term_and_conditions'] = {
                            "title":term_and_conditions.title,
                            "meta_value":term_and_conditions.meta_value,
                            "updated_at":term_and_conditions.updated_at
                        }                        
                return data
            else:
                raise exceptions.ParseError(constants.PASSWORD_WRONG_ERROR_MSG)
        else:
            raise exceptions.ParseError(constants.USER_NOT_FOUND_ERROR_MSG)
class ForgotPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['reset_code',
                'is_reset_mail_send',
                ]
class SuperadminSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField('get_profile')
    def get_profile(self, user):
        return SuperAdminProfileSerializer(Profile.objects.get(user_id=user.id)).data
    class Meta:
        model = Users
        fields = [
                    'id',
                    'first_name',
                    'email',
                    'role',
                    'profile',
                ]
        read_only_fields = [
            'id'
        ]
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['id','meta_key','title','meta_value','updated_at']  
        read_only_fields = [
            'id'
        ]
    def validate_meta_key(self, value):
        if not value:
            raise exceptions.ParseError(constants.META_KEY_MANDATORY_ERROR_MSG)
        return value
    
    def validate_meta_value(self, value):
        if not value:
            raise exceptions.ParseError(constants.META_VALUE_MANDATORY_ERROR_MSG)
        return value
    
    def create(self,data):
        Options.objects.update_or_create(
            meta_key = data['meta_key'],
            defaults={
                'title': data.get('title', None),
                'meta_value': data.get('meta_value', None)
            },
        )
        return data
class SuperAdminUpdateSerializer(serializers.ModelSerializer):
    profile = SuperAdminProfileSerializer(required=False)
    class Meta:
        model = Users
        fields = [
                    'id',
                    'first_name',
                    'email',
                    'profile'
                ]
        read_only_fields = [
            'id'
        ]
    def update(self,user,data):
        profile_request = data['profile']
        user.email = data['email']
        user.first_name = data['first_name']
        profile = Profile.objects.get(user=user.id)
        profile.official_number = profile_request['official_number']
        profile.gender = profile_request['gender']
        profile.phone_no = profile_request['phone_no']
        profile.save()
        user.save()
        data['profile'] = profile
        return data
class DashboardSerializer(serializers.ModelSerializer):
    dashboard_count = JSONSerializerField()
    class Meta:
        model = Profile
        fields = [
                    'id',
                    'dashboard_count'
                ]
        read_only_fields = [
            'id'
        ]