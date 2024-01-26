import constants
from django.db import transaction
from django.utils import timezone
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rbim.models import (OcrOptions, OcrMaster, SurveyEntry, Users)
from rbimapi.serializers.OcrSerializers import (OcrOptionsSerializers, CensusImagesOcrStatusSerializers)
from rbimapi.services.ocr import call_ocr_thread
from rbimapi.services.s3_uploader import upload_images_to_s3, check_file_extension


class OcrOptionsAPIView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        snippets = OcrOptions.objects.all()
        serializer = OcrOptionsSerializers(snippets, many=True)
        return Response(dict(status=1, message="Ocr options retrieved successfully", options=serializer.data),
                        status=status.HTTP_200_OK)

    def post(self, request):
        options = request.data.get('options')
        saved_ = True
        for option in options:
            serializer = OcrOptionsSerializers(data=dict(qid=option['qid'], ops=option['Ops']))
            if serializer.is_valid():
                serializer.save()
        if not saved_:
            return Response(dict(status=0, message="Failed to save ocr options"), status=status.HTTP_400_BAD_REQUEST)
        return Response(dict(status=1, message="Ocr options saved successfully"), status=status.HTTP_201_CREATED)


class CensusImageUploadAPIView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        census_images_count = request.data.get('census_images_count', 0)
        data_reviewer = Users.objects.filter(id=request.user.id).first()
        census_images = []

        if int(census_images_count) == 0 or int(census_images_count) < 11 or int(census_images_count) > 11:
            return Response(dict(status=0, message="All Images required for ocr process"),
                            status=status.HTTP_400_BAD_REQUEST)

        for i in range(0, int(census_images_count)):
            census_images.append(request.FILES.get(f'census_images[{i}]'))

        check_extention = check_file_extension(images=census_images)
        saved_ = True
        if check_extention:
            with transaction.atomic():
                create_survey_entry = SurveyEntry.objects.create(data_reviewer_id=data_reviewer.id,
                                                                 barangay_id=data_reviewer.barangay_id,
                                                                 status=constants.SURVEY_STATUS[0],
                                                                 survey_assigned_on=timezone.now(),
                                                                 survey_type=constants.SURVEY_TYPE[1],
                                                                 is_open_ndividual_view=False
                                                                 )
                ocr_images = upload_images_to_s3(images=census_images, survey_id=create_survey_entry.id)
                OcrMaster.objects.create(survey_entry_id=create_survey_entry.id, ocr_images=ocr_images,
                                         created_by_id=request.user.id)

            # calling ocr class in thread
            call_ocr_thread(survey_entry_id=create_survey_entry.id, request=request)
        else:
            return Response(dict(status=0, message="Invalid file type, Accepted file types are jpg,jpeg,png"),
                            status=status.HTTP_400_BAD_REQUEST)

        if not saved_:
            return Response(dict(status=0, message="Upload failed"), status=status.HTTP_400_BAD_REQUEST)
        return Response(dict(status=1, message="Census image saved successfully, OCR process started"),
                        status=status.HTTP_201_CREATED)
