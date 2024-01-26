from rbimapi.mongoaggregate.survey import mdb_pending_survey_entry
from rbimapi.serializers.NotificationHistorySerializers import NotificationHistorySerializer
from rbimapi.CustomEmails import DoThreadManager
from rbim.models import Users
import emailConstants
import staticContent
def pending_survey_notification():
    try:
        dyparam = {}
        dyparam['match'] = {
            'deleted_at': None,
            'status':{'$in':['survey_assigned','pending_for_approval']}
        }
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
                serializer = NotificationHistorySerializer(data=pending_survey_param) 
                serializer.is_valid(raise_exception = True)
                serializer.save()
    except Exception as e:
        return None
    return None