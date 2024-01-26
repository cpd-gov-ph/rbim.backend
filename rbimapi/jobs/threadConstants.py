from datetime import datetime, date


def get_family_head(final_household_json):
    family_head = final_household_json[0]["category"][0]["page"][0]["section"][0]['questions'][0]['answers'][0][
        'answer_value']
    if family_head is not None:
        return family_head.strip()
    return family_head


def get_member_name(final_household_json, index):
    member_name = final_household_json[index]['member_name']
    if member_name is not None:
        return member_name.strip()
    return member_name


def get_member_gender(final_household_json, index):
    gender_ans = final_household_json[index]["category"][0]["page"][0]["section"][0]['questions'][2]['answers'][0][
        'answer_value']
    if gender_ans is not None:
        return gender_ans.strip()
    return gender_ans


def get_member_age(final_household_json, index):
    age_ans = final_household_json[index]["category"][0]["page"][0]["section"][0]['questions'][4]['answers'][0][
        'answer_value']
    if age_ans is not None:
        return age_ans.strip()
    return age_ans


def get_member_marital_status(final_household_json, index):
    marital_status_ans = \
        final_household_json[index]["category"][0]["page"][0]["section"][0]['questions'][7]['answers'][0][
            'answer_value']
    if marital_status_ans is not None:
        return marital_status_ans.strip()
    return marital_status_ans


def get_member_higheducation(final_household_json, index):
    high_education_ans = \
        final_household_json[index]["category"][1]["page"][0]["section"][0]['questions'][0]['answers'][0][
            'answer_value']
    if high_education_ans is not None:
        return high_education_ans.strip()
    return high_education_ans


def get_member_place_of_delivery(final_household_json, index):
    place_of_delivery_ans = \
        final_household_json[index]["category"][2]["page"][0]["section"][0]['questions'][0]['answers'][0][
            'answer_value']
    if place_of_delivery_ans is not None:
        return place_of_delivery_ans.strip()
    return place_of_delivery_ans


def get_member_birth_attendant(final_household_json, index):
    birth_attendant_ans = \
        final_household_json[index]["category"][2]["page"][0]["section"][0]['questions'][1]['answers'][0][
            'answer_value']
    if birth_attendant_ans is not None:
        return birth_attendant_ans.strip()
    return birth_attendant_ans


def get_member_immunization(final_household_json, index):
    immunization_ans = \
        final_household_json[index]["category"][2]["page"][0]["section"][0]['questions'][2]['answers'][0][
            'answer_value']
    if immunization_ans is not None:
        return immunization_ans.strip().title()
    return immunization_ans


def get_member_religion(final_household_json, index):
    religion_ans = final_household_json[index]["category"][0]["page"][0]["section"][0]['questions'][8]['answers'][0][
        'answer_value']
    if religion_ans is not None:
        return religion_ans.strip()
    return religion_ans


def get_member_ethnic(final_household_json, index):
    ethnic_ans = final_household_json[index]["category"][0]["page"][0]["section"][0]['questions'][9]['answers'][0][
        'answer_value']
    if ethnic_ans is not None:
        return ethnic_ans.strip().title()
    return ethnic_ans


def get_member_source_of_income(final_household_json, index):
    source_of_income_ans = \
        final_household_json[index]["category"][1]["page"][1]["section"][0]['questions'][1]['answers'][0][
            'answer_value']
    if source_of_income_ans is not None:
        return source_of_income_ans.strip()
    return source_of_income_ans


def get_member_status_of_work(final_household_json, index):
    status_of_work_ans = \
        final_household_json[index]["category"][1]["page"][1]["section"][0]['questions'][2]['answers'][0][
            'answer_value']
    if status_of_work_ans is not None:
        return status_of_work_ans.strip()
    return status_of_work_ans


def get_member_salary(final_household_json, index):
    salary_ans = \
        final_household_json[index]["category"][1]["page"][1]["section"][0]['questions'][0]['answers'][0][
            'answer_value']
    if salary_ans is not None:
        return salary_ans.strip()
    return salary_ans


def get_member_preganancy_count(final_household_json, index):
    preganancy_count_ans = \
        final_household_json[index]["category"][2]["page"][0]["section"][1]['questions'][0]['answers'][0][
            'answer_value']
    if preganancy_count_ans is not None:
        return preganancy_count_ans.strip()
    return preganancy_count_ans


