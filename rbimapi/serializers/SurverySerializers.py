import uuid
from rest_framework import serializers
from rest_framework import exceptions
from rbim.models import SurveyMaster, Section, CensusStaticSections, CensusStaticCategory, Users
from rbim.models import (CensusCategory, SurveyEntry, CensusMember, CensusSections, Questions)
from rbimapi.serializers.CommonSerializers import JSONSerializerField
from rbimapi.serializers.NotificationHistorySerializers import NotificationHistorySerializer
import constants
import emailConstants
from django.utils import timezone
import staticContent
from django.db import transaction
from rbimapi.jobs.reportMainThread import call_survey_report_thread
class SurveyMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyMaster
        fields = '__all__'
        read_only_fields = [
            'id'
        ]
    def create(self,validated_data):
        obj_suvery_master = SurveyMaster.objects.filter(deleted_at__isnull=True).order_by('-position').first()
        if obj_suvery_master:
            validated_data['position'] = obj_suvery_master.position + 1
        return super().create(validated_data)
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
        read_only_fields = [
            'id'
        ]
    def create(self,validated_data):
        obj_section = Section.objects.filter(deleted_at__isnull=True).order_by('-position').first()
        if obj_section:
            validated_data['position'] = obj_section.position + 1
        return super().create(validated_data)
class SurveyEntrySerializer(serializers.ModelSerializer):
    next_section = serializers.CharField(allow_null=True, required=False)
    members = JSONSerializerField()
    def validate_survey_number(self, value):
        data = self.get_initial()
        if data['survey_type'] != 'ocr':
            if not value:
                raise exceptions.ParseError(constants.SURVEY_NUMBER_MANDATORY_ERROR_MSG)
            if SurveyEntry.objects.filter(survey_number__iexact=value).count():
                raise exceptions.ParseError(constants.SURVEY_NUMBER_EXISTS_ERROR_MSG)
        return value
    class Meta:
        model = SurveyEntry
        fields = '__all__'
        read_only_fields = [
            'id'
        ]
    def create(self,validated_data):
        return super().create(validated_data)
class SurveyMbLocalSerializer(serializers.ModelSerializer):
    mb_local = JSONSerializerField()
    class Meta:
        model = SurveyEntry
        fields = [
            "id",
            "mb_local"
        ]
    def update(self, instance, validated_data):
        return super().update(instance=SurveyEntry.objects.get(id=instance), validated_data=validated_data)        
class SurveyEntryUpdateSerializer(serializers.ModelSerializer):
    members = JSONSerializerField()
    class Meta:
        model = SurveyEntry
        fields = '__all__'
        read_only_fields = [
            'id'
        ]
    def update(self, instance, validated_data):
        return super().update(instance=SurveyEntry.objects.get(id=instance), validated_data=validated_data)
class CensusStaticCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusStaticCategory
        fields = '__all__'
        read_only_fields = [
            'id'
        ]
    def create(self,validated_data):
        return super().create(validated_data)
class CensusCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusCategory
        fields = '__all__'
        read_only_fields = [
            'id'
        ]
    def create(self,validated_data):
        return super().create(validated_data)
class CensusStaticSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusStaticSections
        fields = '__all__'
        read_only_fields = [
            'id'
        ]
    def create(self,validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance=CensusStaticSections.objects.get(id=instance), validated_data=validated_data)
class CensusSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusSections
        fields = '__all__'
        read_only_fields = [
            'id'
        ]
    def create(self,validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance=CensusSections.objects.get(id=instance), validated_data=validated_data)
class CensusMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusMember
        fields = '__all__'
        read_only_fields = [
            'id'
        ]
    def create(self,validated_data):
        return super().create(validated_data)
class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'
        read_only_fields = [
            'id'
        ]
    def create(self,validated_data):
        return super().create(validated_data)        
