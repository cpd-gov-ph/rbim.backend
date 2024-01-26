from rbim.models import ReportHistory
from rbimapi.jobs import reportConstants as constants


def report_total_population_by_age_sex(location_id, total_population):
    # DISTRIBUTION OF TOTAL POPULATION BY AGE AND SEX

    filter_total_population_by_age_sex_report = ReportHistory.objects.filter(
        location_id=location_id,
        report_category_id__category_slug=constants.CATEGORIES_SLUG[0]).first()

    gender_male_data = list(dict(filter_total_population_by_age_sex_report.chart_constant_left).values())
    filter_total_population_by_age_sex_report.chart_response_left['datasets'][0]['data'] = gender_male_data
    filter_total_population_by_age_sex_report.chart_response_left['datasets'][0][
        'backgroundColor'] = constants.CHART_BACKGROUND_COLOR[:len(gender_male_data)]
    filter_total_population_by_age_sex_report.chart_response_left['datasets'][0]['total_population'] = total_population

    gender_female_data = list(dict(filter_total_population_by_age_sex_report.chart_constant_right).values())
    filter_total_population_by_age_sex_report.chart_response_right['datasets'][0]['data'] = gender_female_data
    filter_total_population_by_age_sex_report.chart_response_right['datasets'][0][
        'backgroundColor'] = constants.CHART_BACKGROUND_COLOR[:len(gender_female_data)]
    filter_total_population_by_age_sex_report.chart_response_right['datasets'][0]['total_population'] = total_population

    # Excel
    excel_male_data = list(dict(filter_total_population_by_age_sex_report.excel_constant['Male']).values())
    excel_female_data = list(dict(filter_total_population_by_age_sex_report.excel_constant['Female']).values())
    filter_total_population_by_age_sex_report.excel_response["Male"] = excel_male_data
    filter_total_population_by_age_sex_report.excel_response["Female"] = excel_female_data
    filter_total_population_by_age_sex_report.excel_response["Male"].append(sum(excel_male_data))
    filter_total_population_by_age_sex_report.excel_response["Female"].append(sum(excel_female_data))
    filter_total_population_by_age_sex_report.save()


def report_household_head_size_sex(location_id, total_population):
    # DISTRIBUTION OF HOUSEHOLDS BY HOUSEHOLD SIZE AND HH SEX
    filter_headcount_report = ReportHistory.objects.filter(
        location_id=location_id,
        report_category_id__category_slug=constants.CATEGORIES_SLUG[1]).first()

    headcount_data = list(dict(filter_headcount_report.chart_constant_left).values())
    filter_headcount_report.chart_response_left['datasets'][0]['data'] = headcount_data
    filter_headcount_report.chart_response_left['datasets'][0][
        'backgroundColor'] = constants.CHART_BACKGROUND_COLOR[:len(headcount_data)]
    filter_headcount_report.chart_response_left['datasets'][0]['total_population'] = total_population

    headcount_data = list(dict(filter_headcount_report.chart_constant_right).values())
    filter_headcount_report.chart_response_right['datasets'][0]['data'] = headcount_data
    filter_headcount_report.chart_response_right['datasets'][0][
        'backgroundColor'] = constants.CHART_BACKGROUND_COLOR[:len(headcount_data)]
    filter_headcount_report.chart_response_right['datasets'][0]['total_population'] = total_population

    # Excel
    hcount_data_excel_male_data = list(dict(filter_headcount_report.excel_constant['Male']).values())
    hcount_data_excel_female_data = list(dict(filter_headcount_report.excel_constant['Female']).values())
    filter_headcount_report.excel_response["Male"] = hcount_data_excel_male_data
    filter_headcount_report.excel_response["Female"] = hcount_data_excel_female_data
    filter_headcount_report.excel_response["Male"].append(sum(hcount_data_excel_male_data))
    filter_headcount_report.excel_response["Female"].append(sum(hcount_data_excel_female_data))
    filter_headcount_report.save()


