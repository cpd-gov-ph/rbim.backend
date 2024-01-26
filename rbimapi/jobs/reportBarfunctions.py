from rbim.models import ReportHistory
from rbimapi.jobs import reportConstants as constants

def report_marital_status_by_age(location_id, total_population):
    # MARITAL STATUS OF THE TOTAL POPULATION BY AGE
    filter_marital_status_by_age = ReportHistory.objects.filter(
        location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[3]).first()

    single_data = dict(label="Single", backgroundColor=constants.CHART_BACKGROUND_COLOR[0],
                       stack="marital_status",
                       data=list(filter_marital_status_by_age.chart_constant_left['Single'].values()))
    married_data = dict(label="Married", backgroundColor=constants.CHART_BACKGROUND_COLOR[1],
                        stack="marital_status",
                        data=list(filter_marital_status_by_age.chart_constant_left['Married'].values()))
    livingin_data = dict(label="Living-in", backgroundColor=constants.CHART_BACKGROUND_COLOR[2],
                         stack="marital_status",
                         data=list(filter_marital_status_by_age.chart_constant_left['Living-in'].values()))
    widowed_data = dict(label="Widowed", backgroundColor=constants.CHART_BACKGROUND_COLOR[3],
                        stack="marital_status",
                        data=list(filter_marital_status_by_age.chart_constant_left['Widowed'].values()))
    separated_data = dict(label="Separated", backgroundColor=constants.CHART_BACKGROUND_COLOR[4],
                          stack="marital_status",
                          data=list(filter_marital_status_by_age.chart_constant_left['Separated'].values()))
    divorced_data = dict(label="Divorced", backgroundColor=constants.CHART_BACKGROUND_COLOR[5],
                         stack="marital_status",
                         data=list(filter_marital_status_by_age.chart_constant_left['Divorced'].values()))
    unknown_data = dict(label="Unknown", backgroundColor=constants.CHART_BACKGROUND_COLOR[6],
                        stack="marital_status",
                        data=list(filter_marital_status_by_age.chart_constant_left['Unknown'].values()))
    data = filter_marital_status_by_age.chart_response_left['datasets']
    data.clear()
    data.extend(
        (single_data, married_data, livingin_data, widowed_data, separated_data, divorced_data, unknown_data))
    filter_marital_status_by_age.excel_response = filter_marital_status_by_age.chart_constant_left
    filter_marital_status_by_age.chart_response_left["total_population"] = \
        filter_marital_status_by_age.chart_response_left["total_population"] + total_population
    filter_marital_status_by_age.save()

def report_marital_status_by_sex(location_id, total_population):
    # MARITAL STATUS OF THE TOTAL POPULATION BY SEX
    filter_marital_status_by_gender = ReportHistory.objects.filter(
        location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[4]).first()
    # Male
    m_single_data = dict(label="Single", backgroundColor=constants.CHART_BACKGROUND_COLOR[0],
                         stack="Male",
                         data=list(filter_marital_status_by_gender.chart_constant_left['Male']['Single'].values()))
    m_married_data = dict(label="Married", backgroundColor=constants.CHART_BACKGROUND_COLOR[1],
                          stack="Male",
                          data=list(
                              filter_marital_status_by_gender.chart_constant_left['Male']['Married'].values()))
    m_livingin_data = dict(label="Living-in", backgroundColor=constants.CHART_BACKGROUND_COLOR[2],
                           stack="Male",
                           data=list(
                               filter_marital_status_by_gender.chart_constant_left['Male']['Living-in'].values()))
    m_widowed_data = dict(label="Widowed", backgroundColor=constants.CHART_BACKGROUND_COLOR[3],
                          stack="Male",
                          data=list(
                              filter_marital_status_by_gender.chart_constant_left['Male']['Widowed'].values()))
    m_separated_data = dict(label="Separated", backgroundColor=constants.CHART_BACKGROUND_COLOR[4],
                            stack="Male",
                            data=list(
                                filter_marital_status_by_gender.chart_constant_left['Male']['Separated'].values()))
    m_divorced_data = dict(label="Divorced", backgroundColor=constants.CHART_BACKGROUND_COLOR[5],
                           stack="Male",
                           data=list(
                               filter_marital_status_by_gender.chart_constant_left['Male']['Divorced'].values()))
    m_unknown_data = dict(label="Unknown", backgroundColor=constants.CHART_BACKGROUND_COLOR[6],
                          stack="Male",
                          data=list(
                              filter_marital_status_by_gender.chart_constant_left['Male']['Unknown'].values()))

    # Female
    f_single_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[0],
                         stack="Female",
                         data=list(
                             filter_marital_status_by_gender.chart_constant_left['Female']['Single'].values()))
    f_married_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[1],
                          stack="Female",
                          data=list(
                              filter_marital_status_by_gender.chart_constant_left['Female']['Married'].values()))
    f_livingin_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[2],
                           stack="Female",
                           data=list(
                               filter_marital_status_by_gender.chart_constant_left['Female']['Living-in'].values()))
    f_widowed_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[3],
                          stack="Female",
                          data=list(
                              filter_marital_status_by_gender.chart_constant_left['Female']['Widowed'].values()))
    f_separated_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[4],
                            stack="Female",
                            data=list(filter_marital_status_by_gender.chart_constant_left['Female'][
                                          'Separated'].values()))
    f_divorced_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[5],
                           stack="Female",
                           data=list(
                               filter_marital_status_by_gender.chart_constant_left['Female']['Divorced'].values()))
    f_unknown_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[6],
                          stack="Female",
                          data=list(
                              filter_marital_status_by_gender.chart_constant_left['Female']['Unknown'].values()))

    data = filter_marital_status_by_gender.chart_response_left['datasets']
    data.clear()
    data.extend((m_single_data, m_married_data, m_livingin_data, m_widowed_data, m_separated_data, m_divorced_data,
                 m_unknown_data, f_single_data, f_married_data, f_livingin_data, f_widowed_data, f_separated_data,
                 f_divorced_data, f_unknown_data))
    filter_marital_status_by_gender.chart_response_left["total_population"] = \
        filter_marital_status_by_gender.chart_response_left["total_population"] + total_population
    filter_marital_status_by_gender.save()

    # Excel
    marital_status_excel_male_data = list(
        dict(filter_marital_status_by_gender.excel_constant['Male']).values())
    marital_status_excel_female_data = list(
        dict(filter_marital_status_by_gender.excel_constant['Female']).values())
    marital_status_excel_keys = list(dict(filter_marital_status_by_gender.excel_constant['Female']).keys())
    marital_status_excel_keys.append('Total')
    filter_marital_status_by_gender.excel_response["Marital_Status"] = marital_status_excel_keys
    filter_marital_status_by_gender.excel_response["Male"] = marital_status_excel_male_data
    filter_marital_status_by_gender.excel_response["Female"] = marital_status_excel_female_data
    filter_marital_status_by_gender.excel_response["Male"].append(sum(marital_status_excel_male_data))
    filter_marital_status_by_gender.excel_response["Female"].append(sum(marital_status_excel_female_data))
    filter_marital_status_by_gender.save()

