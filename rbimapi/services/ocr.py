import copy
import re
import threading
import boto3
from trp import Document
import config
import constants
from ocr_contstant_json import constant_json, member_json
from rbim.models import (OcrMaster, OcrOptions, Users, SurveyEntry)
from ocr_contructed_json import ocr_json
from rbim.models import (Users)
from rbimapi.serializers.SurverySerializers import (CensusStaticSectionSerializer,
                                                    CensusMemberSerializer, CensusCategorySerializer,
                                                    CensusSectionSerializer, CensusStaticCategorySerializer,
                                                    SurveyEntryUpdateSerializer)


class OCRProcess:
    def __init__(self, survey_entry_id=None, **kwargs):
        self.image_path = []
        self.survey_entry_id = survey_entry_id
        self.current_page = 0
        self.AWS_ACCESS_KEY_ID = config.AWS_ACCESS_KEY_ID
        self.AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY
        self.AWS_STORAGE_BUCKET_NAME = config.AWS_STORAGE_BUCKET_NAME

    def connect_s3(self):
        filter_census_image = OcrMaster.objects.filter(survey_entry_id=self.survey_entry_id).first()
        # ordering image based on last modified date
        for img in filter_census_image.ocr_images:
            self.image_path.append(f"media/{img.split('/')[-1]}")
        return None

    # Connecting To AWS Textract
    def connect_textract(self):
        # Connecting Textract
        textract = boto3.client('textract', region_name='ap-south-1',
                                aws_access_key_id=self.AWS_ACCESS_KEY_ID,
                                aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY)
        return textract

    # Read Uploaded Images
    def read_image(self):
        # Reading survey image using textract
        textract = self.connect_textract()
        for c_page, img in enumerate(self.image_path):
            self.current_page = c_page + 1
            response = textract.analyze_document(Document={'S3Object': {'Bucket': self.AWS_STORAGE_BUCKET_NAME,
                                                                        'Name': img}},
                                                 FeatureTypes=['FORMS', 'TABLES'])
            doc_response = Document(response)
            self.construct_page_json(doc_response)
        # calling survey entry payload json function
        self.construct_constant_json(ocr_json)
        constructed_json = self.construct_members_constant_json(ocr_json)
        return constructed_json

    def regex_page_checker(self, value):
        page_no = 0
        page_2 = re.search(r'\bQ5\b', value.strip())
        page_3 = re.search(r'\bQ8\b', value.strip())
        page_4 = re.search(r'\bQ15\b', value.strip())
        page_5 = re.search(r'\bQ19\b', value.strip())
        page_6 = re.search(r'\bQ27\b', value.strip())
        page_7 = re.search(r'\bQ31\b', value.strip())
        page_8 = re.search(r'\bQ37\b', value.strip())
        page_9 = re.search(r'\bQ41\b', value.strip())

        if page_2:
            page_no = 2
            return page_no
        if page_3:
            page_no = 3
            return page_no
        if page_4:
            page_no = 4
            return page_no
        if page_5:
            page_no = 5
            return page_no
        if page_6:
            page_no = 6
            return page_no
        if page_7:
            page_no = 7
            return page_no
        if page_8:
            page_no = 8
            return page_no
        if page_9:
            page_no = 9
            return page_no
        else:
            return page_no

    def construct_page_json(self, response):
        # Constructing JSON for extracted pages
        page_1 = False
        ocr_json_ = {}
        ocr_section_2 = ocr_json[0][f'section_2']
        for page in response.pages:
            key = "Household Head"
            field = page.form.getFieldByKey(key)
            if field:
                page_1 = True
                ocr_json_ = ocr_json[0][f'section_1']
                # ocr_json_ = ocr_json_ = ocr_json[0][f'section_1']
            # form data
            for field in page.form.fields:
                ocr_json_[f'{field.key}'.strip()] = f'{field.value}'.strip()
            # table data
            if page_1:
                for table in page.tables:
                    for r, row in enumerate(table.rows):
                        for c, cell in enumerate(row.cells):
                            ocr_json_[f'Table[1][{r}][{c}]'] = f'{cell.text}'.strip()
            else:
                for table in page.tables:
                    for r, row in enumerate(table.rows):
                        for c, cell in enumerate(row.cells):
                            ocr_json_[f'[{r}][{c}]'] = f'{cell.text}'.strip()

        page = 0
        if not page_1:
            for key, value in ocr_json_.items():
                check_page = self.regex_page_checker(value=value)
                if check_page != 0:
                    page = check_page
                    break
        for key, value in ocr_json_.items():
            ocr_section_2[f'Table[{page}]{key}'] = f'{value}'
        return None

    def filter_option_value(self, qid, index):
        get_option_obj = OcrOptions.objects.filter(qid=qid).first()
        selectbox_question = ["Q7", "Q11", "Q12", "Q23", "Q24", "Q26", "Q28"]
        index = index.strip()
        try:
            if index == 'I' or index == 'i':
                index = 1
            if index == 'II' or index == 'ii':
                index = 11
            if index == 'Il' or index == 'il':
                index = 11
            if int(index) == 99:
                return None
            if get_option_obj:
                option = get_option_obj.ops[int(index) - 1]
                if qid in selectbox_question:
                    return option.strip()
                return [option.strip()]
            return None
        except (ValueError, IndexError):
            return None

    def construct_constant_json(self, c_ocr_json):
        ocr_json_section_1 = c_ocr_json[0]['section_1']
        member_count = ocr_json_section_1['Total No. of Household Members']
        constant_json['survey_number'] = ocr_json_section_1['No.']
        constant_json['household_member_count'] = member_count
        ocr_survey_no = ocr_json_section_1['No.']
        filter_survey_no = SurveyEntry.objects.filter(survey_number=ocr_survey_no).first()
        if filter_survey_no:
            SurveyEntry.objects.filter(id=self.survey_entry_id).delete()
            OcrMaster.objects.filter(survey_entry_id=self.survey_entry_id).delete()
        else:
            SurveyEntry.objects.filter(id=self.survey_entry_id).update(survey_number=ocr_survey_no)

        # Intial Section
        initial_section_questions = constant_json['initial_section']['section'][0]['questions']
        # Interview Section
        interview_section_identification_questions_s1 = constant_json['interview_section'][0]['section'][0][
            'questions']
        interview_section_identification_questions_s2 = constant_json['interview_section'][0]['section'][1][
            'questions']
        # Interview Information
        interview_section_interview_inf_questions = constant_json['interview_section'][1]['section'][0][
            'questions']
        # Encoding Information
        interview_section_interview_encoding_inf_questions = constant_json['interview_section'][1]['section'][0][
            'questions']

        initial_section_questions[0]['answers'][0]['answer_value'] = ocr_json_section_1['No.']
        initial_section_questions[1]['answers'][0]['answer_value'] = True if ocr_json_section_1[
                                                                                 'Household'] == 'SELECTED' else False
        initial_section_questions[2]['answers'][0]['answer_value'] = True if ocr_json_section_1[
                                                                                 'Institutional Living Quarter'] == 'SELECTED' else False

        OcrMaster.objects.filter(
            survey_entry_id=self.survey_entry_id).update(initial_section=True)
        SurveyEntry.objects.filter(
            id=self.survey_entry_id).update(ocr_status=constants.OCR_STATUS[1])
        # Indentification Section
        interview_section_identification_questions_s1[0]['answers'][0]['answer_value'] = ocr_json_section_1[
            'Province']
        interview_section_identification_questions_s1[1]['answers'][0]['answer_value'] = 0  # province code
        interview_section_identification_questions_s1[2]['answers'][0]['answer_value'] = ocr_json_section_1[
            'City/Municipality']
        interview_section_identification_questions_s1[3]['answers'][0]['answer_value'] = 0  # municipality code
        interview_section_identification_questions_s1[4]['answers'][0]['answer_value'] = ocr_json_section_1[
            'Barangay']
        interview_section_identification_questions_s1[5]['answers'][0]['answer_value'] = 0  # barangay code
        interview_section_identification_questions_s1[6]['answers'][0]['answer_value'] = ocr_json_section_1[
            'Name of Respondent']
        interview_section_identification_questions_s1[7]['answers'][0]['answer_value'] = ocr_json_section_1[
            'Household Head']
        # interview_section_identification_questions_s1[8]['answers'][0]['answer_value'] = member_count
        interview_section_identification_questions_s2[0]['answers'][0]['answer_value'] = ''  # locality
        interview_section_identification_questions_s2[1]['answers'][0]['answer_value'] = ocr_json_section_1[
            '(Room/Floor/Unit No. and Building Name)']
        interview_section_identification_questions_s2[2]['answers'][0]['answer_value'] = ocr_json_section_1[
            '(House/Lot and Block No.)']
        interview_section_identification_questions_s2[3]['answers'][0]['answer_value'] = ocr_json_section_1[
            '(Street Name)']
        interview_section_interview_inf_questions[0]['answers'][0]['answer_value'] = None  # visit
        interview_section_interview_inf_questions[1]['answers'][0]['answer_value'] = None  # date of visit
        interview_section_interview_inf_questions[2]['answers'][0]['answer_value'] = None  # time start
        interview_section_interview_inf_questions[3]['answers'][0]['answer_value'] = None  # time end
        interview_section_interview_inf_questions[4]['answers'][0]['answer_value'] = ocr_json_section_1[
            'Table[1][1][4]']  # result
        interview_section_interview_inf_questions[5]['answers'][0]['answer_value'] = None  # date next visit
        interview_section_interview_inf_questions[6]['answers'][0]['answer_value'] = ocr_json_section_1[
            'Table[1][1][6]']  # name of interviewer
        interview_section_interview_inf_questions[7]['answers'][0]['answer_value'] = ocr_json_section_1[
            'Table[1][1][7]']  # intital
        interview_section_interview_inf_questions[8]['answers'][0]['answer_value'] = None  # date

        interview_section_interview_encoding_inf_questions[6]['answers'][0]['answer_value'] = ocr_json_section_1[
            'Barangay']
        try:
            OcrMaster.objects.filter(
                survey_entry_id=self.survey_entry_id).update(interview_section=True)
            SurveyEntry.objects.filter(
                id=self.survey_entry_id).update(ocr_status=constants.OCR_STATUS[2])
        except OcrMaster.DoesNotExist:
            pass
        return None

    def construct_members_constant_json(self, c_ocr_json):
        # try:
        # house_hold_member_section
        ocr_json_section_1 = c_ocr_json[0]['section_1']
        member_count = ocr_json_section_1['Total No. of Household Members']
        ocr_json_section_2 = c_ocr_json[0]['section_2']
        members_ = []
        survey_members = []
        for member in range(0, int(member_count)):
            member_json_ = copy.deepcopy(member_json)
            member_name = ocr_json_section_2[f"Table[2][{5 + member}][1]"]
            member_id = member + 1
            member_dict = {}
            member_json_['member_id'] = member + 1
            member_json_['member_name'] = member_name
            # Members List
            member_dict["member_id"] = member_id
            member_dict["member_name"] = member_name
            member_dict["member_completed_status"] = 0
            survey_members.append(member_dict)

            # Section - 1
            # Demographic Characteristics
            # FOR ALL HOUSEHOLD MEMBERS QUESTIONS
            household_members_questions = member_json_['category'][0]['page'][0]['section'][0]['questions']
            household_members_questions[0]['answers'][0]['answer_value'] = member_name
            try:
                # Relationship to head
                household_members_questions[1]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q2', index=ocr_json_section_2[f"Table[2][{5 + member}][2]"])
                # Sex
                household_members_questions[2]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q3',
                    index=ocr_json_section_2[f"Table[2][{5 + member}][3]"])
                # Age
                household_members_questions[3]['answers'][0]['answer_value'] = ocr_json_section_2[
                    f"Table[2][{5 + member}][4]"]
                # DOB
                household_members_questions[4]['answers'][0]['answer_value'] = None
                # Place of birth
                household_members_questions[5]['answers'][0]['answer_value'] = ocr_json_section_2[
                    f"Table[2][{5 + member}][6]"]
            except:
                pass
            try:
                # Nationality
                household_members_questions[6]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q7',
                    index=ocr_json_section_2[f"Table[3][{4 + member}][1]"])
                # Marital status
                household_members_questions[7]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q8',
                    index=ocr_json_section_2[f"Table[3][{4 + member}][2]"])
                # Religion
                household_members_questions[8]['answers'][0]['answer_value'] = ocr_json_section_2[
                    f"Table[3][{4 + member}][3]"]
                # Ethinicity
                household_members_questions[9]['answers'][0]['answer_value'] = ocr_json_section_2[
                    f"Table[3][{4 + member}][4]"]

                # Category - 2
                # A. Demographic Characteristics
                # FOR 5 YRS & ABOVE
                # FOR 3-24 YEARS OLD

                # Section - 1
                demographic_char_a_questions_section_1 = member_json_['category'][1]['page'][0]['section'][0][
                    'questions']
                # Highest level of education
                demographic_char_a_questions_section_1[0]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q11',
                    index=ocr_json_section_2[f"Table[3][{4 + member}][5]"])
                # Section - 2

                demographic_char_a_questions_section_2 = member_json_['category'][1]['page'][0]['section'][1][
                    'questions']
                # Currently Enrolled
                demographic_char_a_questions_section_2[0]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q12',
                    index=ocr_json_section_2[f"Table[3][{4 + member}][6]"])
                # School level
                demographic_char_a_questions_section_2[1]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q13',
                    index=ocr_json_section_2[f"Table[3][{4 + member}][7]"])
                # Place of school -NW
                demographic_char_a_questions_section_2[2]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q14',
                    index=ocr_json_section_2[f"Table[3][{4 + member}][8]"])
            except:
                pass
            try:
                # page 2 B. Economic Activity
                economic_questions_section = member_json_['category'][1]['page'][1]['section'][0]['questions']
                # Monthly income
                economic_questions_section[0]['answers'][0]['answer_value'] = None if ocr_json_section_2[
                                                                                          f"Table[4][{4 + member}][4]"].strip() == 'N' else \
                    ocr_json_section_2[f"Table[4][{4 + member}][4]"].strip()
                # Source of income
                economic_questions_section[1]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q16',
                    index=ocr_json_section_2[f"Table[4][{4 + member}][5]"])
                # Status of work / business
                economic_questions_section[2]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q17',
                    index=ocr_json_section_2[f"Table[4][{4 + member}][6]"])
                # Place of work / business
                economic_questions_section[3]['answers'][0]['answer_value'] = None if \
                    ocr_json_section_2[f"Table[4][{4 + member}][7]"].strip() == "Not Applicable" \
                    else ocr_json_section_2[f"Table[4][{4 + member}][7]"].strip()
            except:
                pass
            try:
                # C. Health Information
                # Section -1 For 0 to 11 months old
                health_info_questions_section = member_json_['category'][2]['page'][0]['section'][0]['questions']
                # Place of delivery
                health_info_questions_section[0]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q19',
                    index=ocr_json_section_2[f"Table[5][{4 + member}][1]"])
                # Birth attendant
                health_info_questions_section[1]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q20',
                    index=ocr_json_section_2[f"Table[5][{4 + member}][2]"])
                # Immunization
                health_info_questions_section[2]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q21',
                    index=ocr_json_section_2[f"Table[5][{4 + member}][3]"])
                # Health Information Section - 2 FOR WOMEN 10 TO 54 YEARS
                health_info_questions_section = member_json_['category'][2]['page'][0]['section'][1]['questions']
                # Living children
                health_info_questions_section[0]['answers'][0]['answer_value'] = ocr_json_section_2[
                    f"Table[5][{4 + member}][4]"]
                # Family planning
                health_info_questions_section[1]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q23',
                    index=ocr_json_section_2[f"Table[5][{4 + member}][5]"])
                # Siurce of fp method
                health_info_questions_section[2]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q24',
                    index=ocr_json_section_2[f"Table[5][{4 + member}][6]"])
                # Intention of use fp
                health_info_questions_section[3]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q25',
                    index=ocr_json_section_2[f"Table[5][{4 + member}][7]"])
            except:
                pass
            try:
                # Category - 4
                # C. Health Information
                # Page-1 Section - 1 FOR ALL HOUSEHOLD MEMBERS
                health_info_2__questions_section = member_json_['category'][3]['page'][0]['section'][0]['questions']
                # Health insurance
                health_info_2__questions_section[0]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q26',
                    index=ocr_json_section_2[f"Table[6][{4 + member}][4]"])
                # Facility visited in past 12 month
                health_info_2__questions_section[1]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q27',
                    index=ocr_json_section_2[f"Table[6][{4 + member}][5]"])
                # Reason for visit in health facilty
                health_info_2__questions_section[2]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q28',
                    index=ocr_json_section_2[f"Table[6][{4 + member}][6]"])
                # Disability
                health_info_2__questions_section[3]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q29',
                    index=ocr_json_section_2[f"Table[6][{4 + member}][7]"])
            except:
                pass
            try:
                # Category - 4
                # Page-2 Section - 1 D. Socio-Civic Participation FOR 10 & ABOVE
                socio_civic_questions_section_1 = member_json_['category'][3]['page'][1]['section'][0]['questions']
                socio_civic_questions_section_2 = member_json_['category'][3]['page'][1]['section'][1]['questions']
                socio_civic_questions_section_3 = member_json_['category'][3]['page'][1]['section'][2]['questions']
                socio_civic_questions_section_1[0]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q30',
                    index=ocr_json_section_2[f"Table[7][{4 + member}][0]"])
                socio_civic_questions_section_2[0]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q31',
                    index=ocr_json_section_2[f"Table[7][{4 + member}][1]"])
                socio_civic_questions_section_3[0]['answers'][0]['answer_value'] = ocr_json_section_2[
                    f"Table[7][{4 + member}][2]"]

                # Category - 5 E. Migration Information
                # FOR ALL HOUSEHOLD MEMBERS
                migration_info_questions_section_1 = member_json_['category'][4]['page'][0]['section'][0]['questions']
                migration_info_questions_section_2 = member_json_['category'][4]['page'][0]['section'][1]['questions']
                migration_info_questions_section_1[0]['answers'][0]['answer_value'] = ocr_json_section_2[
                    f"Table[7][{4 + member}][3]"]
                migration_info_questions_section_1[1]['answers'][0]['answer_value'] = ocr_json_section_2[
                    f"Table[7][{4 + member}][4]"]
                migration_info_questions_section_1[2]['answers'][0]['answer_value'] = ocr_json_section_2[
                    f"Table[7][{4 + member}][5]"]
                migration_info_questions_section_1[3]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q36',
                    index=ocr_json_section_2[f"Table[7][{4 + member}][6]"])
            except:
                pass
            try:
                # FOR MIGRANTS AND TRANSIENTS
                migration_info_questions_section_2[0]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q37',
                    index=ocr_json_section_2[f"Table[8][{4 + member}][4]"])
                migration_info_questions_section_2[1]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q38',
                    index=ocr_json_section_2[f"Table[8][{4 + member}][5]"])
            except:
                pass
            try:
                # Category 6 E. Migration Information
                # Page 1
                # FOR MIGRANTS AND TRANSIENTS
                migration_info_questions_section_3 = member_json_['category'][5]['page'][0]['section'][0]['questions']
                migration_info_questions_section_3[0]['answers'][0]['answer_value'] = None
                migration_info_questions_section_3[1]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q40',
                    index=ocr_json_section_2[f"Table[9][{4 + member}][0]"])
                migration_info_questions_section_3[2]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q41',
                    index=ocr_json_section_2[f"Table[9][{4 + member}][3]"])

                # Page 2
                # F. Community Tax Certificate
                comm_tax_certificate_questions_section = member_json_['category'][5]['page'][1]['section'][0][
                    'questions']
                comm_tax_certificate_questions_section[0]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q42A',
                    index=ocr_json_section_2[f"Table[9][{4 + member}][4]"])
                comm_tax_certificate_questions_section[1]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q42B',
                    index=ocr_json_section_2[f"Table[9][{4 + member}][5]"])
                # Page 3
                # G. Skill Development
                skill_dev_questions_section = member_json_['category'][5]['page'][2]['section'][0]['questions']
                skill_dev_questions_section[0]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q43',
                    index=ocr_json_section_2[f"Table[9][{4 + member}][6]"])
                skill_dev_questions_section[1]['answers'][0]['answer_value'] = self.filter_option_value(
                    qid='Q44',
                    index=ocr_json_section_2[f"Table[9][{4 + member}][7]"])
            except:
                pass

            members_.append(member_json_)

        constant_json['members'] = survey_members
        constant_json['house_hold_member_section'] = members_
        try:
            OcrMaster.objects.filter(
                survey_entry_id=self.survey_entry_id).update(house_hold_member_section=True,
                                                             final_section=True)
        except OcrMaster.DoesNotExist:
            pass
        return constant_json


