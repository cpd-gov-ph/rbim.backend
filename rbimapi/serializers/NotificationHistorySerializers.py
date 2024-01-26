from rest_framework import serializers
from rbim.models import NotificationHistory
class NotificationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationHistory
        fields = '__all__'
        read_only_fields = [
            'id'
        ]
    def create(self,validated_data):
        instance = NotificationHistory.objects.create(**validated_data)
        instance.user_email_trigger(title=instance.title, html_content=instance.email_message, email=instance.email)
        instance.user_push_notification_trigger(title=instance.title, html_content=instance.message, receiver_id=instance.receiver_id)
        return instance