def report_religion_by_sex(location_id, total_population):
    # RELIGIOUS AFFLIATION OF THE TOTAL POPULATION BY SEX
    filter_religion_report = ReportHistory.objects.filter(
        location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[5]).first()
    religion_religion_data = list(filter_religion_report.excel_constant["Male"].keys())
    data = filter_religion_report.chart_response_left['datasets']
    data.clear()

    m_value = list(filter_religion_report.excel_constant["Male"].values())
    f_value = list(filter_religion_report.excel_constant["Female"].values())
    male_religion_data = dict(label="Male", backgroundColor="#0086B6", data=m_value)
    data.append(male_religion_data)

    female_religion_data = dict(label="Female", backgroundColor="#CC00D0", data=f_value)
    data.append(female_religion_data)

    filter_religion_report.chart_response_left['labels'] = religion_religion_data

    filter_religion_report.chart_response_left["total_population"] = \
        filter_religion_report.chart_response_left["total_population"] + total_population

    # Excel
    religion_excel_male_data = list(dict(filter_religion_report.excel_constant['Male']).values())
    religion_excel_religion_data = list(filter_religion_report.excel_constant["Male"].keys())
    religion_excel_female_data = list(dict(filter_religion_report.excel_constant['Female']).values())
    filter_religion_report.excel_response["Religion"] = religion_excel_religion_data
    filter_religion_report.excel_response["Male"] = religion_excel_male_data
    filter_religion_report.excel_response["Female"] = religion_excel_female_data
    filter_religion_report.excel_response["Religion"].append("Total")
    filter_religion_report.excel_response["Male"].append(sum(religion_excel_male_data))
    filter_religion_report.excel_response["Female"].append(sum(religion_excel_female_data))
    filter_religion_report.save()


def report_ethnic_by_sex(location_id, total_population):
    # ETHNIC GROUPING OF TOTAL POPULATION BY SEX
    filter_ethnic_report = ReportHistory.objects.filter(
        location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[6]).first()
    ethnic_data = list(filter_ethnic_report.excel_constant["Male"].keys())
    data = filter_ethnic_report.chart_response_left['datasets']
    data.clear()

    m_value = list(filter_ethnic_report.excel_constant["Male"].values())
    f_value = list(filter_ethnic_report.excel_constant["Female"].values())
    male_ethnic_data = dict(label="Male", backgroundColor="#0086B6", data=m_value)
    data.append(male_ethnic_data)
    female_ethnic_data = dict(label="Female", backgroundColor="#CC00D0", data=f_value)
    data.append(female_ethnic_data)

    filter_ethnic_report.chart_response_left['labels'] = ethnic_data
    filter_ethnic_report.chart_response_left["total_population"] = \
        filter_ethnic_report.chart_response_left["total_population"] + total_population

    # Excel
    ethnic_excel_male_data = list(dict(filter_ethnic_report.excel_constant['Male']).values())
    ethnic_excel_religion_data = list(filter_ethnic_report.excel_constant["Male"].keys())
    ethnic_excel_female_data = list(dict(filter_ethnic_report.excel_constant['Female']).values())
    filter_ethnic_report.excel_response["Ethnic"] = ethnic_excel_religion_data
    filter_ethnic_report.excel_response["Male"] = ethnic_excel_male_data
    filter_ethnic_report.excel_response["Female"] = ethnic_excel_female_data
    filter_ethnic_report.excel_response["Ethnic"].append("Total")
    filter_ethnic_report.excel_response["Male"].append(sum(ethnic_excel_male_data))
    filter_ethnic_report.excel_response["Female"].append(sum(ethnic_excel_female_data))
    filter_ethnic_report.save()