def report_highest_education_attainment(location_id, total_population):
    # DISTRIBUTION OF TOTAL POPULATION BY HIGHEST EDUCATIONAL ATTAINMENT AND SEX

    filter_highest_report = ReportHistory.objects.filter(
        location_id=location_id,
        report_category_id__category_slug=constants.CATEGORIES_SLUG[2]).first()
    highest_education_data = list(dict(filter_highest_report.chart_constant_left).values())
    filter_highest_report.chart_response_left['datasets'][0]['data'] = highest_education_data
    filter_highest_report.chart_response_left['datasets'][0]['backgroundColor'] = constants.CHART_BACKGROUND_COLOR[
                                                                                  :len(highest_education_data)]
    filter_highest_report.chart_response_left['datasets'][0]['total_population'] = total_population
    filter_highest_report.save()
    highest_education_gender_data = list(dict(filter_highest_report.chart_constant_right).values())
    filter_highest_report.chart_response_right['datasets'][0]['data'] = highest_education_gender_data
    filter_highest_report.chart_response_right['datasets'][0]['backgroundColor'] = constants.CHART_BACKGROUND_COLOR[
                                                                                   :len(
                                                                                       highest_education_gender_data)]
    filter_highest_report.chart_response_right['datasets'][0]['total_population'] = total_population

    # Excel
    m_no_education_data = list(dict(filter_highest_report.excel_constant["Male"]["No education"]).values())
    m_pre_school_data = list(dict(filter_highest_report.excel_constant["Male"]["Pre-school"]).values())
    m_elementary_l_data = list(dict(filter_highest_report.excel_constant["Male"]["Elementary level"]).values())
    m_elementary_g_data = list(dict(filter_highest_report.excel_constant["Male"]["Elementary graduate"]).values())
    m_hs_g_data = list(dict(filter_highest_report.excel_constant["Male"]["High school graduate"]).values())
    m_hs_l_data = list(dict(filter_highest_report.excel_constant["Male"]["High school level"]).values())
    m_jhs_data = list(dict(filter_highest_report.excel_constant["Male"]["Junior HS"]).values())
    m_jhsg_data = list(dict(filter_highest_report.excel_constant["Male"]["Junior HS graduate"]).values())
    m_shs_data = list(dict(filter_highest_report.excel_constant["Male"]["Senior HS level"]).values())
    m_shsg_data = list(dict(filter_highest_report.excel_constant["Male"]["Senior HS graduate"]).values())
    m_vt_data = list(dict(filter_highest_report.excel_constant["Male"]["Vocational/Tech"]).values())
    m_cl_data = list(dict(filter_highest_report.excel_constant["Male"]["College level"]).values())
    m_cg_data = list(dict(filter_highest_report.excel_constant["Male"]["College graduate"]).values())
    m_pg_data = list(dict(filter_highest_report.excel_constant["Male"]["Post-graduate"]).values())

    f_no_education_data = list(dict(filter_highest_report.excel_constant["Female"]["No education"]).values())
    f_pre_school_data = list(dict(filter_highest_report.excel_constant["Female"]["Pre-school"]).values())
    f_elementary_l_data = list(dict(filter_highest_report.excel_constant["Female"]["Elementary level"]).values())
    f_elementary_g_data = list(dict(filter_highest_report.excel_constant["Female"]["Elementary graduate"]).values())
    f_hs_l_data = list(dict(filter_highest_report.excel_constant["Female"]["High school level"]).values())
    f_hs_g_data = list(dict(filter_highest_report.excel_constant["Female"]["High school graduate"]).values())
    f_jhs_data = list(dict(filter_highest_report.excel_constant["Female"]["Junior HS"]).values())
    f_jhsg_data = list(dict(filter_highest_report.excel_constant["Female"]["Junior HS graduate"]).values())
    f_shs_data = list(dict(filter_highest_report.excel_constant["Female"]["Senior HS level"]).values())
    f_shsg_data = list(dict(filter_highest_report.excel_constant["Female"]["Senior HS graduate"]).values())
    f_vt_data = list(dict(filter_highest_report.excel_constant["Female"]["Vocational/Tech"]).values())
    f_cl_data = list(dict(filter_highest_report.excel_constant["Female"]["College level"]).values())
    f_cg_data = list(dict(filter_highest_report.excel_constant["Female"]["College graduate"]).values())
    f_pg_data = list(dict(filter_highest_report.excel_constant["Female"]["Post-graduate"]).values())

    # Male
    filter_highest_report.excel_response['Male_No_education'] = m_no_education_data
    filter_highest_report.excel_response['Male_No_education'].append(sum(m_no_education_data))
    filter_highest_report.excel_response['Male_Pre-school'] = m_pre_school_data
    filter_highest_report.excel_response['Male_Pre-school'].append(sum(m_pre_school_data))
    filter_highest_report.excel_response['Male_Elementary_level'] = m_elementary_l_data
    filter_highest_report.excel_response['Male_Elementary_level'].append(sum(m_elementary_l_data))
    filter_highest_report.excel_response['Male_Elementary_graduate'] = m_elementary_g_data
    filter_highest_report.excel_response['Male_Elementary_graduate'].append(sum(m_elementary_g_data))
    filter_highest_report.excel_response['Male_High_school_level'] = m_hs_l_data
    filter_highest_report.excel_response['Male_High_school_level'].append(sum(m_hs_l_data))
    filter_highest_report.excel_response['Male_High_school_graduate'] = m_hs_g_data
    filter_highest_report.excel_response['Male_High_school_graduate'].append(sum(m_hs_g_data))
    filter_highest_report.excel_response['Male_Junior_HS'] = m_jhs_data
    filter_highest_report.excel_response['Male_Junior_HS'].append(sum(m_jhs_data))
    filter_highest_report.excel_response['Male_Junior_HS_graduate'] = m_jhsg_data
    filter_highest_report.excel_response['Male_Junior_HS_graduate'].append(sum(m_jhsg_data))
    filter_highest_report.excel_response['Male_Senior_HS_level'] = m_shs_data
    filter_highest_report.excel_response['Male_Senior_HS_level'].append(sum(m_shsg_data))
    filter_highest_report.excel_response['Male_Senior_HS_graduate'] = m_shsg_data
    filter_highest_report.excel_response['Male_Senior_HS_graduate'].append(sum(m_shsg_data))
    filter_highest_report.excel_response['Male_Vocational/Tech'] = m_vt_data
    filter_highest_report.excel_response['Male_Vocational/Tech'].append(sum(m_vt_data))
    filter_highest_report.excel_response['Male_College_level'] = m_cl_data
    filter_highest_report.excel_response['Male_College_level'].append(sum(m_cl_data))
    filter_highest_report.excel_response['Male_College_graduate'] = m_cg_data
    filter_highest_report.excel_response['Male_College_graduate'].append(sum(m_cg_data))
    filter_highest_report.excel_response['Male_Post-graduate'] = m_pg_data
    filter_highest_report.excel_response['Male_Post-graduate'].append(sum(m_pg_data))

    # Female
    filter_highest_report.excel_response['Female_No_education'] = f_no_education_data
    filter_highest_report.excel_response['Female_No_education'].append(sum(f_no_education_data))
    filter_highest_report.excel_response['Female_Pre-school'] = f_pre_school_data
    filter_highest_report.excel_response['Female_Pre-school'].append(sum(f_pre_school_data))
    filter_highest_report.excel_response['Female_Elementary_level'] = f_elementary_l_data
    filter_highest_report.excel_response['Female_Elementary_level'].append(sum(f_elementary_l_data))
    filter_highest_report.excel_response['Female_Elementary_graduate'] = f_elementary_g_data
    filter_highest_report.excel_response['Female_Elementary_graduate'].append(sum(f_elementary_g_data))
    filter_highest_report.excel_response['Female_High_school_level'] = f_hs_l_data
    filter_highest_report.excel_response['Female_High_school_level'].append(sum(f_hs_l_data))
    filter_highest_report.excel_response['Female_High_school_graduate'] = f_hs_g_data
    filter_highest_report.excel_response['Female_High_school_graduate'].append(sum(f_hs_g_data))
    filter_highest_report.excel_response['Female_Junior_HS'] = f_jhs_data
    filter_highest_report.excel_response['Female_Junior_HS'].append(sum(f_jhs_data))
    filter_highest_report.excel_response['Female_Junior_HS_graduate'] = f_jhsg_data
    filter_highest_report.excel_response['Female_Junior_HS_graduate'].append(sum(f_jhsg_data))
    filter_highest_report.excel_response['Female_Senior_HS_level'] = f_shs_data
    filter_highest_report.excel_response['Female_Senior_HS_level'].append(sum(f_shsg_data))
    filter_highest_report.excel_response['Female_Senior_HS_graduate'] = f_shsg_data
    filter_highest_report.excel_response['Female_Senior_HS_graduate'].append(sum(f_shsg_data))
    filter_highest_report.excel_response['Female_Vocational/Tech'] = f_vt_data
    filter_highest_report.excel_response['Female_Vocational/Tech'].append(sum(f_vt_data))
    filter_highest_report.excel_response['Female_College_level'] = f_cl_data
    filter_highest_report.excel_response['Female_College_level'].append(sum(f_cl_data))
    filter_highest_report.excel_response['Female_College_graduate'] = f_cg_data
    filter_highest_report.excel_response['Female_College_graduate'].append(sum(f_cg_data))
    filter_highest_report.excel_response['Female_Post-graduate'] = f_pg_data
    filter_highest_report.excel_response['Female_Post-graduate'].append(sum(f_pg_data))

    filter_highest_report.save()


