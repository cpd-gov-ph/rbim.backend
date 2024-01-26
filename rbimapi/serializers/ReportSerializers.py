import json
from rest_framework import serializers
from rbim.models import ReportCategories, ReportHistory, Location
class ReportCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCategories
        fields = ['id', 'category_name']
        read_only_fields = [
            'id'
        ]
class ReportHistorySerializer(serializers.ModelSerializer):
    chart_response_left = serializers.SerializerMethodField()
    chart_response_right = serializers.SerializerMethodField()
    category_type = serializers.SerializerMethodField()
    location_name = serializers.SerializerMethodField()
    def get_chart_response_left(self, obj):
        return json.loads(json.dumps(obj.chart_response_left))
    
    def get_chart_response_right(self, obj):
        return json.loads(json.dumps(obj.chart_response_right))

    def get_category_type(self, obj):
        category_obj = ReportCategories.objects.get(id=obj.report_category_id)
        category = ReportCategorySerializer(category_obj).data
        return category['category_name']

    def get_location_name(self, obj):
        location_obj = Location.objects.filter(id=obj.location_id).first()
        return location_obj.name
    class Meta:
        model = ReportHistory
        fields = ['id', 'location_id' , 'location_name', 'report_category_id', 'category_type', 'meta_value',
                  'chart_response_left', 'chart_response_right', ]
        read_only_fields = [
            'id'
        ]