def get_member_school_level(final_household_json, index):
    school_level_ans = \
        final_household_json[index]["category"][1]["page"][0]["section"][1]['questions'][1]['answers'][0][
            'answer_value']
    if school_level_ans is not None:
        return school_level_ans.strip()
    return school_level_ans


def get_member_school_type(final_household_json, index):
    school_type_ans = \
        final_household_json[index]["category"][1]["page"][0]["section"][1]['questions'][0]['answers'][0][
            'answer_value']
    if school_type_ans is not None:
        return school_type_ans.strip()
    return school_type_ans


def get_common_diseases(final_section_json):
    common_diseases_ans = final_section_json[2]["section"][0]['questions'][2]['answers'][0]['answer_value']
    if common_diseases_ans is not None:
        return common_diseases_ans.strip().title()
    return common_diseases_ans


def get_primary_need(final_section_json):
    primary_needs_ans = final_section_json[2]["section"][0]['questions'][3]['answers'][0]['answer_value']
    if primary_needs_ans is not None:
        return primary_needs_ans.strip().title()
    return primary_needs_ans

def calculate_age(dob):
    date_object = datetime.strptime(dob, '%d/%m/%Y').date()
    today = date.today()
    return today.year - date_object.year - ((today.month, today.day) < (date_object.month, date_object.day))

def age_range_finder(age):
    age = calculate_age(age)
    if age in range(0, 5):
        return "0-4"
    if age in range(5, 10):
        return "5-9"
    if age in range(10, 15):
        return "10-14"
    if age in range(15, 20):
        return "15-19"
    if age in range(20, 25):
        return "20-24"
    if age in range(25, 30):
        return "25-29"
    if age in range(30, 35):
        return "30-34"
    if age in range(35, 40):
        return "35-39"
    if age in range(40, 45):
        return "40-44"
    if age in range(45, 50):
        return "45-49"
    if age in range(50, 55):
        return "50-54"
    if age in range(55, 60):
        return "55-59"
    if age in range(60, 65):
        return "60-64"
    if age in range(65, 70):
        return "65-69"
    if age in range(70, 75):
        return "70-74"
    if age in range(75, 70):
        return "75-79"
    if age >= 80:
        return "80"


def age_range_finder_school(age):
    age = calculate_age(age)
    if age in range(3, 5):
        return "3-4"
    if age in range(5, 10):
        return "5-9"
    if age in range(10, 15):
        return "10-14"
    if age in range(15, 20):
        return "15-19"
    if age in range(20, 25):
        return "20-24"


def salary_range_finder(salary):
    if salary in range(1, 5000):
        return "Under-5k"
    if salary in range(5000, 10000):
        return "5000-9999"
    if salary in range(10000, 15000):
        return "10000-14999"
    if salary in range(15000, 20000):
        return "15000-19999"
    if salary in range(20000, 25000):
        return "20000-24999"
    if salary >= 25000:
        return "25000-Above"
    return "25000-Above"


def preganancy_range_finder(preganancy_count):
    if preganancy_count in range(1, 2):
        return "1-Time-Preganant"
    if preganancy_count in range(2, 3):
        return "2-Time-Preganant"
    if preganancy_count in range(3, 4):
        return "3-Time-Preganant"
    if preganancy_count in range(4, 5):
        return "4-Time-Preganant"
    if preganancy_count in range(5, 6):
        return "5-Time-Preganant"
    if preganancy_count in range(6, 7):
        return "6-Time-Preganant"
    if preganancy_count in range(7, 8):
        return "7-Time-Preganant"
    if preganancy_count in range(8, 9):
        return "8-Time-Preganant"
    if preganancy_count in range(9, 10):
        return "9-Time-Preganant"
    if preganancy_count >= 10:
        return "10-Time-Preganant"
    return "10-Time-Preganant"


def school_type_finder(school_type):
    if school_type == "Yes, public":
        return "Enrolled in public"
    if school_type == "Yes, private":
        return "Enrolled in private"
    if school_type == "No":
        return "Not enrolled"
    return "Not enrolled"


def emptydatalist(n):
    listofzeros = [0] * n
    return listofzeros