def report_place_of_delivery(location_id, total_population):
    # PLACE OF DELIVERY OF POPULATION BY SEX

    filter_delivery_place_report = ReportHistory.objects.filter(
        location_id=location_id,
        report_category_id__category_slug=constants.CATEGORIES_SLUG[10]).first()

    # Male
    delivery_place_male_data = list(dict(filter_delivery_place_report.chart_constant_left).values())
    filter_delivery_place_report.chart_response_left['datasets'][0]['data'] = delivery_place_male_data
    filter_delivery_place_report.chart_response_left['datasets'][0][
        'backgroundColor'] = constants.CHART_BACKGROUND_COLOR[:len(delivery_place_male_data)]
    filter_delivery_place_report.chart_response_left['datasets'][0]['total_population'] = total_population
    # Female
    delivery_place_female_data = list(dict(filter_delivery_place_report.chart_constant_right).values())
    filter_delivery_place_report.chart_response_right['datasets'][0]['data'] = delivery_place_female_data
    filter_delivery_place_report.chart_response_right['datasets'][0][
        'backgroundColor'] = constants.CHART_BACKGROUND_COLOR[:len(delivery_place_female_data)]
    filter_delivery_place_report.chart_response_right['datasets'][0]['total_population'] = total_population

    # Excel
    delivery_place_excel_male_data = list(dict(filter_delivery_place_report.excel_constant['Male']).values())
    delivery_place_excel_female_data = list(dict(filter_delivery_place_report.excel_constant['Female']).values())
    delivery_place_excel_total = list(dict(filter_delivery_place_report.excel_constant['Total']).values())
    male_total = sum(delivery_place_excel_male_data)
    female_total = sum(delivery_place_excel_female_data)
    total = sum(delivery_place_excel_total)
    filter_delivery_place_report.excel_response["Male"] = delivery_place_excel_male_data
    filter_delivery_place_report.excel_response["Female"] = delivery_place_excel_female_data
    filter_delivery_place_report.excel_response["Total"] = delivery_place_excel_total
    filter_delivery_place_report.excel_response["Male"].append(male_total)
    filter_delivery_place_report.excel_response["Female"].append(female_total)
    filter_delivery_place_report.excel_response["Total"].append(total)
    filter_delivery_place_report.save()


