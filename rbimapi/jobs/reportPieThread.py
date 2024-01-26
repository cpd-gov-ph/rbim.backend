import json
import threading
import uuid
from bson import json_util
from rbimapi.jobs import reportConstants as constants
from rbimapi.mongoaggregate.survey import mdb_house_hold_member_section_details, mdb_census_static_category_details
from rbim.models import ReportHistory, ReportCategories, SurveyEntry
from rbimapi.jobs import threadConstants, reportPiefunctions


class PieReports:

    def __init__(self, survey_entry_id=None, **kwargs, ):
        self.survey_entry_id = survey_entry_id

    def get_household_members(self):
        survey_id = self.survey_entry_id
        house_hold_member_section_param = {}
        house_hold_member_section_param['match'] = {
            "survey_entry_id": uuid.UUID(f"{survey_id}")
        }
        hs_ = mdb_house_hold_member_section_details(house_hold_member_section_param)

        json_hs = json.dumps(hs_, default=json_util.default)
        final_household_json = json.loads(json_hs)
        final_section_param = {}
        final_section_param['match'] = {
            "survey_entry_id": uuid.UUID(f"{survey_id}"),
            "part": "final_section"
        }
        survey_final_section_details = mdb_census_static_category_details(final_section_param)
        json_final_section = json.dumps(survey_final_section_details, default=json_util.default)
        final_section_json = json.loads(json_final_section)
        self.construct_report_object(survey_id, final_household_json, final_section_json)

    def immunization_constant_construct(self, location_id, category_slug, gender, immunization):
        filter_immunization = ReportHistory.objects.filter(
            location_id=location_id,
            report_category_id__category_slug=category_slug,
        ).first()
        if gender == "Male":
            if len(filter_immunization.chart_unique_constant_left) == 0:
                filter_immunization.chart_unique_constant_left.append(immunization)
                filter_immunization.chart_constant_left.update({f"{immunization}": 1})

                # Excel

                filter_immunization.excel_constant["Male"].update({f"{immunization}": 1})
                filter_immunization.excel_constant["Female"].update({f"{immunization}": 0})
                filter_immunization.excel_constant["Total"].update({f"{immunization}": 1})
                filter_immunization.save()
            else:
                if immunization not in filter_immunization.chart_unique_constant_left:
                    filter_immunization.chart_unique_constant_left.append(immunization)
                    filter_immunization.chart_constant_left.update({f"{immunization}": 1})

                    # Excel

                    filter_immunization.excel_constant["Male"].update({f"{immunization}": 1})
                    filter_immunization.excel_constant["Female"].update({f"{immunization}": 0})
                    filter_immunization.excel_constant["Total"].update({f"{immunization}": 1})
                    filter_immunization.save()
                else:
                    filter_immunization.chart_constant_left[immunization] = \
                        filter_immunization.chart_constant_left[immunization] + 1
                    filter_immunization.excel_constant["Male"][immunization] = \
                        filter_immunization.excel_constant["Male"][immunization] + 1

                    try:
                        filter_immunization.excel_constant["Female"][immunization] += 0
                    except KeyError:
                        filter_immunization.excel_constant["Female"].update({f"{immunization}": 0})
                    filter_immunization.excel_constant["Total"][immunization] = \
                        filter_immunization.excel_constant["Total"][immunization] + 1

                    filter_immunization.save()
        else:
            if len(filter_immunization.chart_unique_constant_right) == 0:
                filter_immunization.chart_unique_constant_right.append(immunization)
                filter_immunization.chart_constant_right.update({f"{immunization}": 1})
                filter_immunization.save()
                # Excel

                filter_immunization.excel_constant["Female"].update({f"{immunization}": 1})
                filter_immunization.excel_constant["Male"].update({f"{immunization}": 0})
                filter_immunization.excel_constant["Total"].update({f"{immunization}": 1})
                filter_immunization.save()
            else:
                if immunization not in filter_immunization.chart_unique_constant_right:
                    filter_immunization.chart_unique_constant_right.append(immunization)
                    filter_immunization.chart_constant_right.update({f"{immunization}": 1})
                    filter_immunization.save()
                    # Excel

                    filter_immunization.excel_constant["Female"].update({f"{immunization}": 1})
                    filter_immunization.excel_constant["Male"].update({f"{immunization}": 0})
                    filter_immunization.excel_constant["Total"].update({f"{immunization}": 1})
                    filter_immunization.save()
                else:
                    filter_immunization.chart_constant_right[immunization] = \
                        filter_immunization.chart_constant_right[immunization] + 1

                    # Excel
                    filter_immunization.excel_constant["Female"][immunization] = \
                        filter_immunization.excel_constant["Female"][immunization] + 1
                    try:
                        filter_immunization.excel_constant["Male"][immunization] += 0
                    except KeyError:
                        filter_immunization.excel_constant["Male"].update({f"{immunization}": 0})
                    filter_immunization.excel_constant["Total"][immunization] = \
                        filter_immunization.excel_constant["Total"][immunization] + 1

                    filter_immunization.save()

    def common_disease_construct(self, location_id, category_slug, common_disease):
        filter_common_disease = ReportHistory.objects.filter(
            location_id=location_id,
            report_category_id__category_slug=category_slug).first()

        if len(filter_common_disease.chart_unique_constant_left) == 0:
            filter_common_disease.chart_unique_constant_left.append(common_disease)
            filter_common_disease.chart_constant_left.update({f"{common_disease}": 1})
            filter_common_disease.save()
        else:
            if common_disease not in filter_common_disease.chart_unique_constant_left:
                filter_common_disease.chart_unique_constant_left.append(common_disease)
                filter_common_disease.chart_constant_left.update({f"{common_disease}": 1})
                filter_common_disease.save()
            else:
                filter_common_disease.chart_constant_left[common_disease] = filter_common_disease.chart_constant_left[
                                                                                common_disease] + 1
                filter_common_disease.save()

    def primary_needs_construct(self, location_id, category_slug, primary_needs):
        filter_primary_needs = ReportHistory.objects.filter(
            location_id=location_id,
            report_category_id__category_slug=category_slug).first()

        if len(filter_primary_needs.chart_unique_constant_left) == 0:
            filter_primary_needs.chart_unique_constant_left.append(primary_needs)
            filter_primary_needs.chart_constant_left.update({f"{primary_needs}": 1})
            filter_primary_needs.save()
        else:
            if primary_needs not in filter_primary_needs.chart_unique_constant_left:
                filter_primary_needs.chart_unique_constant_left.append(primary_needs)
                filter_primary_needs.chart_constant_left.update({f"{primary_needs}": 1})
                filter_primary_needs.save()
            else:
                filter_primary_needs.chart_constant_left[primary_needs] = filter_primary_needs.chart_constant_left[
                                                                              primary_needs] + 1
                filter_primary_needs.save()

    def construct_report_object(self, survey_id, final_household_json, final_section_json):
        family_head = threadConstants.get_family_head(final_household_json)
        total_members_count = len(final_household_json)

        location_id = SurveyEntry.objects.filter(id=survey_id).first().barangay.location.id

        # DISTRIBUTION OF TOTAL POPULATION BY AGE AND SEX
        filter_total_population_by_age_sex_report = ReportHistory.objects.filter(
            location_id=location_id,
            report_category_id__category_slug=constants.CATEGORIES_SLUG[0]).first()

        # DISTRIBUTION OF HOUSEHOLDS BY HOUSEHOLD SIZE AND HH SEX
        filter_headcount_report = ReportHistory.objects.filter(
            location_id=location_id,
            report_category_id__category_slug=constants.CATEGORIES_SLUG[1]).first()

        # DISTRIBUTION OF TOTAL POPULATION BY HIGHEST EDUCATIONAL ATTAINMENT AND SEX
        filter_highest_report = ReportHistory.objects.filter(
            location_id=location_id,
            report_category_id__category_slug=constants.CATEGORIES_SLUG[2]).first()

        # PLACE OF DELIVERY OF POPULATION BY SEX
        filter_delivery_place_report = ReportHistory.objects.filter(
            location_id=location_id,
            report_category_id__category_slug=constants.CATEGORIES_SLUG[10]).first()

        # BIRTH ATTENDANT OF POPULATION BY SEX
        filter_birth_attender_report = ReportHistory.objects.filter(
            location_id=location_id,
            report_category_id__category_slug=constants.CATEGORIES_SLUG[11]).first()

        # final section questions
        common_diseases_ans = threadConstants.get_common_diseases(final_section_json)
        primary_needs_ans = threadConstants.get_primary_need(final_section_json)

        # headcount range
        if total_members_count >= 10:
            filter_headcount_report.chart_constant_left['10'] += 1
        else:
            filter_headcount_report.chart_constant_left[str(total_members_count)] += 1
        filter_headcount_report.save()

        for member_id in range(0, len(final_household_json)):
            member_name = threadConstants.get_member_name(final_household_json, member_id)
            gender_ans = threadConstants.get_member_gender(final_household_json, member_id)
            age_ans = threadConstants.get_member_age(final_household_json, member_id)
            high_education_ans = threadConstants.get_member_higheducation(final_household_json, member_id)
            place_of_delivery_ans = threadConstants.get_member_place_of_delivery(final_household_json, member_id)
            birth_attender_ans = threadConstants.get_member_birth_attendant(final_household_json, member_id)
            immunization_ans = threadConstants.get_member_immunization(final_household_json, member_id)
            age_from_dob = threadConstants.calculate_age(age_ans)

            # family head
            if member_name.strip() == family_head.strip():
                if gender_ans == "Male":
                    filter_headcount_report.chart_constant_right['Male'] += 1
                    # DISTRIBUTION OF HOUSEHOLDS BY HOUSEHOLD SIZE AND HH SEX
                    filter_headcount_report.excel_constant['Male'][str(total_members_count)] += 1


                else:
                    filter_headcount_report.chart_constant_right['Female'] += 1
                    # DISTRIBUTION OF HOUSEHOLDS BY HOUSEHOLD SIZE AND HH SEX
                    filter_headcount_report.excel_constant['Female'][str(total_members_count)] += 1
                filter_headcount_report.save()
            # sex count
            if gender_ans == "Male":
                filter_total_population_by_age_sex_report.excel_constant['Male'][
                    threadConstants.age_range_finder(age_ans)] += 1
                # Excel DISTRIBUTION OF TOTAL POPULATION BY AGE AND SEX
                filter_total_population_by_age_sex_report.chart_constant_left['Male'] += 1
            else:
                filter_total_population_by_age_sex_report.chart_constant_left['Female'] += 1
                # Excel DISTRIBUTION OF TOTAL POPULATION BY AGE AND SEX
                filter_total_population_by_age_sex_report.excel_constant['Female'][
                    threadConstants.age_range_finder(age_ans)] += 1
            # age range
            age_range = threadConstants.age_range_finder(age_ans)
            filter_total_population_by_age_sex_report.chart_constant_right[age_range] = \
                filter_total_population_by_age_sex_report.chart_constant_right[
                    age_range] + 1
            filter_total_population_by_age_sex_report.save()

            if int(age_from_dob) > 5:
                # highest education
                filter_highest_report.chart_constant_left[high_education_ans] = \
                    filter_highest_report.chart_constant_left[
                        high_education_ans] + 1
                # highest education gender
                if gender_ans == "Male":
                    filter_highest_report.chart_constant_right[gender_ans] = \
                        filter_highest_report.chart_constant_right[gender_ans] + 1
                    try:
                        filter_highest_report.excel_constant[gender_ans][high_education_ans][age_range] = \
                            filter_highest_report.excel_constant[gender_ans][high_education_ans][age_range] + 1
                    except:
                        filter_highest_report.excel_constant[gender_ans][high_education_ans]['65'] = \
                            filter_highest_report.excel_constant[gender_ans][high_education_ans]['65'] + 1
                if gender_ans == "Female":
                    filter_highest_report.chart_constant_right[gender_ans] = \
                        filter_highest_report.chart_constant_right[gender_ans] + 1
                    try:
                        filter_highest_report.excel_constant[gender_ans][high_education_ans][age_range] = \
                            filter_highest_report.excel_constant[gender_ans][high_education_ans][age_range] + 1
                    except:
                        filter_highest_report.excel_constant[gender_ans][high_education_ans]['65'] = \
                            filter_highest_report.excel_constant[gender_ans][high_education_ans]['65'] + 1

                filter_highest_report.save()

            if int(age_from_dob) == 0:
                immunization_ = immunization_ans.strip().title()
                # immunization validator
                self.immunization_constant_construct(location_id, constants.CATEGORIES_SLUG[12], gender_ans,
                                                     immunization_)
                # place of delivery and attendant
                if gender_ans == "Male":
                    filter_delivery_place_report.chart_constant_left[place_of_delivery_ans] = \
                        filter_delivery_place_report.chart_constant_left[place_of_delivery_ans] + 1
                    filter_birth_attender_report.chart_constant_left[birth_attender_ans] = \
                        filter_birth_attender_report.chart_constant_left[birth_attender_ans] + 1
                    # Excel PLACE OF DELIVERY OF POPULATION BY SEX (AGE 0-11)
                    filter_delivery_place_report.excel_constant["Male"][place_of_delivery_ans] = \
                        filter_delivery_place_report.excel_constant["Male"][place_of_delivery_ans] + 1
                    filter_birth_attender_report.excel_constant["Male"][birth_attender_ans] = \
                        filter_birth_attender_report.excel_constant["Male"][birth_attender_ans] + 1
                if gender_ans == "Female":
                    filter_delivery_place_report.chart_constant_right[place_of_delivery_ans] = \
                        filter_delivery_place_report.chart_constant_right[place_of_delivery_ans] + 1
                    filter_birth_attender_report.chart_constant_right[birth_attender_ans] = \
                        filter_birth_attender_report.chart_constant_right[birth_attender_ans] + 1
                    # Excel PLACE OF DELIVERY OF POPULATION BY SEX (AGE 0-11)
                    filter_delivery_place_report.excel_constant["Female"][place_of_delivery_ans] = \
                        filter_delivery_place_report.excel_constant["Female"][place_of_delivery_ans] + 1
                    filter_birth_attender_report.excel_constant["Female"][birth_attender_ans] = \
                        filter_birth_attender_report.excel_constant["Female"][birth_attender_ans] + 1

                filter_delivery_place_report.excel_constant["Total"][place_of_delivery_ans] = \
                    filter_delivery_place_report.excel_constant["Total"][place_of_delivery_ans] + 1
                filter_birth_attender_report.excel_constant["Total"][birth_attender_ans] = \
                    filter_birth_attender_report.excel_constant["Total"][birth_attender_ans] + 1

                filter_delivery_place_report.save()
                filter_birth_attender_report.save()

        # common diseases
        self.common_disease_construct(location_id, constants.CATEGORIES_SLUG[16], common_diseases_ans)
        self.primary_needs_construct(location_id, constants.CATEGORIES_SLUG[17], primary_needs_ans)

        # Total Population
        total_population = filter_total_population_by_age_sex_report.chart_constant_left['Male'] + \
                           filter_total_population_by_age_sex_report.chart_constant_left[
                               'Female']

        # Calling Saving to DB functions
        reportPiefunctions.report_total_population_by_age_sex(location_id, total_population)
        reportPiefunctions.report_household_head_size_sex(location_id, total_population)
        reportPiefunctions.report_highest_education_attainment(location_id, total_population)
        reportPiefunctions.report_place_of_delivery(location_id, total_population)
        reportPiefunctions.report_birth_attendant(location_id, total_population)
        reportPiefunctions.report_immunization_by_sex(location_id, total_population)
        reportPiefunctions.report_common_disease_cause_death(location_id, total_population)
        reportPiefunctions.report_primary_need_in_barangay(location_id, total_population)