def report_monthly_income_by_age_sex(location_id, total_population):
    # MONTHLY INCOME OF THE TOTAL POPULATION (15+) BY AGE AND SEX
    filter_salary_by_age = ReportHistory.objects.filter(
        location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[7]).first()

    # Male
    m_under5k_v = list(filter_salary_by_age.chart_constant_left['Male']["Under-5k"].values())
    m_5000_9000_v = list(filter_salary_by_age.chart_constant_left['Male']['5000-9999'].values())
    m_10000_14999_v = list(filter_salary_by_age.chart_constant_left['Male']['10000-14999'].values())
    m_15000_19999_v = list(filter_salary_by_age.chart_constant_left['Male']['15000-19999'].values())
    m_20000_24999_v = list(filter_salary_by_age.chart_constant_left['Male']['20000-24999'].values())
    m_above_25_v = list(filter_salary_by_age.chart_constant_left['Male']['25000-Above'].values())

    m_under_5k = dict(label="Under-5k", backgroundColor=constants.CHART_BACKGROUND_COLOR[0],
                      stack="Male",
                      data=m_under5k_v)
    m_5000_9999 = dict(label="5000-9999", backgroundColor=constants.CHART_BACKGROUND_COLOR[1],
                       stack="Male",
                       data=m_5000_9000_v)
    m_10000_14999 = dict(label="10000-14999", backgroundColor=constants.CHART_BACKGROUND_COLOR[2],
                         stack="Male",
                         data=m_10000_14999_v)
    m_15000_19999 = dict(label="15000-19999", backgroundColor=constants.CHART_BACKGROUND_COLOR[3],
                         stack="Male",
                         data=m_15000_19999_v)
    m_20000_24999 = dict(label="20000-24999", backgroundColor=constants.CHART_BACKGROUND_COLOR[4],
                         stack="Male",
                         data=m_20000_24999_v)
    m_25000_above = dict(label="25000-Above", backgroundColor=constants.CHART_BACKGROUND_COLOR[5],
                         stack="Male",
                         data=m_above_25_v)

    # Female
    f_under5k_v = list(filter_salary_by_age.chart_constant_left['Female']["Under-5k"].values())
    f_5000_9000_v = list(filter_salary_by_age.chart_constant_left['Female']['5000-9999'].values())
    f_10000_14999_v = list(filter_salary_by_age.chart_constant_left['Female']['10000-14999'].values())
    f_15000_19999_v = list(filter_salary_by_age.chart_constant_left['Female']['15000-19999'].values())
    f_20000_24999_v = list(filter_salary_by_age.chart_constant_left['Female']['20000-24999'].values())
    f_above_25_v = list(filter_salary_by_age.chart_constant_left['Female']['25000-Above'].values())

    f_under_5k = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[0],
                      stack="Female",
                      data=f_under5k_v)
    f_5000_9999 = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[1],
                       stack="Female",
                       data=f_5000_9000_v)
    f_10000_14999 = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[2],
                         stack="Female",
                         data=f_10000_14999_v)
    f_15000_19999 = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[3],
                         stack="Female",
                         data=f_15000_19999_v)
    f_20000_24999 = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[4],
                         stack="Female",
                         data=f_20000_24999_v)
    f_25000_above = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[5],
                         stack="Female",
                         data=f_above_25_v)

    data = filter_salary_by_age.chart_response_left['datasets']
    data.clear()
    data.extend((m_under_5k, m_5000_9999, m_10000_14999, m_15000_19999, m_20000_24999, m_25000_above,
                 f_under_5k, f_5000_9999, f_10000_14999, f_15000_19999, f_20000_24999, f_25000_above))

    filter_salary_by_age.chart_response_left["total_population"] = \
        filter_salary_by_age.chart_response_left["total_population"] + total_population

    # Excel
    filter_salary_by_age.excel_response["Male_Under-5k"] = m_under5k_v
    filter_salary_by_age.excel_response["Male_Under-5k"].append(sum(m_under5k_v))
    filter_salary_by_age.excel_response["Male_5000-9999"] = m_5000_9000_v
    filter_salary_by_age.excel_response["Male_5000-9999"].append(sum(m_5000_9000_v))
    filter_salary_by_age.excel_response["Male_10000-14999"] = m_10000_14999_v
    filter_salary_by_age.excel_response["Male_10000-14999"].append(sum(m_10000_14999_v))
    filter_salary_by_age.excel_response["Male_15000-19999"] = m_15000_19999_v
    filter_salary_by_age.excel_response["Male_15000-19999"].append(sum(m_15000_19999_v))
    filter_salary_by_age.excel_response["Male_20000-24999"] = m_20000_24999_v
    filter_salary_by_age.excel_response["Male_20000-24999"].append(sum(m_20000_24999_v))
    filter_salary_by_age.excel_response["Male_25000-Above"] = m_above_25_v
    filter_salary_by_age.excel_response["Male_25000-Above"].append(sum(m_above_25_v))

    filter_salary_by_age.excel_response["Female_Under-5k"] = f_under5k_v
    filter_salary_by_age.excel_response["Female_Under-5k"].append(sum(f_under5k_v))
    filter_salary_by_age.excel_response["Female_5000-9999"] = f_5000_9000_v
    filter_salary_by_age.excel_response["Female_5000-9999"].append(sum(f_5000_9000_v))
    filter_salary_by_age.excel_response["Female_10000-14999"] = f_10000_14999_v
    filter_salary_by_age.excel_response["Female_10000-14999"].append(sum(f_10000_14999_v))
    filter_salary_by_age.excel_response["Female_15000-19999"] = f_15000_19999_v
    filter_salary_by_age.excel_response["Female_15000-19999"].append(sum(f_15000_19999_v))
    filter_salary_by_age.excel_response["Female_20000-24999"] = f_20000_24999_v
    filter_salary_by_age.excel_response["Female_20000-24999"].append(sum(f_20000_24999_v))
    filter_salary_by_age.excel_response["Female_25000-Above"] = f_above_25_v
    filter_salary_by_age.excel_response["Female_25000-Above"].append(sum(f_above_25_v))

    filter_salary_by_age.save()