def report_birth_attendant(location_id, total_population):
    # BIRTH ATTENDANT OF POPULATION BY SEX

    filter_birth_attender_report = ReportHistory.objects.filter(
        location_id=location_id,
        report_category_id__category_slug=constants.CATEGORIES_SLUG[11]).first()

    # Male
    delivery_attender_male_data = list(dict(filter_birth_attender_report.chart_constant_left).values())
    filter_birth_attender_report.chart_response_left['datasets'][0]['data'] = delivery_attender_male_data
    filter_birth_attender_report.chart_response_left['datasets'][0][
        'backgroundColor'] = constants.CHART_BACKGROUND_COLOR[:len(delivery_attender_male_data)]
    filter_birth_attender_report.chart_response_left['datasets'][0]['total_population'] = total_population
    # Female
    delivery_attender_female_data = list(dict(filter_birth_attender_report.chart_constant_right).values())
    filter_birth_attender_report.chart_response_right['datasets'][0]['data'] = delivery_attender_female_data
    filter_birth_attender_report.chart_response_right['datasets'][0][
        'backgroundColor'] = constants.CHART_BACKGROUND_COLOR[:len(delivery_attender_female_data)]
    filter_birth_attender_report.chart_response_right['datasets'][0]['total_population'] = total_population

    # Excel
    delivery_attender_excel_male_data = list(dict(filter_birth_attender_report.excel_constant['Male']).values())
    delivery_attender_excel_female_data = list(dict(filter_birth_attender_report.excel_constant['Female']).values())
    delivery_attender_excel_total = list(dict(filter_birth_attender_report.excel_constant['Total']).values())
    male_total = sum(delivery_attender_excel_male_data)
    female_total = sum(delivery_attender_excel_female_data)
    total = sum(delivery_attender_excel_total)
    filter_birth_attender_report.excel_response["Male"] = delivery_attender_excel_male_data
    filter_birth_attender_report.excel_response["Female"] = delivery_attender_excel_female_data
    filter_birth_attender_report.excel_response["Total"] = delivery_attender_excel_total
    filter_birth_attender_report.excel_response["Male"].append(male_total)
    filter_birth_attender_report.excel_response["Female"].append(female_total)
    filter_birth_attender_report.excel_response["Total"].append(total)
    filter_birth_attender_report.save()


