from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rbimapi.mongoaggregate.survey import mdb_pending_survey_entry
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
import emailConstants
import staticContent

class GetPendingSurveyAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def get(self,request):
        try:
            dyparam = {}
            dyparam['match'] = {
                'deleted_at': None,
                'status':{'$in':['survey_assigned','pending_for_approval']}
            }
            filter_survey_details = []
            res_survey_details = mdb_pending_survey_entry(dyparam)
            if res_survey_details:
                for row in res_survey_details:
                    email = row['email']
                    first_name = row['first_name']
                    survey_number = row['pending_survey_number']
                    nt_message = emailConstants.MESSAGE_BO_AND_DR_PENDING_SURVEY.format(first_name, survey_number)
                    email_message = emailConstants.EMAIL_MESSAGE_BO_AND_DR_PENDING_SURVEY.format(first_name, survey_number)
                    title = emailConstants.SUBJECT_BO_AND_DR_PENDING_SURVEY
                    pending_survey_param = staticContent.notification_param(sender=row['sender'], receiver=row['receiver'], title=title, nt_message=nt_message, email_message=email_message, email=email)
                    filter_survey_details.append(pending_survey_param)
            return Response({"status":1, "data":filter_survey_details}, status=status.HTTP_200_OK)
        except Exception as e:
           return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