def report_source_of_income_by_age(location_id, total_population):
    # MAJOR SOURCE OF INCOME OF THE TOTAL POPULATION (15+) BY AGE AND SEX
    filter_source_of_income_by_age = ReportHistory.objects.filter(
        location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[8]).first()

    # Male
    m_employment = list(filter_source_of_income_by_age.chart_constant_left['Male']['Employment'].values())
    m_business = list(filter_source_of_income_by_age.chart_constant_left['Male']['Business'].values())
    m_remittance = list(filter_source_of_income_by_age.chart_constant_left['Male']['Remittance'].values())
    m_investment = list(filter_source_of_income_by_age.chart_constant_left['Male']['Investments'].values())
    m_others = list(filter_source_of_income_by_age.chart_constant_left['Male']['Others'].values())

    m_employemnt_data = dict(label="Employment", backgroundColor=constants.CHART_BACKGROUND_COLOR[0],
                             stack="Male",
                             data=m_employment)
    m_business_data = dict(label="Business", backgroundColor=constants.CHART_BACKGROUND_COLOR[1],
                           stack="Male",
                           data=m_business)
    m_remittance_data = dict(label="Remittance", backgroundColor=constants.CHART_BACKGROUND_COLOR[2],
                             stack="Male",
                             data=m_remittance)
    m_investment_data = dict(label="Investments", backgroundColor=constants.CHART_BACKGROUND_COLOR[3],
                             stack="Male",
                             data=m_investment)
    m_others_data = dict(label="Others", backgroundColor=constants.CHART_BACKGROUND_COLOR[4],
                         stack="Male",
                         data=m_others)

    # Female
    f_employment = list(filter_source_of_income_by_age.chart_constant_left['Female']['Employment'].values())
    f_business = list(filter_source_of_income_by_age.chart_constant_left['Female']['Business'].values())
    f_remittance = list(filter_source_of_income_by_age.chart_constant_left['Female']['Remittance'].values())
    f_investment = list(filter_source_of_income_by_age.chart_constant_left['Female']['Investments'].values())
    f_others = list(filter_source_of_income_by_age.chart_constant_left['Female']['Others'].values())

    f_employemnt_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[0],
                             stack="Female",
                             data=f_employment)
    f_business_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[1],
                           stack="Female",
                           data=f_business)
    f_remittance_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[2],
                             stack="Female",
                             data=f_remittance)
    f_investment_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[3],
                             stack="Female",
                             data=f_investment)
    f_others_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[4],
                         stack="Female",
                         data=f_others)

    data = filter_source_of_income_by_age.chart_response_left['datasets']
    data.clear()
    data.extend((m_employemnt_data, m_business_data, m_remittance_data, m_investment_data, m_others_data,
                 f_employemnt_data, f_business_data, f_remittance_data, f_investment_data, f_others_data))

    filter_source_of_income_by_age.chart_response_left["total_population"] = \
        filter_source_of_income_by_age.chart_response_left["total_population"] + total_population

    # #Excel
    filter_source_of_income_by_age.excel_response['Male_Employment'] = m_employment
    filter_source_of_income_by_age.excel_response['Male_Employment'].append(sum(m_employment))
    filter_source_of_income_by_age.excel_response['Male_Business'] = m_business
    filter_source_of_income_by_age.excel_response['Male_Business'].append(sum(m_business))
    filter_source_of_income_by_age.excel_response['Male_Remittance'] = m_remittance
    filter_source_of_income_by_age.excel_response['Male_Remittance'].append(sum(m_remittance))
    filter_source_of_income_by_age.excel_response['Male_Investments'] = m_investment
    filter_source_of_income_by_age.excel_response['Male_Investments'].append(sum(m_investment))
    filter_source_of_income_by_age.excel_response['Male_Others'] = m_others
    filter_source_of_income_by_age.excel_response['Male_Others'].append(sum(m_others))

    filter_source_of_income_by_age.excel_response['Female_Employment'] = f_employment
    filter_source_of_income_by_age.excel_response['Female_Employment'].append(sum(f_employment))
    filter_source_of_income_by_age.excel_response['Female_Business'] = f_business
    filter_source_of_income_by_age.excel_response['Female_Business'].append(sum(f_business))
    filter_source_of_income_by_age.excel_response['Female_Remittance'] = f_remittance
    filter_source_of_income_by_age.excel_response['Female_Remittance'].append(sum(f_remittance))
    filter_source_of_income_by_age.excel_response['Female_Investments'] = f_investment
    filter_source_of_income_by_age.excel_response['Female_Investments'].append(sum(f_investment))
    filter_source_of_income_by_age.excel_response['Female_Others'] = f_others
    filter_source_of_income_by_age.excel_response['Female_Others'].append(sum(f_others))

    filter_source_of_income_by_age.save()