def report_immunization_by_sex(location_id, total_population):
    # IMMUNIZATION OF POPULATION BY SEX

    filter_immunization_report = ReportHistory.objects.filter(
        location_id=location_id,
        report_category_id__category_slug=constants.CATEGORIES_SLUG[12]).first()

    # Male
    immunization_male_data = list(dict(filter_immunization_report.chart_constant_left).values())
    immunization_male_labels = list(dict(filter_immunization_report.chart_constant_left).keys())
    if len(immunization_male_data) == 0:
        immunization_male_data = [0]
        immunization_male_labels = [""]
    filter_immunization_report.chart_response_left['datasets'][0]['data'] = immunization_male_data
    filter_immunization_report.chart_response_left['datasets'][0][
        'backgroundColor'] = constants.CHART_BACKGROUND_COLOR[:len(immunization_male_data)]
    filter_immunization_report.chart_response_left['labels'] = immunization_male_labels
    filter_immunization_report.chart_response_left['datasets'][0]['total_population'] = total_population

    # Female
    immunization_female_data = list(dict(filter_immunization_report.chart_constant_right).values())
    immunization_female_labels = list(dict(filter_immunization_report.chart_constant_right).keys())
    if len(immunization_female_data) == 0:
        immunization_female_data = [0]
        immunization_female_labels = [""]
    filter_immunization_report.chart_response_right['datasets'][0]['data'] = immunization_female_data
    filter_immunization_report.chart_response_right['datasets'][0][
        'backgroundColor'] = constants.CHART_BACKGROUND_COLOR[:len(immunization_female_data)]
    filter_immunization_report.chart_response_right['labels'] = immunization_female_labels
    filter_immunization_report.chart_response_right['datasets'][0]['total_population'] = total_population


    # Excel
    immunization_excel_male_data = list(dict(filter_immunization_report.excel_constant['Male']).values())
    merge_unique_constant = filter_immunization_report.chart_unique_constant_right + filter_immunization_report.chart_unique_constant_left
    immunization_excel_immunization_data = list(set(merge_unique_constant))
    immunization_excel_female_data = list(dict(filter_immunization_report.excel_constant['Female']).values())
    immunization_excel_total = list(dict(filter_immunization_report.excel_constant['Total']).values())
    filter_immunization_report.excel_response["Immunization"] = immunization_excel_immunization_data
    filter_immunization_report.excel_response["Male"] = immunization_excel_male_data
    filter_immunization_report.excel_response["Female"] = immunization_excel_female_data
    filter_immunization_report.excel_response["Total"] = immunization_excel_total
    filter_immunization_report.save()


