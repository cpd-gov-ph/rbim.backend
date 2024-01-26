from rest_framework import serializers
from rbim.models import OcrOptions, OcrMaster
class OcrOptionsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = OcrOptions
class CensusImagesOcrStatusSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = OcrMaster