def report_status_of_work_by_age(location_id, total_population):
    # STATUS OF WORK/ BUSINESS OF THE TOTAL POPULATION (15+) BY AGE AND SEX
    filter_status_of_work_by_age = ReportHistory.objects.filter(
        location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[9]).first()

    # Male
    m_permanent_work = list(filter_status_of_work_by_age.chart_constant_left['Male']['Permanent Work'].values())
    m_casual_work = list(filter_status_of_work_by_age.chart_constant_left['Male']['Casual Work'].values())
    m_contractual_work = list(filter_status_of_work_by_age.chart_constant_left['Male']['Contractual Work'].values())
    m_owned_business = list(
        filter_status_of_work_by_age.chart_constant_left['Male']['Individually Owned Business'].values())
    m_shared_business = list(
        filter_status_of_work_by_age.chart_constant_left['Male']['Shared/Partnership Business'].values())
    m_corporate_business = list(
        filter_status_of_work_by_age.chart_constant_left['Male']['Corporate Business'].values())

    m_permanent_work_data = dict(label="Permanent Work", backgroundColor=constants.CHART_BACKGROUND_COLOR[0],
                                 stack="Male",
                                 data=m_permanent_work)
    m_casual_work_data = dict(label="Casual Work", backgroundColor=constants.CHART_BACKGROUND_COLOR[1],
                              stack="Male",
                              data=m_casual_work)
    m_contractual_work_data = dict(label="Contractual Work", backgroundColor=constants.CHART_BACKGROUND_COLOR[2],
                                   stack="Male",
                                   data=m_contractual_work)
    m_owned_business_data = dict(label="Individually Owned Business",
                                 backgroundColor=constants.CHART_BACKGROUND_COLOR[3],
                                 stack="Male",
                                 data=m_owned_business)
    m_shared_business_data = dict(label="Shared/Partnership Business",
                                  backgroundColor=constants.CHART_BACKGROUND_COLOR[4],
                                  stack="Male",
                                  data=m_shared_business)
    m_corporate_business_data = dict(label="Corporate Business",
                                     backgroundColor=constants.CHART_BACKGROUND_COLOR[5],
                                     stack="Male",
                                     data=m_corporate_business)

    # Female
    f_permanent_work = list(filter_status_of_work_by_age.chart_constant_left['Female']['Permanent Work'].values())
    f_casual_work = list(filter_status_of_work_by_age.chart_constant_left['Female']['Casual Work'].values())
    f_contractual_work = list(
        filter_status_of_work_by_age.chart_constant_left['Female']['Contractual Work'].values())
    f_owned_business = list(
        filter_status_of_work_by_age.chart_constant_left['Female']['Individually Owned Business'].values())
    f_shared_business = list(
        filter_status_of_work_by_age.chart_constant_left['Female']['Shared/Partnership Business'].values())
    f_corporate_business = list(
        filter_status_of_work_by_age.chart_constant_left['Female']['Corporate Business'].values())

    f_permanent_work_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[0],
                                 stack="Female",
                                 data=f_permanent_work)
    f_casual_work_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[1],
                              stack="Female",
                              data=f_casual_work)
    f_contractual_work_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[2],
                                   stack="Female",
                                   data=f_contractual_work)
    f_owned_business_data = dict(
        backgroundColor=constants.CHART_BACKGROUND_COLOR[3],
        stack="Female",
        data=f_owned_business)
    f_shared_business_data = dict(
        backgroundColor=constants.CHART_BACKGROUND_COLOR[4],
        stack="Female",
        data=f_shared_business)
    f_corporate_business_data = dict(
        backgroundColor=constants.CHART_BACKGROUND_COLOR[5],
        stack="Female",
        data=f_corporate_business)

    data = filter_status_of_work_by_age.chart_response_left['datasets']
    data.clear()
    data.extend((m_permanent_work_data, m_casual_work_data, m_contractual_work_data, m_owned_business_data,
                 m_shared_business_data, m_corporate_business_data,
                 f_permanent_work_data, f_casual_work_data, f_contractual_work_data, f_owned_business_data,
                 f_shared_business_data, f_corporate_business_data))

    filter_status_of_work_by_age.chart_response_left["total_population"] = \
        filter_status_of_work_by_age.chart_response_left["total_population"] + total_population

    # #Excel
    filter_status_of_work_by_age.excel_response['Male_Permanent_Work'] = m_permanent_work
    filter_status_of_work_by_age.excel_response['Male_Permanent_Work'].append(sum(m_permanent_work))
    filter_status_of_work_by_age.excel_response['Male_Casual_Work'] = m_casual_work
    filter_status_of_work_by_age.excel_response['Male_Casual_Work'].append(sum(m_casual_work))
    filter_status_of_work_by_age.excel_response['Male_Contractual_Work'] = m_contractual_work
    filter_status_of_work_by_age.excel_response['Male_Contractual_Work'].append(sum(m_contractual_work))
    filter_status_of_work_by_age.excel_response['Male_Individually_Owned_Business'] = m_owned_business
    filter_status_of_work_by_age.excel_response['Male_Individually_Owned_Business'].append(sum(m_owned_business))
    filter_status_of_work_by_age.excel_response['Male_Shared/Partnership_Business'] = m_shared_business
    filter_status_of_work_by_age.excel_response['Male_Shared/Partnership_Business'].append(sum(m_shared_business))
    filter_status_of_work_by_age.excel_response['Male_Corporate_Business'] = m_corporate_business
    filter_status_of_work_by_age.excel_response['Male_Corporate_Business'].append(sum(m_corporate_business))

    filter_status_of_work_by_age.excel_response['Female_Permanent_Work'] = f_permanent_work
    filter_status_of_work_by_age.excel_response['Female_Permanent_Work'].append(sum(f_permanent_work))
    filter_status_of_work_by_age.excel_response['Female_Casual_Work'] = f_casual_work
    filter_status_of_work_by_age.excel_response['Female_Casual_Work'].append(sum(f_casual_work))
    filter_status_of_work_by_age.excel_response['Female_Contractual_Work'] = f_contractual_work
    filter_status_of_work_by_age.excel_response['Female_Contractual_Work'].append(sum(f_contractual_work))
    filter_status_of_work_by_age.excel_response['Female_Individually_Owned_Business'] = f_owned_business
    filter_status_of_work_by_age.excel_response['Female_Individually_Owned_Business'].append(sum(f_owned_business))
    filter_status_of_work_by_age.excel_response['Female_Shared/Partnership_Business'] = f_shared_business
    filter_status_of_work_by_age.excel_response['Female_Shared/Partnership_Business'].append(sum(f_shared_business))
    filter_status_of_work_by_age.excel_response['Female_Corporate_Business'] = f_corporate_business
    filter_status_of_work_by_age.excel_response['Female_Corporate_Business'].append(sum(f_corporate_business))

    filter_status_of_work_by_age.save()