def report_common_disease_cause_death(location_id, total_population):
    # COMMOM DISEASE CAUSED DEATH IN THE BARANGAY

    filter_common_diseases = ReportHistory.objects.filter(
        location_id=location_id,
        report_category_id__category_slug=constants.CATEGORIES_SLUG[16]).first()

    common_diseases_data = list(dict(filter_common_diseases.chart_constant_left).values())
    common_diseases_labels = list(dict(filter_common_diseases.chart_constant_left).keys())
    filter_common_diseases.chart_response_left['datasets'][0]['data'] = common_diseases_data
    filter_common_diseases.chart_response_left['datasets'][0]['backgroundColor'] = constants.CHART_BACKGROUND_COLOR[
                                                                                   :len(common_diseases_data)]
    filter_common_diseases.chart_response_left['datasets'][0]['total_population'] = total_population

    filter_common_diseases.chart_response_left['labels'] = common_diseases_labels


    # Excel
    filter_common_diseases.excel_response['COMMON_DISEASE_CAUSED_DEATH'].clear()
    filter_common_diseases.excel_response[
        'COMMON_DISEASE_CAUSED_DEATH'] = filter_common_diseases.chart_unique_constant_left
    filter_common_diseases.save()


def report_primary_need_in_barangay(location_id, total_population):
    # PRIMARY NEEDS IN THE BARANGAY

    filter_primary_needs = ReportHistory.objects.filter(
        location_id=location_id,
        report_category_id__category_slug=constants.CATEGORIES_SLUG[17]).first()
    primary_needs_data = list(dict(filter_primary_needs.chart_constant_left).values())
    primary_needs_labels = list(dict(filter_primary_needs.chart_constant_left).keys())
    filter_primary_needs.chart_response_left['datasets'][0]['data'] = primary_needs_data
    filter_primary_needs.chart_response_left['datasets'][0]['backgroundColor'] = constants.CHART_BACKGROUND_COLOR[
                                                                                 :len(primary_needs_data)]
    filter_primary_needs.chart_response_left['labels'] = primary_needs_labels
    filter_primary_needs.chart_response_left['datasets'][0]['total_population'] = total_population
    filter_primary_needs.save()

    # Excel
    filter_primary_needs.excel_response['PRIMARY_NEEDS_IN_THE_BARANGAY'].clear()
    filter_primary_needs.excel_response[
        'PRIMARY_NEEDS_IN_THE_BARANGAY'] = filter_primary_needs.chart_unique_constant_left
    filter_primary_needs.save()
