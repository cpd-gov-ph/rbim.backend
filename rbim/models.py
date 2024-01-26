import uuid
import django.utils
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models, transaction
from djongo.models.fields import DjongoManager, ArrayField, MongoField, EmbeddedField
from django.dispatch import receiver
import constants
import emailConstants
from rbimapi.CustomEmails import ThreadManager
import staticContent

isMigrate = False 
#Token:
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

def md_email_trigger_jobs(title, email, html_content):
    message = None
    template=emailConstants.EMAIL_TEMPLATE
    param = staticContent.email_trigger_param(title=title, email=email, html_content=html_content, template=template, message=message)
    ThreadManager.email_trigger_jobs(param)
    return None

def md_push_notification_trigger_jobs(title, fcm_token, html_content):
    param = staticContent.push_notification_trigger_param(title=title, fcm_token=fcm_token, html_content=html_content)
    ThreadManager.push_notification_trigger_jobs(param)
    return None
class UserManager(BaseUserManager):
    @transaction.atomic
    def create_user(self, data, is_active=False, role=None):
        user = Users(**data)
        user.set_password(user.password)
        user.is_active = is_active
        user.role = role # 0-superadmin ,1-barangay,2-data reviewer,3-data collector
        user.save()
        return user   
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null = True)
    class Meta:
        abstract = True

class SurveyMaster(BaseModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=500, blank=True, null=True)
    part = models.CharField(max_length=100, default="A") # dynamic or static
    position = models.IntegerField(default=1)
    page = models.IntegerField(default=1)
    objects = models.Manager() # The default manager.
    mongoObjects = DjongoManager()

class Answers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dtype = models.CharField(max_length=250)
    placeholder = models.CharField(max_length=255,null=True,blank=True)
    position = models.IntegerField(default=1)
    answer_value = MongoField(null=True)
    is_error = models.BooleanField(default=False)
    error_message = models.CharField(max_length=255,null=True,blank=True)
    keyboard_type = models.CharField(max_length=255,null=True,blank=True)
    limitation =  models.IntegerField(null=True,blank=True)
    show_dropdown_modal = models.BooleanField(null=True,blank=True,default=False)
    show_time_picker = models.BooleanField(null=True,blank=True,default=False)
    show_multi_dropdown_modal = models.BooleanField(null=True,blank=True,default=False)
    show_picker = models.BooleanField(null=True,blank=True,default=False)
    ranking =  models.IntegerField(null=True,blank=True)
    options = MongoField()
    class Meta:
        abstract = isMigrate

class Questions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    survey_entry_id = models.UUIDField(null = True)
    category_id = models.UUIDField(null = True)
    section_id = models.UUIDField(null = True)
    question_id = models.UUIDField(null = True)
    qno = models.CharField(max_length=100,null=True,blank=True)
    part = models.CharField(max_length=255,null=True,blank=True)
    title = models.CharField(max_length=500)
    is_required = models.BooleanField(default=True)
    answers = ArrayField(model_container=Answers)
    position = models.IntegerField(default=1)
    is_read_only = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    is_reviewed_by_barangay = models.BooleanField(default=False)
    others_status = models.BooleanField(null=True,blank=True,default=False)
    qn_ranking = models.IntegerField(null=True,blank=True)
    is_qn_enable = models.BooleanField(default=True)
    reject_reason = models.CharField(max_length=255,null=True,blank=True)
    approved_date = models.DateTimeField(default=None)
    rejected_date = models.DateTimeField(default=None)
    created_at = models.DateTimeField(default=django.utils.timezone.now)
    updated_at = models.DateTimeField(default=django.utils.timezone.now)
    is_deleted = models.IntegerField(default=0)
    class Meta:
        abstract = isMigrate

