import json
import uuid
from bson import json_util
from rbimapi.jobs import reportConstants as constants
from rbimapi.mongoaggregate.survey import mdb_house_hold_member_section_details, mdb_census_static_category_details
from rbim.models import ReportHistory, ReportCategories, SurveyEntry
from rbimapi.jobs import threadConstants, reportBarfunctions


class BarReports:
    def __init__(self, survey_entry_id=None, **kwargs, ):
        self.survey_entry_id = survey_entry_id

    def ethnic_constant_construct(self, location_id, category_slug, gender, ethnic):
        filter_ethnic_report = ReportHistory.objects.filter(
            location_id=location_id,
            report_category_id__category_slug=category_slug,
        ).first()
        if gender == "Male":
            if len(filter_ethnic_report.chart_unique_constant_left) == 0:
                filter_ethnic_report.chart_unique_constant_left.append(ethnic)
                filter_ethnic_report.chart_constant_left.update({f"{ethnic}": 1})

                # Excel
                filter_ethnic_report.excel_constant["Male"].update({f"{ethnic}": 1})
                try:
                    filter_ethnic_report.excel_constant["Female"][ethnic] += 0
                except KeyError:
                    filter_ethnic_report.excel_constant["Female"].update({f"{ethnic}": 0})
                filter_ethnic_report.save()
            else:
                if ethnic not in filter_ethnic_report.chart_unique_constant_left:
                    filter_ethnic_report.chart_unique_constant_left.append(ethnic)
                    filter_ethnic_report.chart_constant_left.update({f"{ethnic}": 1})

                    # Excel
                    filter_ethnic_report.excel_constant["Male"].update({f"{ethnic}": 1})
                    try:
                        filter_ethnic_report.excel_constant["Female"][ethnic] += 0
                    except KeyError:
                        filter_ethnic_report.excel_constant["Female"].update({f"{ethnic}": 0})
                    filter_ethnic_report.save()
                else:
                    filter_ethnic_report.chart_constant_left[ethnic] = \
                        filter_ethnic_report.chart_constant_left[ethnic] + 1
                    filter_ethnic_report.excel_constant["Male"][ethnic] = \
                        filter_ethnic_report.excel_constant["Male"][ethnic] + 1

                    # Excel
                    try:
                        filter_ethnic_report.excel_constant["Female"][ethnic] += 0
                    except KeyError:
                        filter_ethnic_report.excel_constant["Female"].update({f"{ethnic}": 0})
                    filter_ethnic_report.save()
        else:
            if len(filter_ethnic_report.chart_unique_constant_right) == 0:
                filter_ethnic_report.chart_unique_constant_right.append(ethnic)
                filter_ethnic_report.chart_constant_right.update({f"{ethnic}": 1})
                filter_ethnic_report.save()

                # Excel
                filter_ethnic_report.excel_constant["Female"].update({f"{ethnic}": 1})
                try:
                    filter_ethnic_report.excel_constant["Male"][ethnic] += 0
                except KeyError:
                    filter_ethnic_report.excel_constant["Male"].update({f"{ethnic}": 0})
                filter_ethnic_report.save()
            else:
                if ethnic not in filter_ethnic_report.chart_unique_constant_right:
                    filter_ethnic_report.chart_unique_constant_right.append(ethnic)
                    filter_ethnic_report.chart_constant_right.update({f"{ethnic}": 1})
                    filter_ethnic_report.save()
                    # Excel
                    filter_ethnic_report.excel_constant["Female"].update({f"{ethnic}": 1})
                    try:
                        filter_ethnic_report.excel_constant["Male"][ethnic] += 0
                    except KeyError:
                        filter_ethnic_report.excel_constant["Male"].update({f"{ethnic}": 0})
                    filter_ethnic_report.save()
                else:
                    filter_ethnic_report.chart_constant_right[ethnic] = \
                        filter_ethnic_report.chart_constant_right[ethnic] + 1

                    # Excel
                    filter_ethnic_report.excel_constant["Female"][ethnic] = \
                        filter_ethnic_report.excel_constant["Female"][ethnic] + 1
                    try:
                        filter_ethnic_report.excel_constant["Male"][ethnic] += 0
                    except KeyError:
                        filter_ethnic_report.excel_constant["Male"].update({f"{ethnic}": 0})
                    filter_ethnic_report.save()

    def get_household_members(self):
        survey_id = self.survey_entry_id
        house_hold_member_section_param = {}
        house_hold_member_section_param['match'] = {
            "survey_entry_id": uuid.UUID(f"{survey_id}")
        }
        hs_ = mdb_house_hold_member_section_details(house_hold_member_section_param)

        json_hs = json.dumps(hs_, default=json_util.default)
        final_household_json = json.loads(json_hs)
        self.construct_report_object(survey_id, final_household_json)

    def construct_report_object(self, survey_id, final_household_json):
        location_id = SurveyEntry.objects.filter(id=survey_id).first().barangay.location.id

        # DISTRIBUTION OF TOTAL POPULATION BY AGE AND SEX
        filter_total_population_by_age_sex_report = ReportHistory.objects.filter(
            location_id=location_id,
            report_category_id__category_slug=constants.CATEGORIES_SLUG[0]).first()

        filter_marital_status_by_age = ReportHistory.objects.filter(
            location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[3]).first()

        filter_marital_status_by_gender = ReportHistory.objects.filter(
            location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[4]).first()

        filter_religion_report = ReportHistory.objects.filter(
            location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[5]).first()
        
        filter_source_of_income_by_age = ReportHistory.objects.filter(
            location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[8]).first()

        filter_salary_by_age = ReportHistory.objects.filter(
            location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[7]).first()

        filter_preganancy_count = ReportHistory.objects.filter(
            location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[13]).first()

        filter_status_of_work_by_age = ReportHistory.objects.filter(
            location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[9]).first()

        filter_school_level_by_age = ReportHistory.objects.filter(
            location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[14]).first()

        filter_school_type_by_age = ReportHistory.objects.filter(
            location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[15]).first()

        for member_id in range(0, len(final_household_json)):
            gender_ans = threadConstants.get_member_gender(final_household_json, member_id)
            age_ans = threadConstants.get_member_age(final_household_json, member_id)
            marital_status_ans = threadConstants.get_member_marital_status(final_household_json, member_id)
            religion_ans = threadConstants.get_member_religion(final_household_json, member_id)
            ethnic_ans = threadConstants.get_member_ethnic(final_household_json, member_id)
            salary_ans = threadConstants.get_member_salary(final_household_json, member_id)
            age_range = threadConstants.age_range_finder(age_ans)
            preganancy_count_ans = threadConstants.get_member_preganancy_count(final_household_json, member_id)

            source_of_income_ans = threadConstants.get_member_source_of_income(final_household_json, member_id)
            status_of_work_ans = threadConstants.get_member_status_of_work(final_household_json, member_id)
            school_level_ans = threadConstants.get_member_school_level(final_household_json, member_id)
            school_type_ans = threadConstants.get_member_school_type(final_household_json, member_id)
            age_from_dob = threadConstants.calculate_age(age_ans)
            # MARITAL STATUS OF THE TOTAL POPULATION BY AGE
            filter_marital_status_by_age.chart_constant_left[marital_status_ans][age_range] = \
                filter_marital_status_by_age.chart_constant_left[marital_status_ans][age_range] + 1
            filter_marital_status_by_age.save()

            # MARITAL STATUS OF THE TOTAL POPULATION BY SEX
            filter_marital_status_by_gender.chart_constant_left[gender_ans][marital_status_ans][age_range] = \
                filter_marital_status_by_gender.chart_constant_left[gender_ans][marital_status_ans][age_range] + 1

            filter_marital_status_by_gender.excel_constant[gender_ans][marital_status_ans] = \
                filter_marital_status_by_gender.excel_constant[gender_ans][marital_status_ans] + 1
            filter_marital_status_by_gender.save()

            # RELIGIOUS AFFLIATION OF THE TOTAL POPULATION BY SEX            
            filter_religion_report.chart_constant_left[gender_ans][religion_ans] = \
                filter_religion_report.chart_constant_left[gender_ans][religion_ans] + 1

            filter_religion_report.excel_constant[gender_ans][religion_ans] = \
                filter_religion_report.excel_constant[gender_ans][religion_ans] + 1
            filter_religion_report.save()

            # ETHNIC GROUPING OF TOTAL POPULATION BY SEX
            self.ethnic_constant_construct(location_id=location_id, category_slug=constants.CATEGORIES_SLUG[6],
                                           gender=gender_ans, ethnic=ethnic_ans)

            # MONTHLY INCOME OF THE TOTAL POPULATION (15+) BY AGE AND SEX
            if int(age_from_dob) >= 15 and salary_ans is not None:
                salary_range = threadConstants.salary_range_finder(int(salary_ans))
                filter_salary_by_age.chart_constant_left[gender_ans][salary_range][age_range] = \
                    filter_salary_by_age.chart_constant_left[gender_ans][salary_range][age_range] + 1
                filter_salary_by_age.save()

                # MAJOR SOURCE OF INCOME OF THE TOTAL POPULATION (15+) BY AGE AND SEX
                filter_source_of_income_by_age.chart_constant_left[gender_ans][source_of_income_ans][age_range] = \
                    filter_source_of_income_by_age.chart_constant_left[gender_ans][source_of_income_ans][age_range] + 1
                filter_source_of_income_by_age.save()

                # STATUS OF WORK/ BUSINESS OF THE TOTAL POPULATION (15+) BY AGE AND SEX
                filter_status_of_work_by_age.chart_constant_left[gender_ans][status_of_work_ans][age_range] = \
                    filter_status_of_work_by_age.chart_constant_left[gender_ans][status_of_work_ans][age_range] + 1
                filter_status_of_work_by_age.save()
            # PREGNANCIES OF POPULATION (WOMEN 10-54) BY AGE AND  GRAVIDA
            if int(age_from_dob) >= 10 and gender_ans == "Female" and preganancy_count_ans is not None:
                preganancy_range_finder = threadConstants.preganancy_range_finder(int(preganancy_count_ans))
                try:
                    filter_preganancy_count.chart_constant_left[gender_ans][preganancy_range_finder][age_range] = \
                        filter_preganancy_count.chart_constant_left[gender_ans][preganancy_range_finder][age_range] + 1
                except:
                    filter_preganancy_count.chart_constant_left[gender_ans][preganancy_range_finder]['50-54'] = \
                        filter_preganancy_count.chart_constant_left[gender_ans][preganancy_range_finder]['50-54'] + 1
                filter_preganancy_count.save()

            if int(age_from_dob) >= 3 and int(age_from_dob) <= 24:
                schl_level_age_range = threadConstants.age_range_finder_school(age_ans)
                # CURRENTLY ENROLLED BY AGE, SEX AND SCHOOL LEVEL
                filter_school_level_by_age.chart_constant_left[gender_ans][school_level_ans][schl_level_age_range] = \
                    filter_school_level_by_age.chart_constant_left[gender_ans][school_level_ans][
                        schl_level_age_range] + 1
                filter_school_level_by_age.save()

                # CURRENTLY ENROLLED BY AGE, SEX AND SCHOOL TYPE
                schl_type_finder = threadConstants.school_type_finder(school_type_ans)
                filter_school_type_by_age.chart_constant_left[gender_ans][schl_type_finder][schl_level_age_range] = \
                    filter_school_type_by_age.chart_constant_left[gender_ans][schl_type_finder][
                        schl_level_age_range] + 1
                filter_school_type_by_age.save()

        total_population = filter_total_population_by_age_sex_report.chart_constant_left["Male"] + \
                           filter_total_population_by_age_sex_report.chart_constant_left["Female"]

        # Calling Saving to DB functions
        reportBarfunctions.report_marital_status_by_age(location_id, total_population)
        reportBarfunctions.report_marital_status_by_sex(location_id, total_population)
        reportBarfunctions.report_religion_by_sex(location_id, total_population)
        reportBarfunctions.report_ethnic_by_sex(location_id, total_population)
        reportBarfunctions.report_monthly_income_by_age_sex(location_id, total_population)
        reportBarfunctions.report_source_of_income_by_age(location_id, total_population)
        reportBarfunctions.report_status_of_work_by_age(location_id, total_population)
        reportBarfunctions.report_preganancy_count(location_id)
        reportBarfunctions.report_school_level_by_age(location_id)
        reportBarfunctions.report_currently_enrolled_school_type_by_age(location_id)
