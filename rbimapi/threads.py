import threading
from rbimapi.serializers.SurverySerializers import CensusStaticCategorySerializer, CensusCategorySerializer, CensusStaticSectionSerializer, CensusMemberSerializer
from rbimapi.serializers.SurverySerializers import CensusSectionSerializer
from rbimapi.serializers.NotificationHistorySerializers import NotificationHistorySerializer
import emailConstants
import staticContent

class SurveyEntryThread(threading.Thread):
    def __init__(self, survey_entry_id, request, user_obj):
        threading.Thread.__init__(self)
        self.survey_entry_id = survey_entry_id
        self.request = request
        self.user_obj = user_obj

    def comman_question_and_answer_create(self, survey_entry_id, survey_data, part):
        for cat_val in survey_data:
            cat_val["survey_entry"] = survey_entry_id
            cat_val["part"] = part
            cat_serializers = CensusStaticCategorySerializer(data = cat_val)
            if cat_serializers.is_valid(raise_exception = True):
                cat_serializers.save()
            for section_val in cat_val['section']:
                section_val['survey_entry'] = survey_entry_id
                section_val['census_static_category'] = cat_serializers.data.get('id')
                cs_section_serializers = CensusStaticSectionSerializer(data = section_val)
                if cs_section_serializers.is_valid(raise_exception = True):
                    cs_section_serializers.save()

    def member_question_and_answer_create(self, survey_entry_id, hh_meber, part):
        for member_values in hh_meber:
            member_values['survey_entry'] = survey_entry_id
            member_serializers = CensusMemberSerializer(data = member_values)
            if member_serializers.is_valid(raise_exception = True):
                member_serializers.save()
                for page_val in member_values['category']:
                    for cat_mem_val in page_val['page']:
                        cat_mem_val["survey_entry"] = survey_entry_id
                        cat_mem_val["census_member"] = member_serializers.data.get('id')
                        cat_mem_val["part"] = part
                        cat_serializers = CensusCategorySerializer(data = cat_mem_val)
                        if cat_serializers.is_valid(raise_exception = True):
                            cat_serializers.save()
                        for section_val in cat_mem_val['section']:
                            section_val['survey_entry'] = survey_entry_id
                            section_val['census_member'] = member_serializers.data.get('id')
                            section_val['census_category'] = cat_serializers.data.get('id')
                            cs_serializers = CensusSectionSerializer(data = section_val)
                            if cs_serializers.is_valid(raise_exception = True):
                                cs_serializers.save()

    def run(self):
        if self.request.data.get("initial_section"):
            initial_section_val = []
            initial_section_val.append(self.request.data.get("initial_section"))
            self.comman_question_and_answer_create(self.survey_entry_id, initial_section_val, 'initial_section')
        if self.request.data.get("interview_section"):
            self.comman_question_and_answer_create(self.survey_entry_id, self.request.data.get("interview_section"), 'interview_section')   
        if self.request.data.get("house_hold_member_section"):
            self.member_question_and_answer_create(self.survey_entry_id, self.request.data.get("house_hold_member_section"), 'house_hold_member_section')      
        if self.request.data.get("final_section"):
            self.comman_question_and_answer_create(self.survey_entry_id, self.request.data.get("final_section"), 'final_section')
            
        nt_message = emailConstants.NT_MESSAGE_DC_COMPLETE_SURVEY.format(self.user_obj.first_name, self.request.data.get("survey_number", None))
        email_message = emailConstants.EMAIL_MESSAGE_DC_COMPLETE_SURVEY.format(self.user_obj.first_name, self.request.data.get("survey_number", None))
        title = emailConstants.SUBJECT_DC_COMPLETE_SURVEY
        dc_survey_completed_param = staticContent.notification_param(sender=self.user_obj.id, receiver=self.user_obj.id, title=title, nt_message=nt_message, email_message=email_message, email=self.user_obj.email)
        nh_serializer = NotificationHistorySerializer(data=dc_survey_completed_param)
        nh_serializer.is_valid(raise_exception = True)
        nh_serializer.save()