class Section(BaseModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    survey_master =  models.ForeignKey(SurveyMaster, related_name='survey_master',on_delete=models.CASCADE)
    position = models.IntegerField(default=1)
    section_name = models.CharField(max_length=400,null=True,blank=True)
    is_enable = models.BooleanField(default=True)
    is_subheader = models.BooleanField(default=True)
    qcount = models.IntegerField(default=0)
    anscount = models.IntegerField(default=0)
    questions = ArrayField(model_container=Questions, null=True)
    objects = models.Manager() # The default manager.
    mongoObjects = DjongoManager()

class City(BaseModel,models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=255,null=True,blank=True)
    code = models.CharField(max_length=255,null=True,blank=True)

class Municipality(BaseModel,models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    city = models.ForeignKey(City, related_name='city',on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=255,null=True,blank=True)
    code = models.CharField(max_length=255,null=True,blank=True) 

class Location(BaseModel,models.Model):
    id =  models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=255,null=True,blank=True)
    code = models.CharField(max_length=255,null=True,blank=True)
    municipality = models.ForeignKey(Municipality, related_name='municipality',on_delete=models.CASCADE,default=None)
    objects = models.Manager() # The default manager.
    mongoObjects = DjongoManager()

class Users(BaseModel,AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    role = models.CharField(max_length=255,null=True,blank=True)
    barangay_id = models.UUIDField(null = True)
    data_reviewer_id = models.UUIDField(null = True)
    city = models.ForeignKey(City,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    location = models.ForeignKey(Location,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    municipality = models.ForeignKey(Municipality,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    first_name = models.CharField(max_length=255,null=True,blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    password = models.CharField(max_length=255,null=True,blank=True)
    is_active = models.BooleanField(default = True)
    last_login = models.DateField(auto_now_add=True)
    reset_code = models.IntegerField(null=True,blank=True)
    is_reset_mail_send = models.BooleanField(default = False)
    is_agree = models.IntegerField(default = 0)
    fcm_token = models.CharField(max_length= 255,null=True,blank=True)
    created_by = models.UUIDField(null = True)
    objects = UserManager()
    mongoObjects = DjongoManager()
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.id
    
    def user_forgot_password_email(self, email, code):
        message = None
        template= "forgot_password.html"
        param = staticContent.forgot_password_param(email=email, code=code, template=template, message=message)
        ThreadManager.email_trigger_jobs(param)
        return None
    
    def welcome_email_for_onboard(self, title, email, html_content):
        md_email_trigger_jobs(title=title, email=email, html_content=html_content)
        return None
    
    def update_profile_email_trigger(self, title, email, html_content):
        md_email_trigger_jobs(title=title, email=email, html_content=html_content)
        return None
    
    def dashboard_count_auto_update(self):
        user_obj = Users.objects.filter(role='superadmin').first()
        if user_obj:
            profile_obj = Profile.objects.filter(user_id = user_obj.id).first()
            profile_obj.dashboard_count = {
                'barangay': Users.objects.filter(role=constants.USER_ROLES[1]).count(),
                'data_reviewer' : Users.objects.filter(role=constants.USER_ROLES[2]).count(),
                'data_collector' : Users.objects.filter(role=constants.USER_ROLES[3]).count(),
                'survey': SurveyEntry.objects.count()
            }
            profile_obj.save()
        return None

    class Meta:
        ordering = ['-created_by']
class Profile(BaseModel,models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    user = models.OneToOneField(Users,related_name = "users",on_delete=models.CASCADE)
    official_number = models.CharField(max_length=255,null=True,blank=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=255,null=True,blank=True)
    phone_no = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    dashboard_count = MongoField(null=True) 
    created_by = models.UUIDField(null = True)

class Options(BaseModel,models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    meta_key = models.CharField(max_length=255,null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    meta_value = models.TextField(null=True,blank=True) 

class Tasks(BaseModel,models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    data_collector = models.ForeignKey(Users,on_delete=models.CASCADE)
    task_no = models.IntegerField(default = 0)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    created_by = models.UUIDField(null = True)
    objects = models.Manager() # The default manager.
    mongoObjects = DjongoManager()

class SurveyEntry(BaseModel,models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    data_collector = models.ForeignKey(Users,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name = "data_collector"
    )
    data_reviewer = models.ForeignKey(Users,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name = "data_reviewer"
        
    )
    barangay = models.ForeignKey(Users,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name = "barangay"
    )
    reviewed_by =  models.ForeignKey(Users,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name = "reviewed_by"
    )
    verfied_by =  models.ForeignKey(Users,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name = "verfied_by"
    )
    survey_number = models.CharField(max_length=255,null=True,blank=True)
    status = models.CharField(max_length=255)
    survey_type = models.CharField(max_length=255,default = "regular")
    household_member_count = models.IntegerField(default = 0)
    survey_assigned_on = models.DateTimeField(null=True)
    survey_review_started_on = models.DateTimeField(null=True)
    survey_review_submitted_on = models.DateTimeField(null=True)
    survey_rejected_on = models.DateTimeField(null=True)
    survey_recorrection_on = models.DateTimeField(null=True)
    pending_for_approval_on = models.DateTimeField(null=True)
    survey_verification_started_on = models.DateTimeField(null=True)
    survey_completed_on = models.DateTimeField(null=True)
    data_collector_signature = models.TextField(null=True,blank=True)
    data_reviewer_signature = models.TextField(null=True,blank=True)
    notes = models.TextField(max_length=500,null=True,blank=True)
    next_section = MongoField(null=True) 
    inner_next_section = MongoField(null=True) 
    mobile_next_section = MongoField(null=True)
    members = MongoField(null=True)
    mb_local = MongoField(null=True)
    signature = MongoField(null=True)
    signature_recorrection_flag = models.BooleanField(default=False)
    total_qcount = models.IntegerField(default = 0)
    total_acount = models.IntegerField(default = 0)
    total_rcount = models.IntegerField(default = 0)
    enable_recorrection_flag = models.BooleanField(default=False)
    is_recorrection_members = models.BooleanField(default=False)
    rejected_by = models.CharField(max_length=255,null=True,blank=True)
    is_barangay_rejected = models.BooleanField(default=False)
    is_reviewer_rejected = models.BooleanField(default=False)
    is_reviewer_enable_rejected_flag = models.BooleanField(default=False)
    is_barangay_enable_rejected_flag = models.BooleanField(default=False)
    is_open_ndividual_view = models.BooleanField(default=True)
    ocr_status = models.CharField(max_length=50, default=constants.OCR_STATUS[0])
    personindex = MongoField(null=True)
    pageindex = MongoField(null=True)
    objects = models.Manager() # The default manager.
    mongoObjects = DjongoManager()

class CensusStaticCategory(BaseModel,models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    survey_entry = models.ForeignKey(SurveyEntry,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    category_name = models.CharField(max_length=255,null=True,blank=True)
    part = models.CharField(max_length=100, null=True,blank=True) # dynamic or static
    position = models.IntegerField(default=1)
    page = models.IntegerField(default=1)
    objects = models.Manager() # The default manager.
    mongoObjects = DjongoManager()

class CensusStaticSections(BaseModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    survey_entry = models.ForeignKey(SurveyEntry,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    census_static_category = models.ForeignKey(CensusStaticCategory,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    section_name = models.CharField(max_length=255,null=True,blank=True)
    is_enable = models.BooleanField(default=True)
    is_subheader = models.BooleanField(default=True)
    is_recorrection = models.BooleanField(default=False)
    position = models.IntegerField(default=1)
    qcount = models.IntegerField(default=0)
    anscount = models.IntegerField(default=0)
    approved_count = models.IntegerField(default=0)
    rejected_count = models.IntegerField(default=0)
    questions = ArrayField(model_container=Questions, null=True)
    objects = models.Manager() # The default manager.
    mongoObjects = DjongoManager()

class CensusMember(BaseModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    survey_entry = models.ForeignKey(SurveyEntry,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    member_name = models.CharField(max_length=255,null=True,blank=True)
    member_id = models.IntegerField(default=0)
    objects = models.Manager() # The default manager.
    mongoObjects = DjongoManager()
    
class CensusCategory(BaseModel,models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    survey_entry = models.ForeignKey(SurveyEntry,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    census_member = models.ForeignKey(CensusMember,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    category_name = models.CharField(max_length=255,null=True,blank=True)
    position = models.IntegerField(default=1)
    page = models.IntegerField(default=1)
    part = models.CharField(max_length=100, null=True,blank=True) # dynamic or static
    
class CensusSections(BaseModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    survey_entry = models.ForeignKey(SurveyEntry,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    census_member = models.ForeignKey(CensusMember,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    census_category = models.ForeignKey(CensusCategory,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    section_name = models.CharField(max_length=255,null=True,blank=True)
    is_enable = models.BooleanField(default=True)
    is_subheader = models.BooleanField(default=True)
    is_recorrection = models.BooleanField(default=False)
    position = models.IntegerField(default=1)
    qcount = models.IntegerField(default=0)
    anscount = models.IntegerField(default=0)
    approved_count = models.IntegerField(default=0)
    rejected_count = models.IntegerField(default=0)
    questions = ArrayField(model_container=Questions, null=True)
    objects = models.Manager() # The default manager.
    mongoObjects = DjongoManager()

class OcrMaster(BaseModel,models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(Users,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name = "created_by_id"
    )
    survey_entry = models.ForeignKey(SurveyEntry,
                                     on_delete=models.CASCADE,
                                     null=True,
                                     default=None)
    initial_section = models.BooleanField(default=False)
    interview_section = models.BooleanField(default=False)
    house_hold_member_section = models.BooleanField(default=False)
    final_section = models.BooleanField(default=False)
    process_complete = models.BooleanField(default=False)
    ocr_images = MongoField(null=True)


class OcrOptions(BaseModel,models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    qid = models.CharField(max_length=50)
    ops = MongoField()

class NotificationHistory(BaseModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(Users,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name = "sender_id"
    )
    receiver = models.ForeignKey(Users,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name = "receiver_id"
    )
    title = models.CharField(max_length=255,null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    email_message = models.TextField(null=True,blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    is_seen = models.BooleanField(default=False)
    is_sent_mail = models.BooleanField(default=False)
    is_clear = models.BooleanField(default=False)
    objects = models.Manager() # The default manager.
    mongoObjects = DjongoManager()
    def user_email_trigger(self, title, html_content, email):
        md_email_trigger_jobs(title, email, html_content)
        return None
    def user_push_notification_trigger(self, title, html_content, receiver_id):
        user_obj = Users.objects.filter(id = receiver_id).first()
        if user_obj and user_obj.fcm_token:
            md_push_notification_trigger_jobs(title=title, fcm_token=user_obj.fcm_token, html_content=html_content)
        return None
class ReportCategories(BaseModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=255,null=True,blank=True)
    category_slug = models.CharField(max_length=255,null=True,blank=True)
    
class ReportHistory(BaseModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.ForeignKey(Location,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    report_category = models.ForeignKey(ReportCategories,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    meta_value = models.CharField(max_length=255,default="left")
    chart_constant_left = MongoField(null=True)
    chart_constant_right = MongoField(null=True)
    chart_response_left = MongoField(null=True)
    chart_response_right = MongoField(null=True)
    chart_unique_constant_left = MongoField(null=True)
    chart_unique_constant_right = MongoField(null=True)
    excel_response = MongoField(null=True)
    excel_constant = MongoField(null=True)