def report_preganancy_count(location_id):
    # PREGNANCIES OF POPULATION (WOMEN 10-54) BY AGE AND  GRAVIDA
    filter_preganancy_count = ReportHistory.objects.filter(
        location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[13]).first()

    f_preganant_1 = list(filter_preganancy_count.chart_constant_left['Female']['1-Time-Preganant'].values())
    f_preganant_2 = list(filter_preganancy_count.chart_constant_left['Female']['2-Time-Preganant'].values())
    f_preganant_3 = list(filter_preganancy_count.chart_constant_left['Female']['3-Time-Preganant'].values())
    f_preganant_4 = list(filter_preganancy_count.chart_constant_left['Female']['4-Time-Preganant'].values())
    f_preganant_5 = list(filter_preganancy_count.chart_constant_left['Female']['5-Time-Preganant'].values())
    f_preganant_6 = list(filter_preganancy_count.chart_constant_left['Female']['6-Time-Preganant'].values())
    f_preganant_7 = list(filter_preganancy_count.chart_constant_left['Female']['7-Time-Preganant'].values())
    f_preganant_8 = list(filter_preganancy_count.chart_constant_left['Female']['8-Time-Preganant'].values())
    f_preganant_9 = list(filter_preganancy_count.chart_constant_left['Female']['9-Time-Preganant'].values())
    f_preganant_10 = list(filter_preganancy_count.chart_constant_left['Female']['10-Time-Preganant'].values())

    f_preganant_1_data = dict(label="1-Time-Preganant", backgroundColor=constants.CHART_BACKGROUND_COLOR[0],
                              stack="Female",
                              data=f_preganant_1)
    f_preganant_2_data = dict(label="2-Time-Preganant", backgroundColor=constants.CHART_BACKGROUND_COLOR[1],
                              stack="Female",
                              data=f_preganant_2)
    f_preganant_3_data = dict(label="3-Time-Preganant", backgroundColor=constants.CHART_BACKGROUND_COLOR[2],
                              stack="Female",
                              data=f_preganant_3)
    f_preganant_4_data = dict(label="4-Time-Preganant",
                              backgroundColor=constants.CHART_BACKGROUND_COLOR[3],
                              stack="Female",
                              data=f_preganant_4)
    f_preganant_5_data = dict(label="5-Time-Preganant",
                              backgroundColor=constants.CHART_BACKGROUND_COLOR[4],
                              stack="Female",
                              data=f_preganant_5)
    f_preganant_6_data = dict(label="6-Time-Preganant",
                              backgroundColor=constants.CHART_BACKGROUND_COLOR[5],
                              stack="Female",
                              data=f_preganant_6)
    f_preganant_7_data = dict(label="7-Time-Preganant",
                              backgroundColor=constants.CHART_BACKGROUND_COLOR[6],
                              stack="Female",
                              data=f_preganant_7)
    f_preganant_8_data = dict(label="8-Time-Preganant",
                              backgroundColor=constants.CHART_BACKGROUND_COLOR[7],
                              stack="Female",
                              data=f_preganant_8)
    f_preganant_9_data = dict(label="9-Time-Preganant",
                              backgroundColor=constants.CHART_BACKGROUND_COLOR[8],
                              stack="Female",
                              data=f_preganant_9)
    f_preganant_10_data = dict(label="10+-Time-Preganant",
                               backgroundColor=constants.CHART_BACKGROUND_COLOR[9],
                               stack="Female",
                               data=f_preganant_10)

    data = filter_preganancy_count.chart_response_left['datasets']
    data.clear()
    data.extend((f_preganant_1_data, f_preganant_2_data, f_preganant_3_data, f_preganant_4_data,
                 f_preganant_5_data, f_preganant_6_data, f_preganant_7_data, f_preganant_8_data,
                 f_preganant_9_data, f_preganant_10_data))

    merged_data = f_preganant_1 + f_preganant_2 + f_preganant_3 + f_preganant_4 + f_preganant_5 + f_preganant_6 + f_preganant_7 + f_preganant_8 + f_preganant_9 + f_preganant_10
    filter_preganancy_count.chart_response_left["total_population"] = filter_preganancy_count.chart_response_left[
                                                                          "total_population"] + sum(merged_data)

    # #Excel
    filter_preganancy_count.excel_response['1'] = f_preganant_1
    filter_preganancy_count.excel_response['1'].append(sum(f_preganant_1))
    filter_preganancy_count.excel_response['2'] = f_preganant_2
    filter_preganancy_count.excel_response['2'].append(sum(f_preganant_2))
    filter_preganancy_count.excel_response['3'] = f_preganant_3
    filter_preganancy_count.excel_response['3'].append(sum(f_preganant_3))
    filter_preganancy_count.excel_response['4'] = f_preganant_4
    filter_preganancy_count.excel_response['4'].append(sum(f_preganant_4))
    filter_preganancy_count.excel_response['5'] = f_preganant_5
    filter_preganancy_count.excel_response['5'].append(sum(f_preganant_5))
    filter_preganancy_count.excel_response['6'] = f_preganant_6
    filter_preganancy_count.excel_response['6'].append(sum(f_preganant_6))
    filter_preganancy_count.excel_response['7'] = f_preganant_7
    filter_preganancy_count.excel_response['7'].append(sum(f_preganant_7))
    filter_preganancy_count.excel_response['8'] = f_preganant_8
    filter_preganancy_count.excel_response['8'].append(sum(f_preganant_8))
    filter_preganancy_count.excel_response['9'] = f_preganant_9
    filter_preganancy_count.excel_response['9'].append(sum(f_preganant_9))
    filter_preganancy_count.excel_response['10+'] = f_preganant_10
    filter_preganancy_count.excel_response['10+'].append(sum(f_preganant_10))
    filter_preganancy_count.save()

