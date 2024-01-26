import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework import status
from rbimapi.mongoaggregate.survey import mdb_suvery_questions, mdb_section, mdb_suvery_list_count, mdb_suvery_list, \
    survey_entry_elastic_search
from rbimapi.mongoaggregate.survey import mdb_suvery_static_all_questions, mdb_suvery_entry_details, mdb_census_static_category_details
from rbimapi.mongoaggregate.survey import mdb_house_hold_member_section_details, mdb_survey_home_dashboard_list, mdb_survey_home_dashboard_list_count
from rbimapi.mongoaggregate.survey import mdb_hh_suvery_static_all_questions, mdb_suvery_recorrection_details, mdb_survey_entry_year_reports
from rbimapi.serializers.SurverySerializers import (SurveyMasterSerializer, SectionSerializer,
    CensusStaticSectionSerializer, CensusSectionSerializer)
from rbimapi.serializers.SurverySerializers import CensusStaticCategorySerializer, CensusCategorySerializer, SurveyEntrySerializer, CensusMemberSerializer
from rbimapi.serializers.SurverySerializers import SurveyQuestionVerificationSerializer, SurveyEntryUpdateSerializer, SurveyMbLocalSerializer, OcrVerificationSerializer
from rbimapi.serializers.NotificationHistorySerializers import NotificationHistorySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rbim.models import (Users, SurveyEntry, CensusMember)
from rbimapi.utilities import round_up
import constants
import emailConstants
from rbimapi.validations import PageValidation
import datetime
import staticContent
from rbimapi.threads import SurveyEntryThread
class CreateSurveyMasterAPIView(generics.CreateAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    serializer_class = SurveyMasterSerializer
    def create(self, request):
        try:
            serializer = self.get_serializer(data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                return Response({"status":1, "message":"Survey master save sucessfully", 'data':serializer.data},status=status.HTTP_201_CREATED)
            return Response({"status":0, "message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
           return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class GetSurveyMasterAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def get(self,request):
        try:
            dyparam = {}
            dyparam['match'] = {
                'deleted_at': None
            }
            res_survey_details = mdb_suvery_questions(dyparam)
            return Response({"status":1, "data":res_survey_details}, status=status.HTTP_200_OK)
        except Exception as e:
           return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class CreateSectionAPIView(generics.CreateAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    serializer_class = SectionSerializer
    def create(self, request):
        try:
            serializer = self.get_serializer(data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                return Response({"status":1, "message":"Survey section save sucessfully", 'data':serializer.data},status=status.HTTP_201_CREATED)
            return Response({"status":0, "message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class GetSectionAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def get(self,request,id):
        try:   
            param={}
            param['match'] ={'survey_master_id':uuid.UUID(id)}
            section_details = mdb_section(param)
            return Response({"status":1, "data":section_details}, status=status.HTTP_200_OK)
        except Exception as e:
           return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class CreateSurveyEntryAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def post(self, request):
        try:
            user_obj = Users.objects.filter(id=self.request.user.id).first()
            if not user_obj:
                return Response({"status":0,"message":constants.DATA_NOT_FOUND_ERROR_MSG},status=status.HTTP_400_BAD_REQUEST)
            survey_entry_param = {}
            survey_entry_param['survey_number'] = request.data.get("survey_number", None)
            survey_entry_param['status'] = request.data.get("status", None)
            survey_entry_param['survey_type'] = constants.SURVEY_TYPE[0]
            survey_entry_param['data_collector'] = user_obj.id
            survey_entry_param['data_reviewer'] = user_obj.data_reviewer_id
            survey_entry_param['barangay'] = user_obj.barangay_id
            survey_entry_param['household_member_count'] = request.data.get("household_member_count", None)
            survey_entry_param['members'] = request.data.get("members", None)
            survey_entry_param['data_collector_signature'] = request.data.get("data_collector_signature", None)
            survey_entry_param['survey_assigned_on'] = request.data.get("survey_assigned_on", None)
            survey_entry_param['mobile_next_section'] = request.data.get("mobile_next_section", None)
            survey_entry_param['notes'] = request.data.get("notes", None)
            serializer = SurveyEntrySerializer(data = survey_entry_param)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                user_obj.dashboard_count_auto_update()
                if serializer.data:
                    survey_entry_id = serializer.data.get('id')
                    SurveyEntryThread(survey_entry_id, request,user_obj).start()

                return Response({"status":1, "message":"Saved","survey_entry_id":survey_entry_id},status=status.HTTP_200_OK)
            return Response({"status":0, "message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
           return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class GetSurveyListView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsAuthenticated,]

    def survey_status_date_param(self, status):
        return f'${status}' + '_on'

    def remove_special_character(self, search_text):
        special_string = "*\[]()?+"
        for i in special_string:
            search_text = search_text.replace(i, '')
        return search_text

    def post(self,request):
        try:
            PageValidation.validate_page_with_status(data = request.data)
            page = request.data['page']
            page_size = request.data['page_size']
            search = request.data['search']
            if(page == 1):
                skip = 0
            else:
                skip = (page - 1) * page_size
            survey_param = {}
            survey_param['skip'] = skip
            survey_param['page_size'] = page_size
            survey_param['sort'] = {'created_at':-1}
            survey_param['SURVEY_STATUS'] = constants.SURVEY_STATUS
            survey_param['survey_status_date_param'] = self.survey_status_date_param(status=request.data['status'])
            survey_param['survey_status'] = constants.SURVEY_STATUS[6] if request.data['status'] == constants.SURVEY_STATUS[3] else  request.data['status']
            # Condition Added Here
            conditions_match = {}
            conditions_match['status'] = request.data['status']
            if request.data["status"] == constants.SURVEY_STATUS[3]:
                conditions_match['status'] = {
                    "$in": [constants.SURVEY_STATUS[4], constants.SURVEY_STATUS[5], constants.SURVEY_STATUS[6]]
                }
            if request.user.role == constants.USER_ROLES[1]:
                conditions_match['barangay_id'] = request.user.id
            else:
                conditions_match['data_reviewer_id'] = request.user.id
            conditions_match['deleted_at'] = None
            survey_param['match'] = conditions_match
            if search:
                remove_spl_char = self.remove_special_character(search_text=search)
                print(remove_spl_char)
                survey_param['text_search'] = f"{remove_spl_char}"
                survey_es = survey_entry_elastic_search(survey_param)
                if survey_es:
                    conditions_match['id'] = {'$in': survey_es[0]['id']}
                    survey_param['match'] = conditions_match
                    survey_list_count = mdb_suvery_list_count(survey_param)
                    survey_list = mdb_suvery_list(survey_param)
                    total_records = survey_list_count
                    num_pages = (total_records / page_size)
                    num_pages = round_up(num_pages)
                    return Response({
                        "status":1,
                        "message":"Fetched",
                        "paginator": staticContent.pagination_param(total_records=total_records, num_pages=num_pages, page=page, obj_info=survey_list),
                        "data":survey_list
                    },status=status.HTTP_200_OK)
                else:
                    return Response({
                        "status": 1,
                        "message": "Fetched",
                        "paginator": staticContent.pagination_param(total_records=0, num_pages=1,
                                                                    page=page, obj_info=[]),
                        "data": []
                    }, status=status.HTTP_200_OK)
            survey_param['match'] = conditions_match
            survey_list_count = mdb_suvery_list_count(survey_param)
            survey_list = mdb_suvery_list(survey_param)
            total_records = survey_list_count
            num_pages = (total_records / page_size)
            num_pages = round_up(num_pages)
            return Response({
                "status": 1,
                "message": "Fetched",
                "paginator": staticContent.pagination_param(total_records=total_records, num_pages=num_pages, page=page,
                                                            obj_info=survey_list),
                "data": survey_list
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status":0,
                "message":str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
class GetSuveryStaticAllQuestionsAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def get(self,request):
        try:   
            res_survey_details = {}
            initial_param = {}
            initial_param['match'] = {
                'deleted_at': None,
                'part':'initial_section'
            }
            res_survey_details["initial_section"] = mdb_suvery_static_all_questions(initial_param)[0]
            interview_section_param = {}
            interview_section_param['match'] = {
                'deleted_at': None,
                'part':'interview_section'
            }
            res_survey_details["interview_section"] = mdb_suvery_static_all_questions(interview_section_param)
            house_hold_member_section_param = {}
            house_hold_member_section_param['match'] = {
                'deleted_at': None,
                'part':'house_hold_member_section'
            }
            res_survey_details["house_hold_member_section"] = mdb_hh_suvery_static_all_questions(house_hold_member_section_param)
            final_section_param = {}
            final_section_param['match'] = {
                'deleted_at': None,
                'part':'final_section'
            }
            res_survey_details["final_section"] = mdb_suvery_static_all_questions(final_section_param)
            return Response({"status":1, "data":res_survey_details}, status=status.HTTP_200_OK)
        except Exception as e:
           return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
class GetViewSuveryEntryQuestionAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def get(self,request, survey_entry_id):
        try:
            res_survey_details = {}
            survey_entry_param = {}
            survey_entry_param['match'] = {
                "id":uuid.UUID(survey_entry_id)
            }
            initial_section_param = {}
            initial_section_param['match'] = {
                "survey_entry_id":uuid.UUID(survey_entry_id),
                "part":"initial_section"
            }
            interview_section_param = {}
            interview_section_param['match'] = {
                "survey_entry_id":uuid.UUID(survey_entry_id),
                "part":"interview_section"
            }

            house_hold_member_section_param = {}
            house_hold_member_section_param['match'] = {
                "survey_entry_id":uuid.UUID(survey_entry_id)
            }
            final_section_param = {}
            final_section_param['match'] = {
                "survey_entry_id":uuid.UUID(survey_entry_id),
                "part":"final_section"
            }
            res_survey_details = mdb_suvery_entry_details(survey_entry_param)[0]
            res_survey_details["initial_section"] = mdb_census_static_category_details(initial_section_param)[0]
            res_survey_details["interview_section"] = mdb_census_static_category_details(interview_section_param)
            res_survey_details["house_hold_member_section"] = mdb_house_hold_member_section_details(house_hold_member_section_param)
            res_survey_details["final_section"] = mdb_census_static_category_details(final_section_param)
            return Response({"status":1, "data":res_survey_details}, status=status.HTTP_200_OK)
        except Exception as e:
           return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
class GetSurveyListAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def post(self,request):
        try:
            # Validations
            PageValidation.validate_page_with_status(data = request.data) 
            page        = request.data['page']
            page_size   = request.data['page_size']
            if(page == 1):
                skip = 0
            else:
                skip = (page - 1) * page_size            
            survey_home_dashboard_param = {}
            survey_home_dashboard_param['skip'] = skip
            survey_home_dashboard_param['page_size'] = page_size
            survey_home_dashboard_param['sort'] = {'created_at':-1}
            # Condition Added Here
            conditions_match = {}
            conditions_match['status'] = request.data['status']
            conditions_match['data_collector_id'] = request.user.id 
            conditions_match['deleted_at'] = None
            search_fields = ['survey_number']
            search_param = []
            if request.data["search"]:
                for sval in search_fields:
                    ar_prm = {
                        sval : {'$regex':request.data["search"], '$options':'i'}
                    }
                    search_param.append(ar_prm)
                conditions_match['$or'] = search_param

            survey_home_dashboard_param['match'] = conditions_match           
            survey_home_dashboard_list_count = {}
            survey_home_dashboard_list_count = mdb_survey_home_dashboard_list_count(survey_home_dashboard_param)
            survey_home_dashboard_list = mdb_survey_home_dashboard_list(survey_home_dashboard_param)
            total_records = survey_home_dashboard_list_count
            num_pages = (total_records / page_size)
            num_pages = round_up(num_pages)
            return Response({
                "status":1,
                "message":"Fetched",
                "paginator": staticContent.pagination_param(total_records=total_records, num_pages=num_pages, page=page, obj_info=survey_home_dashboard_list),
                "data":survey_home_dashboard_list
            },status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
class SurveyQuestionVerificationAPIView(generics.CreateAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def post(self, request):
        try:
            serializer = SurveyQuestionVerificationSerializer(data = request.data, context={"user_id":request.user.id})
            if serializer.is_valid(raise_exception = True):
                return Response({"status":1, "message":"Submited sucessfully", "data":serializer.validated_data},status=status.HTTP_201_CREATED)
            return Response({"status":0, "message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
           return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
class SurveyRecorrectionSubmitAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def static_question(self, survey_entry_id, survey_data):
        for cat_val in survey_data:
            cat_val["survey_entry"] = survey_entry_id
            for section_val in cat_val['section']:
                if section_val['is_recorrection']==True:
                    cs_section_serializers = CensusStaticSectionSerializer(section_val["id"], data=section_val, partial=True)
                    if cs_section_serializers.is_valid(raise_exception = True):
                        cs_section_serializers.save()

    def member_question(self, survey_entry_id, hh_meber):
        for member_values in hh_meber:
            member_values['survey_entry'] = survey_entry_id
            for page_val in member_values['category']:
                for cat_mem_val in page_val['page']:
                    for section_val in cat_mem_val['section']:
                        if section_val['is_recorrection']==True:
                            cs_serializers = CensusSectionSerializer(section_val["id"], data=section_val, partial=True)
                            if cs_serializers.is_valid(raise_exception = True):
                                cs_serializers.save()

    def post(self, request):
        try:
            user_obj = Users.objects.filter(id=self.request.user.id).first()
            if not user_obj:
                return Response({"status":0,"message":constants.DATA_NOT_FOUND_ERROR_MSG},status=status.HTTP_400_BAD_REQUEST)
            save_status = []
            survey_entry_param = {}
            survey_entry_param['survey_number'] = request.data.get("survey_number", None)
            survey_entry_param['status'] = request.data.get("status", None)
            survey_entry_param['household_member_count'] = request.data.get("household_member_count", None)
            survey_entry_param['data_collector_signature'] = request.data.get("data_collector_signature", None)
            survey_entry_param['survey_assigned_on'] = request.data.get("survey_assigned_on", None)
            survey_entry_param['mobile_next_section'] = request.data.get("mobile_next_section", None)
            survey_entry_param['notes'] = request.data.get("notes", None)
            survey_entry_id = request.data.get("id", None)
            se_serializers = SurveyEntryUpdateSerializer(survey_entry_id, data=survey_entry_param, partial=True)
            if se_serializers.is_valid(raise_exception = True):
                se_serializers.save()
            if request.data.get("initial_section"):
                initial_section_val = []
                initial_section_val.append(request.data.get("initial_section"))
                self.static_question(survey_entry_id, initial_section_val)
                save_status.append("initial_section")
            if request.data.get("interview_section"):
                self.static_question(survey_entry_id, request.data.get("interview_section"))
                save_status.append("interview_section")
            if request.data.get("house_hold_member_section"):
                self.member_question(survey_entry_id, request.data.get("house_hold_member_section"))
                save_status.append("house_hold_member_section")
            if request.data.get("final_section"):
                self.static_question(survey_entry_id, request.data.get("final_section"))
                save_status.append("final_section")
                
            nt_message = emailConstants.NT_MESSAGE_DC_COMPLETE_SURVEY.format(user_obj.first_name, request.data.get("survey_number", None))
            email_message = emailConstants.EMAIL_MESSAGE_DC_COMPLETE_SURVEY.format(user_obj.first_name, request.data.get("survey_number", None))
            title = emailConstants.SUBJECT_DC_COMPLETE_SURVEY
            dc_survey_completed_param = staticContent.notification_param(sender=user_obj.id, receiver=user_obj.id, title=title, nt_message=nt_message, email_message=email_message, email=user_obj.email)
            nh_serializer = NotificationHistorySerializer(data=dc_survey_completed_param)
            nh_serializer.is_valid(raise_exception = True)
            nh_serializer.save()
                
            return Response({"status":1, "message":"Saved", "data":save_status},status=status.HTTP_200_OK)
        except Exception as e:
           return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class OngoingSurveyEntryAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def comman_question_and_answer_create(self, survey_entry_id, survey_data, part):
        for cat_val in survey_data:
            cat_val["survey_entry"] = survey_entry_id
            cat_val["part"] = part
            if not cat_val.get("id", None):
                cat_serializers = CensusStaticCategorySerializer(data = cat_val)
                if cat_serializers.is_valid(raise_exception = True):
                    cat_serializers.save()
                    census_static_category = cat_serializers.data.get('id')
            else:
               census_static_category =  cat_val["id"]
            if census_static_category:
                for section_val in cat_val['section']:
                    section_val['survey_entry'] = survey_entry_id
                    section_val['census_static_category'] = census_static_category
                    if not section_val.get("id", None):
                        cs_section_serializers = CensusStaticSectionSerializer(data = section_val)
                        if cs_section_serializers.is_valid(raise_exception = True):
                            cs_section_serializers.save()
                    else:
                        cs_section_serializers = CensusStaticSectionSerializer(section_val["id"], data=section_val, partial=True)
                        if cs_section_serializers.is_valid(raise_exception = True):
                            cs_section_serializers.save()

    def member_question_and_answer_create(self, survey_entry_id, hh_meber, part):
        for member_values in hh_meber:
            member_values['survey_entry'] = survey_entry_id
            if not member_values.get("id", None):
                member_serializers = CensusMemberSerializer(data = member_values)
                if member_serializers.is_valid(raise_exception = True):
                    member_serializers.save()
                    census_member = member_serializers.data.get('id')
            else:
                census_member = member_values["id"]
            if census_member:
                for page_val in member_values['category']:
                    for cat_mem_val in page_val['page']:
                        cat_mem_val["survey_entry"] = survey_entry_id
                        cat_mem_val["census_member"] = census_member
                        cat_mem_val["part"] = part
                        if not cat_mem_val.get("id", None):
                            cat_serializers = CensusCategorySerializer(data = cat_mem_val)
                            if cat_serializers.is_valid(raise_exception = True):
                                cat_serializers.save()
                                census_category = cat_serializers.data.get('id')
                        else:
                            census_category = cat_mem_val["id"]
                        if census_category:
                            for section_val in cat_mem_val['section']:
                                section_val['survey_entry'] = survey_entry_id
                                section_val['census_member'] = census_member
                                section_val['census_category'] = census_category
                                if not section_val.get("id", None):
                                    cs_serializers = CensusSectionSerializer(data = section_val)
                                    if cs_serializers.is_valid(raise_exception = True):
                                        cs_serializers.save()
    def post(self, request):
        try:
            user_obj = Users.objects.filter(id=self.request.user.id).first()
            if not user_obj:
                return Response({"status":0,"message":constants.DATA_NOT_FOUND_ERROR_MSG},status=status.HTTP_400_BAD_REQUEST)
            survey_entry_param = {}
            survey_entry_param['survey_number'] = request.data.get("survey_number", None)
            survey_entry_param['status'] = request.data.get("status", None)
            survey_entry_param['household_member_count'] = request.data.get("household_member_count", None)
            survey_entry_param['members'] = request.data.get("members", None)
            survey_entry_param['data_collector_signature'] = request.data.get("data_collector_signature", None)
            survey_entry_param['survey_assigned_on'] = request.data.get("survey_assigned_on", None)
            survey_entry_param['mobile_next_section'] = request.data.get("mobile_next_section", None)
            survey_entry_param['notes'] = request.data.get("notes", None)
            survey_entry_param['mb_local'] = None
            if not request.data.get("id", None):
                serializer = SurveyEntrySerializer(data=survey_entry_param)
                if serializer.is_valid(raise_exception = True):
                    serializer.save()
                    survey_entry_id = serializer.data.get('id')
            else:
                survey_entry_id = request.data.get("id", None)
                se_serializers = SurveyEntryUpdateSerializer(survey_entry_id, data=survey_entry_param, partial=True)
                if se_serializers.is_valid(raise_exception = True):
                    se_serializers.save()
            if survey_entry_id:
                save_status = []
                if request.data.get("initial_section"):
                    initial_section_val = []
                    initial_section_val.append(request.data.get("initial_section"))
                    self.comman_question_and_answer_create(survey_entry_id, initial_section_val, 'initial_section')
                    save_status.append("initial_section")
                if request.data.get("interview_section"):
                    self.comman_question_and_answer_create(survey_entry_id, request.data.get("interview_section"), 'interview_section')
                    save_status.append("interview_section")
                if request.data.get("house_hold_member_section"):
                    self.member_question_and_answer_create(survey_entry_id, request.data.get("house_hold_member_section"), 'house_hold_member_section')
                    save_status.append("house_hold_member_section")
                if request.data.get("final_section"):
                    self.comman_question_and_answer_create(survey_entry_id, request.data.get("final_section"), 'final_section')
                    save_status.append("final_section")
            return Response({"status":1, "message":"Saved", "data":save_status, "survey_entry_id":survey_entry_id},status=status.HTTP_200_OK)
        except Exception as e:
           return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class GetHomeDashboardAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def get(self,request):
        try:
            # Validations
            survey_home_dashboard_param = {}
            survey_home_dashboard_param['skip'] = 0
            survey_home_dashboard_param['page_size'] = 3
            survey_home_dashboard_param['sort'] = {'created_at':-1}
            
            # Condition Added Here
            conditions_match = {}
            conditions_match['data_collector_id'] = request.user.id 
            conditions_match['deleted_at'] = None
            survey_home_dashboard_list = {}
            conditions_match['status'] = "survey_recorrection"
            survey_home_dashboard_param['match'] = conditions_match 
            survey_home_dashboard_list["recorrection"] = mdb_survey_home_dashboard_list(survey_home_dashboard_param)

            return Response({"status":1, "message":"Fetched","data":survey_home_dashboard_list},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)

class SurveyMbLocalAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    serializer_class = SurveyMbLocalSerializer
    def post(self, request, survey_entry_id):
        try:
            survey_entry_obj = SurveyEntry.objects.filter(id = survey_entry_id).first()
            if survey_entry_obj:
                survey_entry_obj.mb_local = request.data.get('mb_local', None)
                survey_entry_obj.save()
                return Response({"status":1, "message":"MB Saved sucessfully"},status=status.HTTP_201_CREATED)
            return Response({"status":0, "message":"Something wront"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
           return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, survey_entry_id):
        try:
            survey_entry_obj = SurveyEntry.objects.filter(id = survey_entry_id).first()
            survey_entry_obj = self.get_serializer(survey_entry_obj).data
            if not survey_entry_obj:
                return Response({"status":0,"message":constants.USER_NOT_FOUND_ERROR_MSG},status = status.HTTP_404_NOT_FOUND)
            return Response({"status":1,"message":"User data retrieved","data":survey_entry_obj},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
class OcrVerificationAPIView(generics.CreateAPIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def post(self, request):
        try:
            serializer = OcrVerificationSerializer(data = request.data, context={"user_id":request.user.id})
            if serializer.is_valid(raise_exception = True):
                return Response({"status":1, "message":"OCR Saved sucessfully", "data":serializer.validated_data},status=status.HTTP_201_CREATED)
            return Response({"status":0, "message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
           return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
class GetSuveryRecorrectionListAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def get(self,request):
        try:
            res_survey_details = {}
            survey_entry_param = {}
            survey_entry_param['match'] = {
                "data_collector_id":request.user.id,
                "status":"survey_recorrection"
            }
            res_survey_details = mdb_suvery_recorrection_details(survey_entry_param)
            if res_survey_details:
                return Response({"status":1, "data":res_survey_details}, status=status.HTTP_200_OK)
            else:
                return Response({"status":0, "message":constants.DATA_NOT_FOUND_ERROR_MSG}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
           return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class GetSuveryYearReportsListAPIView(APIView):
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]
    def get(self,request):
        try:
            today = datetime.date.today()
            year = int(today.strftime("%Y"))
            report_param = {}
            report_param['match'] = {
                "deleted_at":None,
                "created_year":year
            }
            res_survey_details = mdb_survey_entry_year_reports(report_param)
            if res_survey_details:
                return Response({"status":1, "data":res_survey_details}, status=status.HTTP_200_OK)
            else:
                return Response({"status":0, "message":constants.DATA_NOT_FOUND_ERROR_MSG}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
           return Response({"status":0,"message":str(e)},status=status.HTTP_400_BAD_REQUEST)


class OcrSurveyMembersUpdateAPIView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def post(self,request):
        survey_entry_id = request.data.get('survey_entry_id')
        members = request.data.get('members')
        check_survey_entry = SurveyEntry.objects.filter(id=survey_entry_id).first()
        if check_survey_entry:
            SurveyEntry.objects.filter(id=survey_entry_id).update(members=members)
            for member in members:
                CensusMember.objects.filter(survey_entry_id=survey_entry_id,
                                            member_id=member['member_id']).update(
                                            member_name=member['member_name'])
            return Response(dict(status=1, message="Members data updated successfully"), status=status.HTTP_200_OK)
        else:
            return Response(dict(status=0, message="Survey not found"), status=status.HTTP_404_NOT_FOUND)