class SurveyQuestionVerificationSerializer(serializers.Serializer):
    next_section  = serializers.CharField(allow_null=True, required=False)
    inner_next_section  = serializers.CharField(allow_null=True, required=False)
    reviews = JSONSerializerField()
    def validate(self, data):
        next_section = data.get("next_section",None)
        inner_next_section = data.get("inner_next_section",None)
        reviews = data.get("reviews",None)
        for val in reviews:
            section_id = uuid.UUID(val.get("section_id"))
            question_id = uuid.UUID(val.get("question_id"))
            user_obj = Users.objects.filter(id=self.context.get('user_id')).first()
            survey_part = val.get("part")
            is_approved = val.get("is_approved", False)
            is_rejected = val.get("is_rejected", False)
            approved_date = val.get("approved_date", None)
            reject_reason = val.get("reject_reason", None)
            rejected_date = val.get("rejected_date", None)
            if survey_part == "house_hold_member_section":
                section_obj = CensusSections.objects.filter(id=section_id).filter(questions={"id":question_id}).first()
            else:
                section_obj = CensusStaticSections.objects.filter(id=section_id).filter(questions={"id":question_id}).first()
            survey_entry_id = section_obj.survey_entry_id
            survey_entry_obj = SurveyEntry.objects.filter(id=survey_entry_id).first()
            if user_obj.role == constants.USER_ROLES[1]: #Barangay
                if not survey_entry_obj.reviewed_by:
                    raise exceptions.ParseError(constants.SURVEY_REVIEW_ERROR_MSG)
            if section_obj and section_obj.questions:
                for question in section_obj.questions:
                    if question['id'] == question_id:
                        if user_obj.role == constants.USER_ROLES[1]: #Barangay
                            question['is_reviewed_by_barangay'] = True
                        else:
                            question['is_reviewed_by_barangay'] = False
                        if is_approved:
                            question['is_approved'] = is_approved
                            question['approved_date'] = approved_date
                            question['is_rejected'] = False
                            question['reject_reason'] = None
                            question['rejected_date'] = None
                        else:
                            question['is_approved'] = False
                            question['approved_date'] = None
                            question['is_rejected'] = is_rejected
                            question['reject_reason'] = reject_reason
                            question['rejected_date'] = rejected_date        
            section_obj.approved_count = sum(map(lambda i: i["is_approved"]==True, section_obj.questions))
            section_obj.rejected_count = sum(map(lambda i: i["is_rejected"]==True, section_obj.questions))
            if section_obj.rejected_count > 0:
                section_obj.is_recorrection = True
            section_obj.save()
        # Survey Entry Update
        survey_entry_obj = SurveyEntry.objects.filter(id=survey_entry_id).first()
        survey_entry_obj.next_section = next_section
        survey_entry_obj.inner_next_section = inner_next_section
        if user_obj.role == constants.USER_ROLES[1]: #Barangay
            survey_entry_obj.status = constants.SURVEY_STATUS[5] #survey_verification_started
            survey_entry_obj.survey_verification_started_on = timezone.now()
        elif user_obj.role == constants.USER_ROLES[2]: #Reviewer
            survey_entry_obj.status = constants.SURVEY_STATUS[1] #survey_review_started
            survey_entry_obj.survey_review_started_on = timezone.now()
        survey_entry_obj.save()
        return survey_entry_obj.status
class ReviewFinalSubmitSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    signature = JSONSerializerField(allow_null=True, required=False)
    survey_status  = serializers.CharField(allow_null=True, required=False)
    def validate(self, data):
        survey_entry_id = data.get("id",None)
        survey_status = data.get("survey_status",None)
        signature = data.get("signature",None)
        survey_entry_obj = SurveyEntry.objects.filter(id=survey_entry_id).first()
        user_obj = Users.objects.filter(id=self.context.get('user_id')).first()
        if not survey_entry_obj:
            raise exceptions.ParseError(constants.INVALID_SURVEY_ERROR_MSG)
        if user_obj.role == constants.USER_ROLES[1]: #Barangay
            if not survey_entry_obj.reviewed_by:
                raise exceptions.ParseError(constants.SURVEY_UNPROCESSABLE_ERROR_MSG)
        if survey_status == "review_pending":
            if user_obj.role == constants.USER_ROLES[1]: #Barangay
                survey_entry_obj.status = constants.SURVEY_STATUS[5] #survey_verification_started
                survey_entry_obj.survey_verification_started_on = timezone.now()
            elif user_obj.role == constants.USER_ROLES[2]: #Reviewer
                survey_entry_obj.status = constants.SURVEY_STATUS[1] #survey_review_started
                survey_entry_obj.survey_review_started_on = timezone.now()
        elif survey_status == "review_completed":
            total_qcount = []
            total_acount = []
            total_rcount = []
            total_qcount.append(1)
            if signature and (('is_approved' in signature and signature['is_approved']) and signature["is_approved"]==True):
                total_acount.append(1)
                survey_entry_obj.signature_recorrection_flag = False
            if signature and (('is_rejected' in signature and signature['is_rejected']) and signature["is_rejected"]==True):
                survey_entry_obj.signature_recorrection_flag = True
                total_rcount.append(1)
            census_static_category_arrobj = CensusStaticCategory.objects.filter(survey_entry=survey_entry_obj.id).all()
            if census_static_category_arrobj:
                for csc in census_static_category_arrobj:
                    census_static_section_arrobj = CensusStaticSections.objects.filter(census_static_category=csc.id).all()
                    for css in census_static_section_arrobj:
                        if css.is_enable:
                            if css.qcount:
                                total_qcount.append(css.qcount)
                            if css.approved_count:
                                total_acount.append(css.approved_count)
                            if css.rejected_count:
                                total_rcount.append(css.rejected_count)
            census_category_arrobj = CensusCategory.objects.filter(survey_entry=survey_entry_obj.id).all()
            if census_category_arrobj:
                for dy_csc in census_category_arrobj:
                    census_section_arrobj = CensusSections.objects.filter(census_category=dy_csc.id).all()
                    for dy_css in census_section_arrobj:
                        if dy_css.is_enable:
                            if dy_css.qcount:
                                total_qcount.append(dy_css.qcount)
                            if dy_css.approved_count:
                                total_acount.append(dy_css.approved_count)
                            if dy_css.rejected_count:
                                total_rcount.append(dy_css.rejected_count)
            survey_entry_obj.total_qcount = sum(total_qcount)
            survey_entry_obj.total_acount = sum(total_acount)
            survey_entry_obj.total_rcount = sum(total_rcount)
            survey_entry_obj.signature = signature
            if user_obj.role == constants.USER_ROLES[1]: #Barangay
                survey_entry_obj.verfied_by = user_obj
            elif user_obj.role == constants.USER_ROLES[2]: #Reviewer
                survey_entry_obj.reviewed_by = user_obj
            if survey_entry_obj.total_rcount == 0:
                if user_obj.role == constants.USER_ROLES[1]: #Barangay
                    survey_entry_obj.status = constants.SURVEY_STATUS[6] #survey_completed
                    survey_entry_obj.survey_completed_on = timezone.now()
                    if survey_entry_obj.is_barangay_rejected:
                        survey_entry_obj.is_barangay_rejected = False
                        survey_entry_obj.is_barangay_enable_rejected_flag = False
                    # Email Notification 1- start
                    nt_message = emailConstants.NT_MESSAGE_BO_COMPLETE_SURVEY.format(user_obj.first_name, survey_entry_obj.survey_number)
                    email_message = emailConstants.EMAIL_MESSAGE_BO_COMPLETE_SURVEY.format(user_obj.first_name, survey_entry_obj.survey_number)
                    title = emailConstants.SUBJECT_BO_COMPLETE_SURVEY
                    bo_complete_sn_param = staticContent.notification_param(sender=user_obj.id, receiver=user_obj.id, title=title, nt_message=nt_message, email_message=email_message, email=user_obj.email)
                    nh_serializer = NotificationHistorySerializer(data=bo_complete_sn_param) 
                    nh_serializer.is_valid(raise_exception = True)
                    nh_serializer.save()
                    # Email Notification 2- start
                    receiver_obj = Users.objects.filter(id=survey_entry_obj.data_reviewer_id).first()
                    nt_message = emailConstants.NT_MESSAGE_BO_APPROVED_SURVEY.format(receiver_obj.first_name, survey_entry_obj.survey_number)
                    email_message = emailConstants.EMAIL_MESSAGE_BO_APPROVED_SURVEY.format(receiver_obj.first_name, survey_entry_obj.survey_number)
                    title = emailConstants.SUBJECT_BO_APPROVED_SURVEY
                    bo_approved_sn_param = staticContent.notification_param(sender=user_obj.id, receiver=receiver_obj.id, title=title, nt_message=nt_message, email_message=email_message, email=receiver_obj.email)
                    nh_serializer = NotificationHistorySerializer(data=bo_approved_sn_param) 
                    nh_serializer.is_valid(raise_exception = True)
                    nh_serializer.save()
                    try:
                        with transaction.atomic():
                            call_survey_report_thread(survey_entry_id=survey_entry_obj.id)
                    except:
                        pass
                elif user_obj.role == constants.USER_ROLES[2]: #Reviewer
                    survey_entry_obj.status = constants.SURVEY_STATUS[4] #pending_for_approval
                    survey_entry_obj.pending_for_approval_on = timezone.now()
                    survey_entry_obj.survey_review_submitted_on = timezone.now()
                    if survey_entry_obj.is_reviewer_rejected:
                        survey_entry_obj.is_reviewer_rejected = False
                        survey_entry_obj.is_reviewer_enable_rejected_flag = False
                    survey_entry_obj.next_section = None
                    survey_entry_obj.inner_next_section = None
                    # Email Notification 1- start
                    nt_message = emailConstants.NT_MESSAGE_DR_COMPLETE_SURVEY.format(user_obj.first_name, survey_entry_obj.survey_number)
                    email_message = emailConstants.EMAIL_MESSAGE_DR_COMPLETE_SURVEY.format(user_obj.first_name, survey_entry_obj.survey_number)
                    title = emailConstants.SUBJECT_DR_COMPLETE_SURVEY
                    dr_complete_sn_param = staticContent.notification_param(sender=user_obj.id, receiver=user_obj.id, title=title, nt_message=nt_message, email_message=email_message, email=user_obj.email)
                    nh_serializer = NotificationHistorySerializer(data=dr_complete_sn_param) 
                    nh_serializer.is_valid(raise_exception = True)
                    nh_serializer.save()
                    # Email Notification 2 - start
                    receiver_obj = Users.objects.filter(id=survey_entry_obj.data_collector_id).first()
                    nt_message = emailConstants.NT_MESSAGE_DR_APPROVED_SURVEY.format(receiver_obj.first_name, survey_entry_obj.survey_number)
                    email_message = emailConstants.EMAIL_MESSAGE_DR_APPROVED_SURVEY.format(receiver_obj.first_name, survey_entry_obj.survey_number)
                    title = emailConstants.SUBJECT_DR_APPROVED_SURVEY
                    dr_approved_sn_param = staticContent.notification_param(sender=user_obj.id, receiver=receiver_obj.id, title=title, nt_message=nt_message, email_message=email_message, email=receiver_obj.email)
                    nh_serializer = NotificationHistorySerializer(data=dr_approved_sn_param) 
                    nh_serializer.is_valid(raise_exception = True)
                    nh_serializer.save()
            else:
                if user_obj.role == constants.USER_ROLES[1]: #Barangay
                    survey_entry_obj.status = constants.SURVEY_STATUS[2] #survey_rejected
                    survey_entry_obj.survey_rejected_on = timezone.now()
                    survey_entry_obj.survey_recorrection_on = timezone.now()
                    survey_entry_obj.rejected_by = "barangay"
                    survey_entry_obj.is_barangay_rejected = True
                    survey_entry_obj.is_barangay_enable_rejected_flag = True
                    survey_entry_obj.next_section = None
                    survey_entry_obj.inner_next_section = None
                    # Email Notification - start
                    receiver_obj = Users.objects.filter(id=survey_entry_obj.data_reviewer_id).first()
                    nt_message = emailConstants.NT_MESSAGE_BO_REJECTED_SURVEY.format(receiver_obj.first_name, survey_entry_obj.survey_number)
                    email_message = emailConstants.EMAIL_MESSAGE_BO_REJECTED_SURVEY.format(receiver_obj.first_name, survey_entry_obj.survey_number)
                    title = emailConstants.SUBJECT_BO_REJECTED_SURVEY
                    survey_notification_param = staticContent.notification_param(sender=user_obj.id, receiver=receiver_obj.id, title=title, nt_message=nt_message, email_message=email_message, email=receiver_obj.email)
                elif user_obj.role == constants.USER_ROLES[2]: #Reviewer
                    survey_entry_obj.status = constants.SURVEY_STATUS[7] #survey_recorrection
                    survey_entry_obj.survey_recorrection_on = timezone.now()
                    survey_entry_obj.rejected_by = "reviewer"
                    survey_entry_obj.is_reviewer_rejected = True
                    survey_entry_obj.is_reviewer_enable_rejected_flag = True
                    survey_entry_obj.next_section = None
                    survey_entry_obj.inner_next_section = None
                    # Email Notification - start
                    receiver_obj = Users.objects.filter(id=survey_entry_obj.data_collector_id).first()
                    nt_message = emailConstants.NT_MESSAGE_DR_REJECTED_SURVEY.format(receiver_obj.first_name, survey_entry_obj.survey_number)
                    email_message = emailConstants.EMAIL_MESSAGE_DR_REJECTED_SURVEY.format(receiver_obj.first_name, survey_entry_obj.survey_number)
                    title = emailConstants.SUBJECT_DR_REJECTED_SURVEY
                    survey_notification_param = staticContent.notification_param(sender=user_obj.id, receiver=receiver_obj.id, title=title, nt_message=nt_message, email_message=email_message, email=receiver_obj.email)
                nh_serializer = NotificationHistorySerializer(data=survey_notification_param) 
                nh_serializer.is_valid(raise_exception = True)
                nh_serializer.save()
        else:
            raise exceptions.ParseError(constants.UNPROCESSABLE_SURVEY_ERROR_MSG)
        survey_entry_obj.enable_recorrection_flag = False
        if survey_entry_obj.is_reviewer_rejected or survey_entry_obj.is_barangay_rejected:
            survey_entry_obj.enable_recorrection_flag = True
        survey_entry_obj.save()
        return data