def report_school_level_by_age(location_id):
    # CURRENTLY ENROLLED BY AGE, SEX AND SCHOOL LEVEL
    filter_school_level_by_age = ReportHistory.objects.filter(
        location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[14]).first()

    # Male
    m_pre_school = list(
        filter_school_level_by_age.chart_constant_left['Male']['Pre-school'].values())
    m_elementary = list(
        filter_school_level_by_age.chart_constant_left['Male']['Elementary'].values())
    m_junior_high_schl = list(
        filter_school_level_by_age.chart_constant_left['Male']['Junior High School'].values())
    m_senior_high_schl = list(
        filter_school_level_by_age.chart_constant_left['Male']['Senior High School'].values())
    m_vocational_tech = list(
        filter_school_level_by_age.chart_constant_left['Male']['Vocational/Technical'].values())
    m_college_university = list(
        filter_school_level_by_age.chart_constant_left['Male']['College/University'].values())

    m_pre_school_data = dict(label="Pre-school", backgroundColor=constants.CHART_BACKGROUND_COLOR[0],
                             stack="Male",
                             data=m_pre_school)
    m_elementary_data = dict(label="Elementary", backgroundColor=constants.CHART_BACKGROUND_COLOR[1],
                             stack="Male",
                             data=m_elementary)
    m_junior_high_schl_data = dict(label="Junior High School", backgroundColor=constants.CHART_BACKGROUND_COLOR[2],
                                   stack="Male",
                                   data=m_junior_high_schl)
    m_senior_high_schl_data = dict(label="Senior High School",
                                   backgroundColor=constants.CHART_BACKGROUND_COLOR[3],
                                   stack="Male",
                                   data=m_senior_high_schl)
    m_vocational_tech_data = dict(label="Vocational/Technical",
                                  backgroundColor=constants.CHART_BACKGROUND_COLOR[4],
                                  stack="Male",
                                  data=m_vocational_tech)
    m_college_university_data = dict(label="College/University",
                                     backgroundColor=constants.CHART_BACKGROUND_COLOR[5],
                                     stack="Male",
                                     data=m_college_university)

    # Female
    f_pre_school = list(
        filter_school_level_by_age.chart_constant_left['Female']['Pre-school'].values())
    f_elementary = list(
        filter_school_level_by_age.chart_constant_left['Female']['Elementary'].values())
    f_junior_high_schl = list(
        filter_school_level_by_age.chart_constant_left['Female']['Junior High School'].values())
    f_senior_high_schl = list(
        filter_school_level_by_age.chart_constant_left['Female']['Senior High School'].values())
    f_vocational_tech = list(
        filter_school_level_by_age.chart_constant_left['Female']['Vocational/Technical'].values())
    f_college_university = list(
        filter_school_level_by_age.chart_constant_left['Female']['College/University'].values())

    f_pre_school_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[0],
                             stack="Female",
                             data=f_pre_school)
    f_elementary_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[1],
                             stack="Female",
                             data=f_elementary)
    f_junior_high_schl_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[2],
                                   stack="Female",
                                   data=f_junior_high_schl)
    f_senior_high_schl_data = dict(
        backgroundColor=constants.CHART_BACKGROUND_COLOR[3],
        stack="Female",
        data=f_senior_high_schl)
    f_vocational_tech_data = dict(
        backgroundColor=constants.CHART_BACKGROUND_COLOR[4],
        stack="Female",
        data=f_vocational_tech)
    f_college_university_data = dict(
        backgroundColor=constants.CHART_BACKGROUND_COLOR[5],
        stack="Female",
        data=f_college_university)

    data = filter_school_level_by_age.chart_response_left['datasets']
    data.clear()
    data.extend((m_pre_school_data, m_elementary_data, m_junior_high_schl_data,
                 m_senior_high_schl_data, m_vocational_tech_data, m_college_university_data,
                 f_pre_school_data, f_elementary_data, f_junior_high_schl_data,
                 f_senior_high_schl_data, f_vocational_tech_data, f_college_university_data))

    # #Excel
    filter_school_level_by_age.excel_response['Male_Pre-school'] = m_pre_school
    filter_school_level_by_age.excel_response['Male_Pre-school'].append(sum(m_pre_school))
    filter_school_level_by_age.excel_response['Male_Elementary'] = m_elementary
    filter_school_level_by_age.excel_response['Male_Elementary'].append(sum(m_elementary))
    filter_school_level_by_age.excel_response['Male_Junior_High_School'] = m_junior_high_schl
    filter_school_level_by_age.excel_response['Male_Junior_High_School'].append(sum(m_junior_high_schl))
    filter_school_level_by_age.excel_response['Male_Senior_High_School'] = m_senior_high_schl
    filter_school_level_by_age.excel_response['Male_Senior_High_School'].append(sum(m_senior_high_schl))
    filter_school_level_by_age.excel_response['Male_Vocational/Technical'] = m_vocational_tech
    filter_school_level_by_age.excel_response['Male_Vocational/Technical'].append(sum(m_vocational_tech))
    filter_school_level_by_age.excel_response['Male_College/University'] = m_college_university
    filter_school_level_by_age.excel_response['Male_College/University'].append(sum(m_college_university))

    filter_school_level_by_age.excel_response['Female_Pre-school'] = f_pre_school
    filter_school_level_by_age.excel_response['Female_Pre-school'].append(sum(f_pre_school))
    filter_school_level_by_age.excel_response['Female_Elementary'] = f_elementary
    filter_school_level_by_age.excel_response['Female_Elementary'].append(sum(f_elementary))
    filter_school_level_by_age.excel_response['Female_Junior_High_School'] = f_junior_high_schl
    filter_school_level_by_age.excel_response['Female_Junior_High_School'].append(sum(f_junior_high_schl))
    filter_school_level_by_age.excel_response['Female_Senior_High_School'] = f_senior_high_schl
    filter_school_level_by_age.excel_response['Female_Senior_High_School'].append(sum(f_senior_high_schl))
    filter_school_level_by_age.excel_response['Female_Vocational/Technical'] = f_vocational_tech
    filter_school_level_by_age.excel_response['Female_Vocational/Technical'].append(sum(f_vocational_tech))
    filter_school_level_by_age.excel_response['Female_College/University'] = f_college_university
    filter_school_level_by_age.excel_response['Female_College/University'].append(sum(f_college_university))

    pre_school_total = [m_pre_school[i] + f_pre_school[i] for i in range(len(m_pre_school))]
    elementary_total = [m_elementary[i] + f_elementary[i] for i in range(len(m_elementary))]
    junior_schl_total = [m_junior_high_schl[i] + f_junior_high_schl[i] for i in range(len(m_junior_high_schl))]
    senior_schl_total = [m_senior_high_schl[i] + f_senior_high_schl[i] for i in range(len(m_senior_high_schl))]
    vocational_total = [m_vocational_tech[i] + f_vocational_tech[i] for i in range(len(m_vocational_tech))]
    college_university_total = [m_college_university[i] + f_college_university[i] for i in
                                range(len(m_college_university))]

    filter_school_level_by_age.excel_response['Total_Pre-school'] = pre_school_total
    filter_school_level_by_age.excel_response['Total_Elementary'] = elementary_total
    filter_school_level_by_age.excel_response['Total_Junior_High_School'] = junior_schl_total
    filter_school_level_by_age.excel_response['Total_Senior_High_School'] = senior_schl_total
    filter_school_level_by_age.excel_response['Total_Vocational/Technical'] = vocational_total
    filter_school_level_by_age.excel_response['Total_College/University'] = college_university_total

    merged_data = pre_school_total + elementary_total + junior_schl_total + senior_schl_total + vocational_total + college_university_total
    filter_school_level_by_age.chart_response_left["total_population"] = \
        filter_school_level_by_age.chart_response_left[
            "total_population"] + sum(merged_data)

    filter_school_level_by_age.save()