class CreateOCRSurveyEntry:

    def __init__(self, request, **kwargs):
        self.request = request

    def comman_question_and_answer_create(self, survey_entry_id, survey_data, part):
        for cat_val in survey_data:
            cat_val["survey_entry"] = survey_entry_id
            cat_val["part"] = part
            cat_serializers = CensusStaticCategorySerializer(data=cat_val)
            if cat_serializers.is_valid(raise_exception=True):
                cat_serializers.save()
            if cat_serializers.data:
                for section_val in cat_val['section']:
                    section_val['survey_entry'] = survey_entry_id
                    section_val['census_static_category'] = cat_serializers.data.get('id')
                    cs_section_serializers = CensusStaticSectionSerializer(data=section_val)
                    if cs_section_serializers.is_valid(raise_exception=True):
                        cs_section_serializers.save()

    def member_question_and_answer_create(self, survey_entry_id, hh_meber, part):
        for member_values in hh_meber:
            member_values['survey_entry'] = survey_entry_id
            member_serializers = CensusMemberSerializer(data=member_values)
            if member_serializers.is_valid(raise_exception=True):
                member_serializers.save()
                if member_serializers.data:
                    for page_val in member_values['category']:
                        for cat_mem_val in page_val['page']:
                            cat_mem_val["survey_entry"] = survey_entry_id
                            cat_mem_val["census_member"] = member_serializers.data.get('id')
                            cat_mem_val["part"] = part
                            cat_serializers = CensusCategorySerializer(data=cat_mem_val)
                            if cat_serializers.is_valid(raise_exception=True):
                                cat_serializers.save()
                            if cat_serializers.data:
                                for section_val in cat_mem_val['section']:
                                    section_val['survey_entry'] = survey_entry_id
                                    section_val['census_member'] = member_serializers.data.get('id')
                                    section_val['census_category'] = cat_serializers.data.get('id')
                                    cs_serializers = CensusSectionSerializer(data=section_val)
                                    if cs_serializers.is_valid(raise_exception=True):
                                        cs_serializers.save()

    def ocr_survey_entry(self, constructed_ocr_json, survey_entry_id):
        try:
            user_obj = Users.objects.filter(id=self.request.user.id).first()
            if not user_obj:
                return {"status": 0, "message": constants.DATA_NOT_FOUND_ERROR_MSG}
            survey_entry_param = {}
            survey_entry_param['household_member_count'] = constructed_ocr_json["household_member_count"]
            survey_entry_param['members'] = constructed_ocr_json["members"]
            survey_entry_param['notes'] = constructed_ocr_json["notes"]
            serializer = SurveyEntryUpdateSerializer(survey_entry_id, data=survey_entry_param, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                if serializer.data:
                    save_status = []
                    survey_entry_id = serializer.data.get('id')
                    if constructed_ocr_json["initial_section"]:
                        initial_section_val = []
                        initial_section_val.append(constructed_ocr_json["initial_section"])
                        self.comman_question_and_answer_create(survey_entry_id, initial_section_val, 'initial_section')
                        save_status.append("initial_section")
                    if constructed_ocr_json["interview_section"]:
                        self.comman_question_and_answer_create(survey_entry_id, constructed_ocr_json["interview_section"],
                                                               'interview_section')
                        save_status.append("interview_section")
                    if constructed_ocr_json["house_hold_member_section"]:
                        self.member_question_and_answer_create(survey_entry_id,
                                                               constructed_ocr_json["house_hold_member_section"],
                                                               'house_hold_member_section')
                        save_status.append("house_hold_member_section")
                    if constructed_ocr_json["final_section"]:
                        self.comman_question_and_answer_create(survey_entry_id, constructed_ocr_json["final_section"],
                                                               'final_section')
                        save_status.append("final_section")
            return serializer.errors
        except Exception as e:
            return e
class OCRThread(threading.Thread):
    def __init__(self, survey_entry_id, request):
        self.survey_entry_id = survey_entry_id
        self.request = request
        threading.Thread.__init__(self, daemon=True)

    def run(self):
        ocr_process = OCRProcess(survey_entry_id=self.survey_entry_id)
        create_ocr_survey = CreateOCRSurveyEntry(request=self.request)
        ocr_process.connect_s3()

        constructed_json = ocr_process.read_image()

        try:
            create_ocr_survey.ocr_survey_entry(constructed_json, self.survey_entry_id)
            OcrMaster.objects.filter(
                survey_entry_id=self.survey_entry_id).update(process_complete=True)
            SurveyEntry.objects.filter(
                id=self.survey_entry_id).update(is_open_ndividual_view=True, ocr_status=constants.OCR_STATUS[4])
        except (OcrMaster.DoesNotExist, SurveyEntry.DoesNotExist):
            pass


def call_ocr_thread(survey_entry_id, request):
    OCRThread(survey_entry_id, request).start()