class OcrVerificationSerializer(serializers.Serializer):
    next_section  = serializers.CharField(allow_null=True, required=False)
    inner_next_section  = serializers.CharField(allow_null=True, required=False)
    personindex  = serializers.CharField(allow_null=True, required=False)
    pageindex  = serializers.CharField(allow_null=True, required=False)
    reviews = JSONSerializerField()
    def validate(self,data):
        next_section = data.get("next_section",None)
        inner_next_section = data.get("inner_next_section",None)
        personindex = data.get("personindex",None)
        pageindex = data.get("pageindex",None)
        reviews = data.get("reviews",None)
        for val in reviews:
            section_id = uuid.UUID(val.get("section_id"))
            question_id = uuid.UUID(val.get("question_id"))
            user_obj = Users.objects.filter(id=self.context.get('user_id')).first()
            survey_part = val.get("part")
            is_approved = val.get("is_approved", False)
            is_rejected = val.get("is_rejected", False)
            approved_date = val.get("approved_date", None)
            reject_reason = val.get("reject_reason", None)
            rejected_date = val.get("rejected_date", None)
            if survey_part == "house_hold_member_section":
                section_obj = CensusSections.objects.filter(id=section_id).filter(questions={"id":question_id}).first()
            else:
                section_obj = CensusStaticSections.objects.filter(id=section_id).filter(questions={"id":question_id}).first()
            survey_entry_id = section_obj.survey_entry_id
            survey_entry_obj = SurveyEntry.objects.filter(id=survey_entry_id).first()
            if user_obj.role == constants.USER_ROLES[1]: #Barangay
                if not survey_entry_obj.reviewed_by:
                    raise exceptions.ParseError(constants.SURVEY_REVIEW_ERROR_MSG)
            if section_obj and section_obj.questions:
                for question in section_obj.questions:
                    if question['id'] == question_id:
                        question['answers'] = val.get("answers", None)
                        if user_obj.role == constants.USER_ROLES[1]: #Barangay
                            question['is_reviewed_by_barangay'] = True
                        else:
                            question['is_reviewed_by_barangay'] = False
                        if is_approved:
                            question['is_approved'] = is_approved
                            question['approved_date'] = approved_date
                            question['is_rejected'] = False
                            question['reject_reason'] = None
                            question['rejected_date'] = None
                        else:
                            question['is_approved'] = False
                            question['approved_date'] = None
                            question['is_rejected'] = is_rejected
                            question['reject_reason'] = reject_reason
                            question['rejected_date'] = rejected_date        
            section_obj.approved_count = sum(map(lambda i: i["is_approved"]==True, section_obj.questions))
            section_obj.rejected_count = sum(map(lambda i: i["is_rejected"]==True, section_obj.questions))
            if section_obj.rejected_count > 0:
                section_obj.is_recorrection = True
            section_obj.save()
        # Survey Entry Update
        survey_entry_obj = SurveyEntry.objects.filter(id=survey_entry_id).first()
        survey_entry_obj.next_section = next_section
        survey_entry_obj.inner_next_section = inner_next_section
        survey_entry_obj.personindex = personindex
        survey_entry_obj.pageindex = pageindex
        if user_obj.role == constants.USER_ROLES[1]: #Barangay
            survey_entry_obj.status = constants.SURVEY_STATUS[5] #survey_verification_started
            survey_entry_obj.survey_verification_started_on = timezone.now()
        elif user_obj.role == constants.USER_ROLES[2]: #Reviewer
            survey_entry_obj.status = constants.SURVEY_STATUS[1] #survey_review_started
            survey_entry_obj.survey_review_started_on = timezone.now()
        survey_entry_obj.save()
        return survey_entry_obj.status
class OcrFinalSubmitSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    signature = JSONSerializerField(allow_null=True, required=False)
    survey_status  = serializers.CharField(allow_null=True, required=False)
    def validate(self, data):
        survey_entry_id = data.get("id",None)
        survey_status = data.get("survey_status",None)
        signature = data.get("signature",None)
        survey_entry_obj = SurveyEntry.objects.filter(id=survey_entry_id).first()
        user_obj = Users.objects.filter(id=self.context.get('user_id')).first()
        if not survey_entry_obj:
            raise exceptions.ParseError(constants.INVALID_SURVEY_ERROR_MSG)
        if user_obj.role == constants.USER_ROLES[1]: #Barangay
            if not survey_entry_obj.reviewed_by:
                raise exceptions.ParseError(constants.SURVEY_UNPROCESSABLE_ERROR_MSG)
        if survey_status == "review_pending":
            if user_obj.role == constants.USER_ROLES[1]: #Barangay
                survey_entry_obj.status = constants.SURVEY_STATUS[5] #survey_verification_started
                survey_entry_obj.survey_verification_started_on = timezone.now()
            elif user_obj.role == constants.USER_ROLES[2]: #Reviewer
                survey_entry_obj.status = constants.SURVEY_STATUS[1] #survey_review_started
                survey_entry_obj.survey_review_started_on = timezone.now()
        elif survey_status == "review_completed":
            total_qcount = []
            total_acount = []
            total_rcount = []
            total_qcount.append(1)
            if signature and (('is_approved' in signature and signature['is_approved']) and signature["is_approved"]==True):
                total_acount.append(1)
                survey_entry_obj.signature_recorrection_flag = False
            if signature and (('is_rejected' in signature and signature['is_rejected']) and signature["is_rejected"]==True):
                survey_entry_obj.signature_recorrection_flag = True
                total_rcount.append(1)
            census_static_category_arrobj = CensusStaticCategory.objects.filter(survey_entry=survey_entry_obj.id).all()
            if census_static_category_arrobj:
                for csc in census_static_category_arrobj:
                    census_static_section_arrobj = CensusStaticSections.objects.filter(census_static_category=csc.id).all()
                    for css in census_static_section_arrobj:
                        if css.is_enable:
                            if css.qcount:
                                total_qcount.append(css.qcount)
                            if css.approved_count:
                                total_acount.append(css.approved_count)
                            if css.rejected_count:
                                total_rcount.append(css.rejected_count)
            census_category_arrobj = CensusCategory.objects.filter(survey_entry=survey_entry_obj.id).all()
            if census_category_arrobj:
                for dy_csc in census_category_arrobj:
                    census_section_arrobj = CensusSections.objects.filter(census_category=dy_csc.id).all()
                    for dy_css in census_section_arrobj:
                        if dy_css.is_enable:
                            if dy_css.qcount:
                                total_qcount.append(dy_css.qcount)
                            if dy_css.approved_count:
                                total_acount.append(dy_css.approved_count)
                            if dy_css.rejected_count:
                                total_rcount.append(dy_css.rejected_count)
            survey_entry_obj.total_qcount = sum(total_qcount)
            survey_entry_obj.total_acount = sum(total_acount)
            survey_entry_obj.total_rcount = sum(total_rcount)
            survey_entry_obj.signature = signature
            if user_obj.role == constants.USER_ROLES[1]: #Barangay
                survey_entry_obj.verfied_by = user_obj
            elif user_obj.role == constants.USER_ROLES[2]: #Reviewer
                survey_entry_obj.reviewed_by = user_obj
            if survey_entry_obj.total_rcount == 0:
                if user_obj.role == constants.USER_ROLES[1]: #Barangay
                    survey_entry_obj.status = constants.SURVEY_STATUS[6] #survey_completed
                    survey_entry_obj.survey_completed_on = timezone.now()
                    if survey_entry_obj.is_barangay_rejected:
                        survey_entry_obj.is_barangay_rejected = False
                        survey_entry_obj.is_barangay_enable_rejected_flag = False
                    # Email Notification 1- start
                    nt_message = emailConstants.NT_MESSAGE_BO_COMPLETE_SURVEY.format(user_obj.first_name,
                                                                                     survey_entry_obj.survey_number)
                    email_message = emailConstants.EMAIL_MESSAGE_BO_COMPLETE_SURVEY.format(user_obj.first_name,
                                                                                           survey_entry_obj.survey_number)
                    title = emailConstants.SUBJECT_BO_COMPLETE_SURVEY
                    bo_complete_sn_param = staticContent.notification_param(sender=user_obj.id,
                                                                            receiver=user_obj.id, title=title,
                                                                            nt_message=nt_message,
                                                                            email_message=email_message,
                                                                            email=user_obj.email)
                    nh_serializer = NotificationHistorySerializer(data=bo_complete_sn_param)
                    nh_serializer.is_valid(raise_exception=True)
                    nh_serializer.save()
                    # Email Notification 2- start
                    receiver_obj = Users.objects.filter(id=survey_entry_obj.data_reviewer_id).first()
                    nt_message = emailConstants.NT_MESSAGE_BO_APPROVED_SURVEY.format(receiver_obj.first_name,
                                                                                     survey_entry_obj.survey_number)
                    email_message = emailConstants.EMAIL_MESSAGE_BO_APPROVED_SURVEY.format(receiver_obj.first_name,
                                                                                           survey_entry_obj.survey_number)
                    title = emailConstants.SUBJECT_BO_APPROVED_SURVEY
                    bo_approved_sn_param = staticContent.notification_param(sender=user_obj.id,
                                                                            receiver=receiver_obj.id, title=title,
                                                                            nt_message=nt_message,
                                                                            email_message=email_message,
                                                                            email=receiver_obj.email)
                    nh_serializer = NotificationHistorySerializer(data=bo_approved_sn_param)
                    nh_serializer.is_valid(raise_exception=True)
                    nh_serializer.save()
                elif user_obj.role == constants.USER_ROLES[2]: #Reviewer
                    survey_entry_obj.status = constants.SURVEY_STATUS[4] #pending_for_approval
                    survey_entry_obj.pending_for_approval_on = timezone.now()
                    survey_entry_obj.survey_review_submitted_on = timezone.now()
                    if survey_entry_obj.is_reviewer_rejected:
                        survey_entry_obj.is_reviewer_rejected = False
                        survey_entry_obj.is_reviewer_enable_rejected_flag = False
                    survey_entry_obj.next_section = None
                    survey_entry_obj.inner_next_section = None
                    # Email Notification 1- start
                    nt_message = emailConstants.NT_MESSAGE_DR_COMPLETE_SURVEY.format(user_obj.first_name,
                                                                                     survey_entry_obj.survey_number)
                    email_message = emailConstants.EMAIL_MESSAGE_DR_COMPLETE_SURVEY.format(user_obj.first_name,
                                                                                           survey_entry_obj.survey_number)
                    title = emailConstants.SUBJECT_DR_COMPLETE_SURVEY
                    dr_complete_sn_param = staticContent.notification_param(sender=user_obj.id, receiver=user_obj.id,
                                                                            title=title, nt_message=nt_message,
                                                                            email_message=email_message,
                                                                            email=user_obj.email)
                    nh_serializer = NotificationHistorySerializer(data=dr_complete_sn_param)
                    nh_serializer.is_valid(raise_exception=True)
                    nh_serializer.save()
            else:
                if user_obj.role == constants.USER_ROLES[1]: #Barangay
                    survey_entry_obj.status = constants.SURVEY_STATUS[2] #survey_rejected
                    survey_entry_obj.survey_rejected_on = timezone.now()
                    survey_entry_obj.survey_recorrection_on = timezone.now()
                    survey_entry_obj.rejected_by = "barangay"
                    survey_entry_obj.is_barangay_rejected = True
                    survey_entry_obj.is_barangay_enable_rejected_flag = True
                    survey_entry_obj.next_section = None
                    survey_entry_obj.inner_next_section = None
                    # Email Notification - start
                    receiver_obj = Users.objects.filter(id=survey_entry_obj.data_reviewer_id).first()
                    nt_message = emailConstants.NT_MESSAGE_BO_REJECTED_SURVEY_OCR.format(receiver_obj.first_name,
                                                                                     survey_entry_obj.survey_number)
                    email_message = emailConstants.EMAIL_MESSAGE_BO_REJECTED_SURVEY_OCR.format(receiver_obj.first_name,
                                                                                           survey_entry_obj.survey_number)
                    title = emailConstants.SUBJECT_BO_REJECTED_SURVEY
                    survey_notification_param = staticContent.notification_param(sender=user_obj.id,
                                                                                 receiver=receiver_obj.id, title=title,
                                                                                 nt_message=nt_message,
                                                                                 email_message=email_message,
                                                                                 email=receiver_obj.email)
                    nh_serializer = NotificationHistorySerializer(data=survey_notification_param)
                    nh_serializer.is_valid(raise_exception=True)
                    nh_serializer.save()
                elif user_obj.role == constants.USER_ROLES[2]: #Reviewer
                    survey_entry_obj.status = constants.SURVEY_STATUS[4] #pending_for_approval
                    survey_entry_obj.pending_for_approval_on = timezone.now()
                    survey_entry_obj.is_reviewer_rejected = True
                    survey_entry_obj.is_reviewer_enable_rejected_flag = True
                    survey_entry_obj.rejected_by = "reviewer"
                    survey_entry_obj.next_section = None
                    survey_entry_obj.inner_next_section = None
        else:
            raise exceptions.ParseError(constants.UNPROCESSABLE_SURVEY_ERROR_MSG)   
        survey_entry_obj.enable_recorrection_flag = False
        if survey_entry_obj.is_reviewer_rejected or survey_entry_obj.is_barangay_rejected:
            survey_entry_obj.enable_recorrection_flag = True
        survey_entry_obj.save() 
        return data