from rest_framework import serializers
from rbim.models import City, Municipality, Location, Users
from rbim.models import Profile
from rest_framework import exceptions
import constants
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','name','code']  
        read_only_fields = [
            'id'
        ]
    def create(self,validated_data):
        return super().create(validated_data)   
class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = ['id','name','code','city']  
        read_only_fields = [
            'id'
        ]
    def create(self,validated_data):
        return super().create(validated_data)  
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id','name','code','municipality']  
        read_only_fields = [
            'id'
        ]
    def create(self,validated_data):
        return super().create(validated_data)
class OfficialNumberSerializer(serializers.ModelSerializer):
     class Meta:
        model = Profile
        fields = ['id', 'official_number']
        read_only_fields = [
            'id'
        ]
class UserNameSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField('get_profile')
    def get_profile(self, user):
        profile = Profile.objects.get(user_id=user.id)
        if not profile:
            raise exceptions.ParseError(constants.DATA_NOT_FOUND_ERROR_MSG)
        profile_obj = OfficialNumberSerializer(profile).data
        first_name = user.first_name + '(' + profile_obj['official_number'] + ')'
        return  first_name
    class Meta:
        model = Users
        fields = ['id', 'first_name']
        read_only_fields = [
            'id'
        ]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'email']
        read_only_fields = [
            'id'
        ]
class SurveyEntryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'barangay_id', 'data_reviewer_id']
        read_only_fields = [
            'id'
        ]
class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""
    def to_internal_value(self, data):
        return data
    def to_representation(self, value):
        return value