def report_currently_enrolled_school_type_by_age(location_id):
    # CURRENTLY ENROLLED BY AGE, SEX AND SCHOOL TYPE
    filter_school_type_by_age = ReportHistory.objects.filter(
        location_id=location_id, report_category_id__category_slug=constants.CATEGORIES_SLUG[15]).first()
    # Male
    m_public = list(
        filter_school_type_by_age.chart_constant_left['Male']['Enrolled in public'].values())
    m_private = list(
        filter_school_type_by_age.chart_constant_left['Male']['Enrolled in private'].values())
    m_not_enrolled = list(
        filter_school_type_by_age.chart_constant_left['Male']['Not enrolled'].values())

    m_public_data = dict(label="Enrolled in public", backgroundColor=constants.CHART_BACKGROUND_COLOR[0],
                         stack="Male",
                         data=m_public)
    m_private_data = dict(label="Enrolled in private", backgroundColor=constants.CHART_BACKGROUND_COLOR[1],
                          stack="Male",
                          data=m_private)
    m_not_enrolled_data = dict(label="Not enrolled", backgroundColor=constants.CHART_BACKGROUND_COLOR[2],
                               stack="Male",
                               data=m_not_enrolled)

    # Female
    f_public = list(
        filter_school_type_by_age.chart_constant_left['Female']['Enrolled in public'].values())
    f_private = list(
        filter_school_type_by_age.chart_constant_left['Female']['Enrolled in private'].values())
    f_not_enrolled = list(
        filter_school_type_by_age.chart_constant_left['Female']['Not enrolled'].values())

    f_public_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[0],
                         stack="Female",
                         data=f_public)
    f_private_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[1],
                          stack="Female",
                          data=f_private)
    f_not_enrolled_data = dict(backgroundColor=constants.CHART_BACKGROUND_COLOR[2],
                               stack="Female",
                               data=f_not_enrolled)

    data = filter_school_type_by_age.chart_response_left['datasets']
    data.clear()
    data.extend((m_public_data, m_private_data, m_not_enrolled_data,
                 f_public_data, f_private_data, f_not_enrolled_data))

    # Excel
    filter_school_type_by_age.excel_response['Male_Enrolled_in_public'] = m_public
    filter_school_type_by_age.excel_response['Male_Enrolled_in_public'].append(sum(m_public))
    filter_school_type_by_age.excel_response['Male_Enrolled_in_private'] = m_private
    filter_school_type_by_age.excel_response['Male_Enrolled_in_private'].append(sum(m_private))
    filter_school_type_by_age.excel_response['Male_Not_enrolled'] = m_not_enrolled
    filter_school_type_by_age.excel_response['Male_Not_enrolled'].append(sum(m_not_enrolled))

    filter_school_type_by_age.excel_response['Female_Enrolled_in_public'] = f_public
    filter_school_type_by_age.excel_response['Female_Enrolled_in_public'].append(sum(f_public))
    filter_school_type_by_age.excel_response['Female_Enrolled_in_private'] = f_private
    filter_school_type_by_age.excel_response['Female_Enrolled_in_private'].append(sum(f_private))
    filter_school_type_by_age.excel_response['Female_Not_enrolled'] = f_not_enrolled
    filter_school_type_by_age.excel_response['Female_Not_enrolled'].append(sum(f_not_enrolled))

    enrolled_public_total = [m_public[i] + f_public[i] for i in range(len(m_public))]
    enrolled_private_total = [m_private[i] + f_private[i] for i in range(len(m_private))]
    not_enrolled_total = [m_not_enrolled[i] + f_not_enrolled[i] for i in range(len(m_not_enrolled))]

    filter_school_type_by_age.excel_response['Total_Enrolled_in_public'] = enrolled_public_total
    filter_school_type_by_age.excel_response['Total_Enrolled_in_private'] = enrolled_private_total
    filter_school_type_by_age.excel_response['Total_Not_enrolled'] = not_enrolled_total

    merged_data = enrolled_public_total + enrolled_private_total + not_enrolled_total
    filter_school_type_by_age.chart_response_left["total_population"] = \
        filter_school_type_by_age.chart_response_left[
            "total_population"] + sum(merged_data)

    filter_school_type_by_age.save()