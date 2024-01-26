from rbim.models import SurveyMaster, Section, SurveyEntry, CensusStaticCategory
from rbim.models import CensusMember
import constants
def mdb_suvery_questions(param):
    survey_master_info = {}
    survey_master_info = SurveyMaster.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$project':{
                '_id' : 0,
                'id': { '$ifNull': [ "$id", None ] },
                'category_name': { '$ifNull': [ "$category_name", None ] },
                'position': { '$ifNull': [ "$position", None ] },
                'page':{ '$ifNull': [ "$page", None ] }
            }
        },
        {
            '$sort':{'position':1}
        }
    ])
    return list(survey_master_info)

def mdb_section(param):
    section_info = {}
    section_info = Section.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$lookup':
            {
                'from': "rbim_surveymaster",
                'let': { 'survey_master_id': "$survey_master_id"},
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': [ "$id",  "$$survey_master_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'category_name': { '$ifNull': [ "$category_name", None ] }
                        }
                    }
                ],
                'as': "rbim_surveymaster"
             }
        },
        {
            '$unwind':{
                'path' : '$rbim_surveymaster',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$project':{
                '_id' : 0,
                'id': { '$ifNull': [ "$id", None ] },
                'survey_master_id': { '$ifNull': [ "$survey_master_id", None ] },
                'category_name': { '$ifNull': [ "$rbim_surveymaster.category_name", None ] },
                'section_name': { '$ifNull': [ "$section_name", None ] },
                'position': { '$ifNull': [ "$position", None ] },
                'is_subheader': { '$ifNull': [ "$is_subheader", None ] },
                'questions': { '$ifNull': [ "$questions", None ] }
            }
        }
    ])
    return list(section_info)
    
def mdb_suvery_static_all_questions(param):
    survey_master_info = {}
    survey_master_info = SurveyMaster.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$lookup':
            {
                'from': "rbim_section",
                'let': { 'survey_master_id': "$id"},
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': [ "$survey_master_id",  "$$survey_master_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'section_name': { '$ifNull': [ "$section_name", None ] },
                            'is_subheader': { '$ifNull': [ "$is_subheader", None ] },
                            'position': { '$ifNull': [ "$position", None ] },
                            'qcount': { '$ifNull': [ "$qcount", None ] },
                            'anscount': { '$ifNull': [ "$anscount", None ] },
                            'questions': {
                                "$map": {
                                "input": "$questions",
                                "as": "qus",
                                    "in": {
                                        'qno': { '$ifNull': [ "$$qus.qno", None ] },
                                        'title': { '$ifNull': [ "$$qus.title", None ] },
                                        'is_required': { '$ifNull': [ "$$qus.is_required", None ] },
                                        'is_read_only': { '$ifNull': [ "$$qus.is_read_only", None ] },
                                        'position': { '$ifNull': [ "$$qus.position", None ] },
                                        'others_status': { '$ifNull': [ "$$qus.others_status", None ] },
                                        'qn_ranking': { '$ifNull': [ "$$qus.qn_ranking", None ] },
                                        'answers': {
                                            "$map": {
                                            "input": "$$qus.answers",
                                            "as": "ans",
                                                "in": {
                                                    'dtype': { '$ifNull': [ "$$ans.dtype", None ] },
                                                    'position': { '$ifNull': [ "$$ans.position", None ] },
                                                    'placeholder': { '$ifNull': [ "$$ans.placeholder", None ] },
                                                    'options': { '$ifNull': [ "$$ans.options", None ] },
                                                    'answer_value': { '$ifNull': [ "$$ans.answer_value", None ] },
                                                    'is_error': { '$ifNull': [ "$$ans.is_error", None ] },
                                                    'error_message': { '$ifNull': [ "$$ans.error_message", None ] },
                                                    'keyboard_type': { '$ifNull': [ "$$ans.keyboard_type", None ] },
                                                    'limitation': { '$ifNull': [ "$$ans.limitation", None ] },
                                                    'show_dropdown_modal': { '$ifNull': [ "$$ans.show_dropdown_modal", None ] },
                                                    'show_time_picker': { '$ifNull': [ "$$ans.show_time_picker", None ] },
                                                    'show_multi_dropdown_modal': { '$ifNull': [ "$$ans.show_multi_dropdown_modal", None ] },
                                                    'show_picker': { '$ifNull': [ "$$ans.show_picker", None ] },
                                                    'ranking': { '$ifNull': [ "$$ans.ranking", None ] }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    {
                        '$sort':{'position':1}
                    }
                ],
                'as': "rbim_section"
             }
        },
        {
            '$project':{
                '_id' : 0,
                'category_name': { '$ifNull': [ "$category_name", None ] },
                'position': { '$ifNull': [ "$position", None ] },
                'page':{ '$ifNull': [ "$page", None ] },
                'section':{ '$ifNull': [ "$rbim_section", None ] }
            }
        },
        {
            '$sort':{'position':1}
        }
    ])
    return list(survey_master_info)
   
def mdb_hh_suvery_static_all_questions(param):
    survey_master_info = {}
    survey_master_info = SurveyMaster.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$lookup':
            {
                'from': "rbim_section",
                'let': { 'survey_master_id': "$id"},
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': [ "$survey_master_id",  "$$survey_master_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'section_name': { '$ifNull': [ "$section_name", None ] },
                            'is_subheader': { '$ifNull': [ "$is_subheader", None ] },
                            'position': { '$ifNull': [ "$position", None ] },
                            'qcount': { '$ifNull': [ "$qcount", None ] },
                            'anscount': { '$ifNull': [ "$anscount", None ] },
                            'questions': {
                                "$map": {
                                "input": "$questions",
                                "as": "qus",
                                    "in": {
                                        'qno': { '$ifNull': [ "$$qus.qno", None ] },
                                        'title': { '$ifNull': [ "$$qus.title", None ] },
                                        'is_required': { '$ifNull': [ "$$qus.is_required", None ] },
                                        'is_read_only': { '$ifNull': [ "$$qus.is_read_only", None ] },
                                        'position': { '$ifNull': [ "$$qus.position", None ] },
                                        'others_status': { '$ifNull': [ "$$qus.others_status", None ] },
                                        'qn_ranking': { '$ifNull': [ "$$qus.qn_ranking", None ] },
                                        'answers': {
                                            "$map": {
                                            "input": "$$qus.answers",
                                            "as": "ans",
                                                "in": {
                                                    'dtype': { '$ifNull': [ "$$ans.dtype", None ] },
                                                    'position': { '$ifNull': [ "$$ans.position", None ] },
                                                    'placeholder': { '$ifNull': [ "$$ans.placeholder", None ] },
                                                    'options': { '$ifNull': [ "$$ans.options", None ] },
                                                    'answer_value': { '$ifNull': [ "$$ans.answer_value", None ] },
                                                    'is_error': { '$ifNull': [ "$$ans.is_error", None ] },
                                                    'error_message': { '$ifNull': [ "$$ans.error_message", None ] },
                                                    'keyboard_type': { '$ifNull': [ "$$ans.keyboard_type", None ] },
                                                    'limitation': { '$ifNull': [ "$$ans.limitation", None ] },
                                                    'show_dropdown_modal': { '$ifNull': [ "$$ans.show_dropdown_modal", None ] },
                                                    'show_time_picker': { '$ifNull': [ "$$ans.show_time_picker", None ] },
                                                    'show_multi_dropdown_modal': { '$ifNull': [ "$$ans.show_multi_dropdown_modal", None ] },
                                                    'show_picker': { '$ifNull': [ "$$ans.show_picker", None ] },
                                                    'ranking': { '$ifNull': [ "$$ans.ranking", None ] }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    {
                        '$sort':{'position':1}
                    }
                ],
                'as': "rbim_section"
             }
        },
        {
            '$project':{
                '_id' : 0,
                'category_name': { '$ifNull': [ "$category_name", None ] },
                'position': { '$ifNull': [ "$position", None ] },
                'page':{ '$ifNull': [ "$page", None ] },
                'section':{ '$ifNull': [ "$rbim_section", None ] }
            }
        },
        {
            '$sort':{'position':1}
        },
        {
            '$group':{
                '_id':'$page',
                'page':{
                    "$push":{
                        'category_name': { '$ifNull': [ "$category_name", None ] },
                        'position': { '$ifNull': [ "$position", None ] },
                        'page':{ '$ifNull': [ "$page", None ] },
                        'section':{ '$ifNull': [ "$section", None ] }
                    }
                }
            }
        },
        {
            '$sort':{'_id':1}
        }

    ])
    return list(survey_master_info)

def mdb_suvery_list_count(param):
    survey_count = {}
    survey_count = SurveyEntry.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$project':{
                '_id' : 0,
                'id': { '$ifNull': [ "$id", None ] },
            }
        }
    ])
    count = 0
    count = len(list(survey_count))
    return count

def mdb_suvery_list(param):
    survey_list = {}
    survey_list = SurveyEntry.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$lookup':
            {
                'from': "rbim_profile",
                'let': { 'data_collector_id': "$data_collector_id"},
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': [ "$user_id",  "$$data_collector_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'official_number': { '$ifNull': [ "$official_number", None ] }
                        }
                    }
                ],
                'as': "data_collector"
             }
        },
        {
            '$unwind':{
                'path' : '$data_collector',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$lookup':
            {
                'from': "rbim_profile",
                'let': { 'data_reviewer_id': "$data_reviewer_id"},
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': [ "$user_id",  "$$data_reviewer_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'official_number': { '$ifNull': [ "$official_number", None ] }
                        }
                    }
                ],
                'as': "data_reviewer"
             }
        },
        {
            '$unwind':{
                'path' : '$data_reviewer',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$lookup':
                {
                    'from': "rbim_ocrmaster",
                    'let': {'survey_entry_id': "$id"},
                    'pipeline': [
                        {
                            '$match': {
                                '$expr': {
                                    '$and': [
                                        {'$eq': ["$survey_entry_id", "$$survey_entry_id"]}
                                    ]
                                }
                            }
                        },
                        {
                            '$project': {
                                '_id': 0,
                                'ocr_images': {'$ifNull': ["$ocr_images", None]},
                            }
                        }
                    ],
                    'as': "rbim_ocr_master_data"
                }
        },
        {
            '$unwind': {
                'path': '$rbim_ocr_master_data',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$sort': param['sort']
        },
        {
            '$skip':param['skip']
        },
        {
            '$limit':param['page_size']
        },
        {
            '$project':{
                '_id' : 0,
                'id': { '$ifNull': [ "$id", None ] },
                'survey_number': { '$ifNull': [ "$survey_number", None ] },
                'status': { '$ifNull': [ "$status", None ] },
                'data_collector': { '$ifNull': [ "$data_collector", None ] },
                'data_reviewer': { '$ifNull': [ "$data_reviewer", None ] },
                'survey_type': { '$ifNull': [ "$survey_type", None ] },
                'survey_assigned_on': { '$ifNull': [ "$survey_assigned_on", None ] },
                'survey_review_started_on': { '$ifNull': [ "$survey_review_started_on", None ] },
                'survey_review_submitted_on': { '$ifNull': [ "$survey_review_submitted_on", None ] },
                'survey_rejected_on': { '$ifNull': [ "$survey_rejected_on", None ] },
                'pending_for_approval_on': { '$ifNull': [ "$pending_for_approval_on", None ] },
                'survey_verification_started_on': { '$ifNull': [ "$survey_verification_started_on", None ] },
                'survey_completed_on': { '$ifNull': [ "$survey_completed_on", None ] },
                'enable_recorrection_flag': { '$ifNull': [ "$enable_recorrection_flag", False ] },
                'is_open_individual_view': { '$ifNull': [ "$is_open_ndividual_view", False ] },
                'ocr_status': { '$ifNull': [ "$ocr_status", False ] },
                'ocr_images': { '$ifNull': [ "$rbim_ocr_master_data.ocr_images", None ] }
            }
        }
    ])
    return list(survey_list)

def mdb_suvery_entry_details(param):
    survey_entry_details = {}
    survey_entry_details = SurveyEntry.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$lookup':
                {
                    'from': "rbim_ocrmaster",
                    'let': {'survey_entry_id': "$id"},
                    'pipeline': [
                        {
                            '$match': {
                                '$expr': {
                                    '$and': [
                                        {'$eq': ["$survey_entry_id", "$$survey_entry_id"]}
                                    ]
                                }
                            }
                        },
                        {
                            '$project': {
                                '_id': 0,
                                'ocr_images': {'$ifNull': ["$ocr_images", None]},
                            }
                        }
                    ],
                    'as': "rbim_ocr_master_data"
                }
        },
        {
            '$unwind': {
                'path': '$rbim_ocr_master_data',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$project':{
                '_id' : 0,
                'id': { '$ifNull': [ "$id", None ] },
                'survey_number': { '$ifNull': [ "$survey_number", None ] },
                'data_collector_id': { '$ifNull': [ "$data_collector_id", None ] },
                'data_reviewer_id': { '$ifNull': [ "$data_reviewer_id", None ] },
                'survey_type': { '$ifNull': [ "$survey_type", None ] },
                'household_member_count': { '$ifNull': [ "$household_member_count", None ] },
                'data_collector_signature': { '$ifNull': [ "$data_collector_signature", None ] },
                'signature': { '$ifNull': [ "$signature", None ] },
                'signature_recorrection_flag': { '$ifNull': [ "$signature_recorrection_flag", None ] },
                'mobile_next_section': { '$ifNull': [ "$mobile_next_section", None ] },
                'next_section': { '$ifNull': [ "$next_section", None ] },
                'inner_next_section': { '$ifNull': [ "$inner_next_section", None ] },
                'is_recorrection_members': { '$ifNull': [ "$is_recorrection_members", False ] },
                'data_reviewer_signature': { '$ifNull': [ "$data_reviewer_signature", None ] },
                'notes': { '$ifNull': [ "$notes", None ] },
                'personindex': { '$ifNull': [ "$personindex", None ] },
                'pageindex': { '$ifNull': [ "$pageindex", None ] },
                'members': { '$ifNull': [ "$members", None ] },
                'ocr_images': {'$ifNull': ["$rbim_ocr_master_data.ocr_images", None]}
            }
        }
    ])
    return list(survey_entry_details)
    
def mdb_census_static_category_details(param):
    survey_entry_details = {}
    survey_entry_details = CensusStaticCategory.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$lookup':
            {
                'from': "rbim_censusstaticsections",
                'let': { 
                    'survey_entry_id': "$survey_entry_id",
                    'census_static_category_id': "$id",
                    'part': "$part",
                },
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                    {'$eq': ["$census_static_category_id",  "$$census_static_category_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                            'census_static_category_id': { '$ifNull': [ "$census_static_category_id", None ] },
                            'section_name': { '$ifNull': [ "$section_name", None ] },
                            'is_enable': { '$ifNull': [ "$is_enable", None ] },
                            'is_subheader': { '$ifNull': [ "$is_subheader", None ] },
                            'is_recorrection': { '$ifNull': [ "$is_recorrection", None ] },
                            'position': { '$ifNull': [ "$position", None ] },
                            'qcount': { '$ifNull': [ "$qcount", None ] },
                            'anscount': { '$ifNull': [ "$anscount", None ] },
                            'questions': {
                                "$map": {
                                "input": "$questions",
                                "as": "qus",
                                    "in": {
                                        'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                        'category_id': { '$ifNull': [ "$census_static_category_id", None ] },
                                        'section_id': { '$ifNull': [ "$id", None ] },
                                        'question_id': { '$ifNull': [ "$$qus.id", None ] },
                                        'part': { '$ifNull': [ "$$part", None ] },
                                        'qno': { '$ifNull': [ "$$qus.qno", None ] },
                                        'title': { '$ifNull': [ "$$qus.title", None ] },
                                        'is_required': { '$ifNull': [ "$$qus.is_required", None ] },
                                        'answers': { '$ifNull': [ "$$qus.answers", None ] },
                                        'position': { '$ifNull': [ "$$qus.position", None ] },
                                        'is_read_only': { '$ifNull': [ "$$qus.is_read_only", None ] },
                                        'is_approved': { '$ifNull': [ "$$qus.is_approved", None ] },
                                        'is_rejected': { '$ifNull': [ "$$qus.is_rejected", None ] },
                                        'is_reviewed_by_barangay': { '$ifNull': [ "$$qus.is_reviewed_by_barangay", None ] },
                                        'reject_reason': { '$ifNull': [ "$$qus.reject_reason", None ] },
                                        'approved_date': { '$ifNull': [ "$$qus.approved_date", None ] },
                                        'rejected_date': { '$ifNull': [ "$$qus.rejected_date", None ] },
                                        'others_status': { '$ifNull': [ "$$qus.others_status", None ] },
                                        'qn_ranking': { '$ifNull': [ "$$qus.qn_ranking", None ] },
                                        'is_qn_enable': { '$ifNull': [ "$$qus.is_qn_enable", None ] },
                                        'created_at': { '$ifNull': [ "$$qus.created_at", None ] },
                                        'updated_at': { '$ifNull': [ "$$qus.updated_at", None ] },
                                        'is_deleted': { '$ifNull': [ "$$qus.is_deleted", None ] },
                                    }
                                }
                            }
                        }
                    },
                    {
                        '$sort':{'position':1}
                    }
                ],
                'as': "section"
             }
        },
        {
            '$project':{
                '_id' : 0,
                'id': { '$ifNull': [ "$id", None ] },
                'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                'category_name': { '$ifNull': [ "$category_name", None ] },
                'position': { '$ifNull': [ "$position", None ] },
                'page': { '$ifNull': [ "$page", None ] },
                'part': { '$ifNull': [ "$part", None ] },
                'section': { '$ifNull': [ "$section", None ] },
            }
        },
        {
            '$sort':{'position':1}
        }
    ])
    return list(survey_entry_details)
    
def mdb_house_hold_member_section_details(param):
    census_member_details = {}
    census_member_details = CensusMember.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$lookup':
            {
                'from': "rbim_censuscategory",
                'let': { 
                    'survey_entry_id': "$survey_entry_id",
                    'census_member_id': "$id",
                },
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                    {'$eq': ["$census_member_id",  "$$census_member_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$lookup':
                        {
                            'from': "rbim_censussections",
                            'let': { 
                                'survey_entry_id': "$survey_entry_id",
                                'census_category_id': "$id",
                                'part': "$part",
                            },
                            'pipeline': [
                                { 
                                    '$match': { 
                                        '$expr': { 
                                            '$and': [
                                                {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                                {'$eq': ["$census_category_id",  "$$census_category_id" ] }
                                            ]
                                        }
                                    }
                                },
                                {
                                    '$project':{
                                        '_id' : 0,
                                        'id': { '$ifNull': [ "$id", None ] },
                                        'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                        'census_category_id': { '$ifNull': [ "$census_category_id", None ] },
                                        'section_name': { '$ifNull': [ "$section_name", None ] },
                                        'is_enable': { '$ifNull': [ "$is_enable", None ] },
                                        'is_subheader': { '$ifNull': [ "$is_subheader", None ] },
                                        'is_recorrection': { '$ifNull': [ "$is_recorrection", None ] },
                                        'position': { '$ifNull': [ "$position", None ] },
                                        'qcount': { '$ifNull': [ "$qcount", None ] },
                                        'anscount': { '$ifNull': [ "$anscount", None ] },
                                        'questions': {
                                            "$map": {
                                            "input": "$questions",
                                            "as": "qus",
                                                "in": {
                                                    'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                                    'category_id': { '$ifNull': [ "$census_category_id", None ] },
                                                    'section_id': { '$ifNull': [ "$id", None ] },
                                                    'question_id': { '$ifNull': [ "$$qus.id", None ] },
                                                    'part': { '$ifNull': [ "$$part", None ] },
                                                    'qno': { '$ifNull': [ "$$qus.qno", None ] },
                                                    'title': { '$ifNull': [ "$$qus.title", None ] },
                                                    'is_required': { '$ifNull': [ "$$qus.is_required", None ] },
                                                    'answers': { '$ifNull': [ "$$qus.answers", None ] },
                                                    'position': { '$ifNull': [ "$$qus.position", None ] },
                                                    'is_read_only': { '$ifNull': [ "$$qus.is_read_only", None ] },
                                                    'is_approved': { '$ifNull': [ "$$qus.is_approved", None ] },
                                                    'is_rejected': { '$ifNull': [ "$$qus.is_rejected", None ] },
                                                    'is_reviewed_by_barangay': { '$ifNull': [ "$$qus.is_reviewed_by_barangay", None ] },
                                                    'reject_reason': { '$ifNull': [ "$$qus.reject_reason", None ] },
                                                    'approved_date': { '$ifNull': [ "$$qus.approved_date", None ] },
                                                    'rejected_date': { '$ifNull': [ "$$qus.rejected_date", None ] },
                                                    'others_status': { '$ifNull': [ "$$qus.others_status", None ] },
                                                    'qn_ranking': { '$ifNull': [ "$$qus.qn_ranking", None ] },
                                                    'is_qn_enable': { '$ifNull': [ "$$qus.is_qn_enable", None ] },         
                                                    'created_at': { '$ifNull': [ "$$qus.created_at", None ] },
                                                    'updated_at': { '$ifNull': [ "$$qus.updated_at", None ] },
                                                    'is_deleted': { '$ifNull': [ "$$qus.is_deleted", None ] },
                                                }
                                            }
                                        }
                                    }
                                },
                                {
                                    '$sort':{'position':1}
                                }
                            ],
                            'as': "section"
                        }
                    },
                    {
                        '$sort':{'position':1}
                    },
                    {
                        '$group':{
                            '_id':'$page',
                            'page':{
                                "$push":{
                                    'id': { '$ifNull': [ "$id", None ] },
                                    'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                    'census_member_id': { '$ifNull': [ "$census_member_id", None ] },
                                    'category_name': { '$ifNull': [ "$category_name", None ] },
                                    'position': { '$ifNull': [ "$position", None ] },
                                    'page': { '$ifNull': [ "$page", None ] },
                                    'part': { '$ifNull': [ "$part", None ] },
                                    'section': { '$ifNull': [ "$section", None ] }
                                }
                            }
                        }
                    },
                    {
                        '$sort':{'_id':1}
                    }
                ],
                'as': "category"
             }
        },
        {
            '$project':{
                '_id' : 0,
                'id': { '$ifNull': [ "$id", None ] },
                'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                'member_id': { '$ifNull': [ "$member_id", None ] },
                'member_name': { '$ifNull': [ "$member_name", None ] },
                'category': { '$ifNull': [ "$category", None ] },
            }
        }
    ])
    return list(census_member_details)
 
def mdb_survey_home_dashboard_list_count(param):
    ongoin_survey_count = {}
    ongoin_survey_count = SurveyEntry.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$project':{
                '_id' : 0,
                'id': { '$ifNull': [ "$id", None ] },
                'survey_number': { '$ifNull': [ "$survey_number", None ] },
            }
        }
    ])
    count = 0
    count = len(list(ongoin_survey_count))
    return count

def mdb_survey_home_dashboard_list(param):
    survey_home_dashboard_list = {}
    survey_home_dashboard_list = SurveyEntry.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$sort': param['sort']
        },
        {
            '$skip':param['skip']
        },
        {
            '$limit':param['page_size']
        },
        {
            '$project':{
                '_id' : 0,
                'id': { '$ifNull': [ "$id", None ] },
                'survey_number': { '$ifNull': [ "$survey_number", None ] },
            }
        }
    ])
    return list(survey_home_dashboard_list)

def mdb_suvery_recorrection_details(param):
    survey_entry_details = {}
    survey_entry_details = SurveyEntry.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$addFields':{
                'survey_entry_id': { '$ifNull': [ "$id", None ] },
            }
        },
        {
            '$lookup':
            {
                'from': "rbim_censusstaticcategory",
                'let': { 
                    'survey_entry_id': "$survey_entry_id"
                },
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                    {'$eq': ["$part",  "initial_section" ] },
                                ]
                            }
                        }
                    },
                    {
                        '$addFields':{
                            'census_static_category_id': { '$ifNull': [ "$id", None ] },
                        }
                    },
                    {
                        '$lookup':
                        {
                            'from': "rbim_censusstaticsections",
                            'let': { 
                                'survey_entry_id': "$survey_entry_id",
                                'census_static_category_id': "$census_static_category_id",
                                'part': "$part",
                            },
                            'pipeline': [
                                { 
                                    '$match': { 
                                        '$expr': { 
                                            '$and': [
                                                {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                                {'$eq': ["$census_static_category_id",  "$$census_static_category_id" ] }
                                            ]
                                        }
                                    }
                                },
                                {
                                    '$project':{
                                        '_id' : 0,
                                        'id': { '$ifNull': [ "$id", None ] },
                                        'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                        'census_static_category_id': { '$ifNull': [ "$census_static_category_id", None ] },
                                        'section_name': { '$ifNull': [ "$section_name", None ] },
                                        'is_enable': { '$ifNull': [ "$is_enable", None ] },
                                        'is_subheader': { '$ifNull': [ "$is_subheader", None ] },
                                        'is_recorrection': { '$ifNull': [ "$is_recorrection", None ] },
                                        'position': { '$ifNull': [ "$position", None ] },
                                        'qcount': { '$ifNull': [ "$qcount", None ] },
                                        'anscount': { '$ifNull': [ "$anscount", None ] },
                                        'questions': {
                                            "$map": {
                                            "input": "$questions",
                                            "as": "qus",
                                                "in": {
                                                    'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                                    'category_id': { '$ifNull': [ "$census_static_category_id", None ] },
                                                    'section_id': { '$ifNull': [ "$id", None ] },
                                                    'question_id': { '$ifNull': [ "$$qus.id", None ] },
                                                    'part': { '$ifNull': [ "$$part", None ] },
                                                    'qno': { '$ifNull': [ "$$qus.qno", None ] },
                                                    'title': { '$ifNull': [ "$$qus.title", None ] },
                                                    'is_required': { '$ifNull': [ "$$qus.is_required", None ] },
                                                    'answers': { '$ifNull': [ "$$qus.answers", None ] },
                                                    'position': { '$ifNull': [ "$$qus.position", None ] },
                                                    'is_read_only': { '$ifNull': [ "$$qus.is_read_only", None ] },
                                                    'is_approved': { '$ifNull': [ "$$qus.is_approved", None ] },
                                                    'is_rejected': { '$ifNull': [ "$$qus.is_rejected", None ] },
                                                    'is_reviewed_by_barangay': { '$ifNull': [ "$$qus.is_reviewed_by_barangay", None ] },
                                                    'reject_reason': { '$ifNull': [ "$$qus.reject_reason", None ] },
                                                    'approved_date': { '$ifNull': [ "$$qus.approved_date", None ] },
                                                    'rejected_date': { '$ifNull': [ "$$qus.rejected_date", None ] },
                                                    'others_status': { '$ifNull': [ "$$qus.others_status", None ] },
                                                    'is_qn_enable': { '$ifNull': [ "$$qus.is_qn_enable", None ] },                                       
                                                    'created_at': { '$ifNull': [ "$$qus.created_at", None ] },
                                                    'updated_at': { '$ifNull': [ "$$qus.updated_at", None ] },
                                                    'is_deleted': { '$ifNull': [ "$$qus.is_deleted", None ] },
                                                }
                                            }
                                        }
                                    }
                                },
                                {
                                    '$sort':{'position':1}
                                }
                            ],
                            'as': "section"
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                            'category_name': { '$ifNull': [ "$category_name", None ] },
                            'position': { '$ifNull': [ "$position", None ] },
                            'page': { '$ifNull': [ "$page", None ] },
                            'part': { '$ifNull': [ "$part", None ] },
                            'section': { '$ifNull': [ "$section", None ] },
                        }
                    },
                    {
                        '$sort':{'position':1}
                    }
                ],
                'as':'initial_section'
            }
        },
        {
            '$unwind':{
                'path' : '$initial_section',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$lookup':
            {
                'from': "rbim_censusstaticcategory",
                'let': { 
                    'survey_entry_id': "$survey_entry_id"
                },
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                    {'$eq': ["$part",  "interview_section" ] },
                                ]
                            }
                        }
                    },
                    {
                        '$addFields':{
                            'census_static_category_id': { '$ifNull': [ "$id", None ] },
                        }
                    },
                    {
                        '$lookup':
                        {
                            'from': "rbim_censusstaticsections",
                            'let': { 
                                'survey_entry_id': "$survey_entry_id",
                                'census_static_category_id': "$census_static_category_id",
                                'part': "$part",
                            },
                            'pipeline': [
                                { 
                                    '$match': { 
                                        '$expr': { 
                                            '$and': [
                                                {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                                {'$eq': ["$census_static_category_id",  "$$census_static_category_id" ] }
                                            ]
                                        }
                                    }
                                },
                                {
                                    '$project':{
                                        '_id' : 0,
                                        'id': { '$ifNull': [ "$id", None ] },
                                        'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                        'census_static_category_id': { '$ifNull': [ "$census_static_category_id", None ] },
                                        'section_name': { '$ifNull': [ "$section_name", None ] },
                                        'is_enable': { '$ifNull': [ "$is_enable", None ] },
                                        'is_subheader': { '$ifNull': [ "$is_subheader", None ] },
                                        'is_recorrection': { '$ifNull': [ "$is_recorrection", None ] },
                                        'position': { '$ifNull': [ "$position", None ] },
                                        'qcount': { '$ifNull': [ "$qcount", None ] },
                                        'anscount': { '$ifNull': [ "$anscount", None ] },
                                        'questions': {
                                            "$map": {
                                            "input": "$questions",
                                            "as": "qus",
                                                "in": {
                                                    'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                                    'category_id': { '$ifNull': [ "$census_static_category_id", None ] },
                                                    'section_id': { '$ifNull': [ "$id", None ] },
                                                    'question_id': { '$ifNull': [ "$$qus.id", None ] },
                                                    'part': { '$ifNull': [ "$$part", None ] },
                                                    'qno': { '$ifNull': [ "$$qus.qno", None ] },
                                                    'title': { '$ifNull': [ "$$qus.title", None ] },
                                                    'is_required': { '$ifNull': [ "$$qus.is_required", None ] },
                                                    'answers': { '$ifNull': [ "$$qus.answers", None ] },
                                                    'position': { '$ifNull': [ "$$qus.position", None ] },
                                                    'is_read_only': { '$ifNull': [ "$$qus.is_read_only", None ] },
                                                    'is_approved': { '$ifNull': [ "$$qus.is_approved", None ] },
                                                    'is_rejected': { '$ifNull': [ "$$qus.is_rejected", None ] },
                                                    'is_reviewed_by_barangay': { '$ifNull': [ "$$qus.is_reviewed_by_barangay", None ] },
                                                    'reject_reason': { '$ifNull': [ "$$qus.reject_reason", None ] },
                                                    'approved_date': { '$ifNull': [ "$$qus.approved_date", None ] },
                                                    'rejected_date': { '$ifNull': [ "$$qus.rejected_date", None ] },
                                                    'others_status': { '$ifNull': [ "$$qus.others_status", None ] },
                                                    'is_qn_enable': { '$ifNull': [ "$$qus.is_qn_enable", None ] },                                        
                                                    'created_at': { '$ifNull': [ "$$qus.created_at", None ] },
                                                    'updated_at': { '$ifNull': [ "$$qus.updated_at", None ] },
                                                    'is_deleted': { '$ifNull': [ "$$qus.is_deleted", None ] },
                                                }
                                            }
                                        }
                                    }
                                },
                                {
                                    '$sort':{'position':1}
                                }
                            ],
                            'as': "section"
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                            'category_name': { '$ifNull': [ "$category_name", None ] },
                            'position': { '$ifNull': [ "$position", None ] },
                            'page': { '$ifNull': [ "$page", None ] },
                            'part': { '$ifNull': [ "$part", None ] },
                            'section': { '$ifNull': [ "$section", None ] },
                        }
                    },
                    {
                        '$sort':{'position':1}
                    }
                ],
                'as':'interview_section'
            }
        },
        {
            '$lookup':{
               'from': "rbim_censusmember",
                'let': { 
                    'survey_entry_id': "$survey_entry_id"
                }, 
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$addFields':{
                            'census_member_id': { '$ifNull': [ "$id", None ] },
                        }
                    },
                    {
                        '$lookup':
                        {
                            'from': "rbim_censuscategory",
                            'let': { 
                                'survey_entry_id': "$survey_entry_id",
                                'census_member_id': "$census_member_id",
                            },
                            'pipeline': [
                                { 
                                    '$match': { 
                                        '$expr': { 
                                            '$and': [
                                                {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                                {'$eq': ["$census_member_id",  "$$census_member_id" ] }
                                            ]
                                        }
                                    }
                                },
                                {
                                    '$lookup':
                                    {
                                        'from': "rbim_censussections",
                                        'let': { 
                                            'survey_entry_id': "$survey_entry_id",
                                            'census_category_id': "$id",
                                            'part': "$part",
                                        },
                                        'pipeline': [
                                            { 
                                                '$match': { 
                                                    '$expr': { 
                                                        '$and': [
                                                            {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                                            {'$eq': ["$census_category_id",  "$$census_category_id" ] }
                                                        ]
                                                    }
                                                }
                                            },
                                            {
                                                '$project':{
                                                    '_id' : 0,
                                                    'id': { '$ifNull': [ "$id", None ] },
                                                    'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                                    'census_category_id': { '$ifNull': [ "$census_category_id", None ] },
                                                    'section_name': { '$ifNull': [ "$section_name", None ] },
                                                    'is_enable': { '$ifNull': [ "$is_enable", None ] },
                                                    'is_subheader': { '$ifNull': [ "$is_subheader", None ] },
                                                    'is_recorrection': { '$ifNull': [ "$is_recorrection", None ] },
                                                    'position': { '$ifNull': [ "$position", None ] },
                                                    'qcount': { '$ifNull': [ "$qcount", None ] },
                                                    'anscount': { '$ifNull': [ "$anscount", None ] },
                                                    'questions': {
                                                        "$map": {
                                                        "input": "$questions",
                                                        "as": "qus",
                                                            "in": {
                                                                'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                                                'category_id': { '$ifNull': [ "$census_category_id", None ] },
                                                                'section_id': { '$ifNull': [ "$id", None ] },
                                                                'question_id': { '$ifNull': [ "$$qus.id", None ] },
                                                                'part': { '$ifNull': [ "$$part", None ] },
                                                                'qno': { '$ifNull': [ "$$qus.qno", None ] },
                                                                'title': { '$ifNull': [ "$$qus.title", None ] },
                                                                'is_required': { '$ifNull': [ "$$qus.is_required", None ] },
                                                                'answers': { '$ifNull': [ "$$qus.answers", None ] },
                                                                'position': { '$ifNull': [ "$$qus.position", None ] },
                                                                'is_read_only': { '$ifNull': [ "$$qus.is_read_only", None ] },
                                                                'is_approved': { '$ifNull': [ "$$qus.is_approved", None ] },
                                                                'is_rejected': { '$ifNull': [ "$$qus.is_rejected", None ] },
                                                                'is_reviewed_by_barangay': { '$ifNull': [ "$$qus.is_reviewed_by_barangay", None ] },
                                                                'reject_reason': { '$ifNull': [ "$$qus.reject_reason", None ] },
                                                                'approved_date': { '$ifNull': [ "$$qus.approved_date", None ] },
                                                                'rejected_date': { '$ifNull': [ "$$qus.rejected_date", None ] },
                                                                'others_status': { '$ifNull': [ "$$qus.others_status", None ] },
                                                                'is_qn_enable': { '$ifNull': [ "$$qus.is_qn_enable", None ] },                                                               
                                                                'created_at': { '$ifNull': [ "$$qus.created_at", None ] },
                                                                'updated_at': { '$ifNull': [ "$$qus.updated_at", None ] },
                                                                'is_deleted': { '$ifNull': [ "$$qus.is_deleted", None ] },
                                                            }
                                                        }
                                                    }
                                                }
                                            },
                                            {
                                                '$sort':{'position':1}
                                            }
                                        ],
                                        'as': "section"
                                    }
                                },
                                {
                                    '$sort':{'position':1}
                                },
                                {
                                    '$group':{
                                        '_id':'$page',
                                        'page':{
                                            "$push":{
                                                'id': { '$ifNull': [ "$id", None ] },
                                                'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                                'census_member_id': { '$ifNull': [ "$census_member_id", None ] },
                                                'category_name': { '$ifNull': [ "$category_name", None ] },
                                                'position': { '$ifNull': [ "$position", None ] },
                                                'page': { '$ifNull': [ "$page", None ] },
                                                'part': { '$ifNull': [ "$part", None ] },
                                                'section': { '$ifNull': [ "$section", None ] }
                                            }
                                        }
                                    }
                                },
                                {
                                    '$sort':{'_id':1}
                                }
                            ],
                            'as': "category"
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                            'member_id': { '$ifNull': [ "$member_id", None ] },
                            'member_name': { '$ifNull': [ "$member_name", None ] },
                            'category': { '$ifNull': [ "$category", None ] },
                        }
                    }
                ],
                'as':'house_hold_member_section'
            }
        },
        {
            '$lookup':
            {
                'from': "rbim_censusstaticcategory",
                'let': { 
                    'survey_entry_id': "$survey_entry_id"
                },
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                    {'$eq': ["$part",  "final_section" ] },
                                ]
                            }
                        }
                    },
                    {
                        '$addFields':{
                            'census_static_category_id': { '$ifNull': [ "$id", None ] },
                        }
                    },
                    {
                        '$lookup':
                        {
                            'from': "rbim_censusstaticsections",
                            'let': { 
                                'survey_entry_id': "$survey_entry_id",
                                'census_static_category_id': "$census_static_category_id",
                                'part': "$part",
                            },
                            'pipeline': [
                                { 
                                    '$match': { 
                                        '$expr': { 
                                            '$and': [
                                                {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                                {'$eq': ["$census_static_category_id",  "$$census_static_category_id" ] }
                                            ]
                                        }
                                    }
                                },
                                {
                                    '$project':{
                                        '_id' : 0,
                                        'id': { '$ifNull': [ "$id", None ] },
                                        'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                        'census_static_category_id': { '$ifNull': [ "$census_static_category_id", None ] },
                                        'section_name': { '$ifNull': [ "$section_name", None ] },
                                        'is_enable': { '$ifNull': [ "$is_enable", None ] },
                                        'is_subheader': { '$ifNull': [ "$is_subheader", None ] },
                                        'is_recorrection': { '$ifNull': [ "$is_recorrection", None ] },
                                        'position': { '$ifNull': [ "$position", None ] },
                                        'qcount': { '$ifNull': [ "$qcount", None ] },
                                        'anscount': { '$ifNull': [ "$anscount", None ] },
                                        'questions': {
                                            "$map": {
                                            "input": "$questions",
                                            "as": "qus",
                                                "in": {
                                                    'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                                    'category_id': { '$ifNull': [ "$census_static_category_id", None ] },
                                                    'section_id': { '$ifNull': [ "$id", None ] },
                                                    'question_id': { '$ifNull': [ "$$qus.id", None ] },
                                                    'part': { '$ifNull': [ "$$part", None ] },
                                                    'qno': { '$ifNull': [ "$$qus.qno", None ] },
                                                    'title': { '$ifNull': [ "$$qus.title", None ] },
                                                    'is_required': { '$ifNull': [ "$$qus.is_required", None ] },
                                                    'answers': { '$ifNull': [ "$$qus.answers", None ] },
                                                    'position': { '$ifNull': [ "$$qus.position", None ] },
                                                    'is_read_only': { '$ifNull': [ "$$qus.is_read_only", None ] },
                                                    'is_approved': { '$ifNull': [ "$$qus.is_approved", None ] },
                                                    'is_rejected': { '$ifNull': [ "$$qus.is_rejected", None ] },
                                                    'is_reviewed_by_barangay': { '$ifNull': [ "$$qus.is_reviewed_by_barangay", None ] },
                                                    'reject_reason': { '$ifNull': [ "$$qus.reject_reason", None ] },
                                                    'approved_date': { '$ifNull': [ "$$qus.approved_date", None ] },
                                                    'rejected_date': { '$ifNull': [ "$$qus.rejected_date", None ] },
                                                    'others_status': { '$ifNull': [ "$$qus.others_status", None ] },
                                                    'is_qn_enable': { '$ifNull': [ "$$qus.is_qn_enable", None ] },                                                    
                                                    'created_at': { '$ifNull': [ "$$qus.created_at", None ] },
                                                    'updated_at': { '$ifNull': [ "$$qus.updated_at", None ] },
                                                    'is_deleted': { '$ifNull': [ "$$qus.is_deleted", None ] },
                                                }
                                            }
                                        }
                                    }
                                },
                                {
                                    '$sort':{'position':1}
                                }
                            ],
                            'as': "section"
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                            'category_name': { '$ifNull': [ "$category_name", None ] },
                            'position': { '$ifNull': [ "$position", None ] },
                            'page': { '$ifNull': [ "$page", None ] },
                            'part': { '$ifNull': [ "$part", None ] },
                            'section': { '$ifNull': [ "$section", None ] },
                        }
                    },
                    {
                        '$sort':{'position':1}
                    }
                ],
                'as':'final_section'
            }
        },
        {
            '$project':{
                '_id' : 0,
                'id': { '$ifNull': [ "$id", None ] },
                'survey_number': { '$ifNull': [ "$survey_number", None ] },
                'data_collector_id': { '$ifNull': [ "$data_collector_id", None ] },
                'data_reviewer_id': { '$ifNull': [ "$data_reviewer_id", None ] },
                'survey_type': { '$ifNull': [ "$survey_type", None ] },
                'status': { '$ifNull': [ "$status", None ] },
                'household_member_count': { '$ifNull': [ "$household_member_count", None ] },
                'data_collector_signature': { '$ifNull': [ "$data_collector_signature", None ] },
                'signature': { '$ifNull': [ "$signature", None ] },
                'signature_recorrection_flag': { '$ifNull': [ "$signature_recorrection_flag", None ] },
                'mobile_next_section': { '$ifNull': [ "$mobile_next_section", None ] },
                'next_section': { '$ifNull': [ "$next_section", None ] },
                'inner_next_section': { '$ifNull': [ "$inner_next_section", None ] },
                'is_recorrection_members': { '$ifNull': [ "$is_recorrection_members", False ] },
                'data_reviewer_signature': { '$ifNull': [ "$data_reviewer_signature", None ] },
                'notes': { '$ifNull': [ "$notes", None ] },
                'members': { '$ifNull': [ "$members", None ] },
                'initial_section':{ '$ifNull': [ "$initial_section", None ] },
                'interview_section':{ '$ifNull': [ "$interview_section", None ] },
                'house_hold_member_section':{ '$ifNull': [ "$house_hold_member_section", None ] },
                'final_section':{ '$ifNull': [ "$final_section", None ] },
            }
        }
    ])
    return list(survey_entry_details)
   
def mdb_pending_survey_entry(param):
    pending_survey_details = {}
    pending_survey_details = SurveyEntry.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$lookup':
            {
                'from': "rbim_users",
                'let': { 'data_reviewer_id': "$data_reviewer_id"},
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': [ "$id",  "$$data_reviewer_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'first_name': { '$ifNull': [ "$first_name", None ] },
                            'email':{ '$ifNull': [ "$email", None ] },
                            'fcm_token':{ '$ifNull': [ "$fcm_token", None ] }
                        }
                    }
                ],
                'as': "data_reviewer"
             }
        },
        {
            '$unwind':{
                'path' : '$data_reviewer',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$lookup':
            {
                'from': "rbim_users",
                'let': { 'barangay_id': "$barangay_id"},
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': [ "$id",  "$$barangay_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'first_name': { '$ifNull': [ "$first_name", None ] },
                            'email':{ '$ifNull': [ "$email", None ] },
                            'fcm_token':{ '$ifNull': [ "$fcm_token", None ] }
                        }
                    }
                ],
                'as': "barangay"
             }
        },
        {
            '$unwind':{
                'path' : '$barangay',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$group':{
                '_id':{
                    "status": "$status",
                    "data_reviewer": "$data_reviewer",
                    "barangay": "$barangay"
                },
                'pending_survey_number':{
                    "$push": "$survey_number"
                }
            }
        },
        {
            '$addFields':{
                'user_info': {
                    '$cond': { 'if': { '$eq': [ "$_id.status", "pending_for_approval" ] }, 'then': "$_id.barangay", 'else': "$_id.data_reviewer" }
                }
            }
        },
        {
            '$project':{
                '_id' : 0,
                'status': { '$ifNull': [ "$_id.status", None ] },
                'first_name': { '$ifNull': [ "$user_info.first_name", None ] },
                'sender': { '$ifNull': [ "$user_info.id", None ] },
                'receiver': { '$ifNull': [ "$user_info.id", None ] },
                'email': { '$ifNull': [ "$user_info.email", None ] },
                'fcm_token': { '$ifNull': [ "$user_info.fcm_token", None ] },
                'pending_survey_number': {
                    '$reduce': {
                        'input': '$pending_survey_number',
                        'initialValue': '',
                        'in': {
                            '$concat': [
                                '$$value',
                                {'$cond': [{'$eq': ['$$value', '']}, '', ', ']}, 
                                '$$this']
                        }
                    }
                }
            }
        },
        {
            '$sort':{'status':1}
        }
    ])
    return list(pending_survey_details)

def mdb_survey_entry_year_reports(param):
    survey_year_reports = {}
    survey_year_reports = SurveyEntry.mongoObjects.mongo_aggregate([
        {
            '$addFields':{
                'created_year':{'$year':'$created_at' },
                'created_month':{'$month':'$created_at' }
            }
        },
        {
            '$match': param['match']
        },
        {
            '$group':{
                '_id':'$created_month',
                'count': { '$sum': 1 }
            }
        },
        {
            '$group': {
            '_id': "",
            'monthsAndCount': { '$push': { 'month': "$_id", 'count': "$count" } }
            }
        },
        {
            '$project': {
                '_id': 0,
                'monthsAndCount': {
                    '$reduce': {
                        'input': {
                            '$setDifference': [ constants.MONTH_NUMBER_LIST,
                            "$monthsAndCount.month" 
                            ]
                        },
                        'initialValue': "$monthsAndCount",
                        'in': {
                            '$concatArrays': [
                            [
                                {
                                'month': "$$this",
                                'count': 0
                                }
                            ],
                            "$$value"
                            ]
                        }
                    }
                }
            }
        },
        {
            '$unwind': "$monthsAndCount"
        },
        {
            '$sort': {"monthsAndCount.month": 1}
        },
        {
            '$group': {
                '_id': "",
                'survey_count': {
                    '$push': "$monthsAndCount.count"
                }
            }
        },
        {
            '$project': {
                "_id":0,
                "label": constants.MONTH_NAME_LIST,
                "survey_count": { '$ifNull': [ "$survey_count", None ] }
            }
        }
    ])
    return list(survey_year_reports)

def survey_entry_elastic_search(param):
    survey_entry_details = {}
    print(param)
    survey_entry_details = SurveyEntry.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$addFields':{
                'survey_entry_id': { '$ifNull': [ "$id", None ] },
            }
        },
        {
            '$lookup':
            {
                'from': "rbim_censusstaticcategory",
                'let': {
                    'survey_entry_id': "$survey_entry_id"
                },
                'pipeline': [
                    {
                        '$match': {
                            '$expr': {
                                '$and': [
                                    {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                    {'$eq': ["$part",  "initial_section" ] },
                                ]
                            }
                        }
                    },
                    {
                        '$addFields':{
                            'census_static_category_id': { '$ifNull': [ "$id", None ] },
                        }
                    },
                    {
                        '$lookup':
                        {
                            'from': "rbim_censusstaticsections",
                            'let': {
                                'survey_entry_id': "$survey_entry_id",
                                'census_static_category_id': "$census_static_category_id",
                                'part': "$part",
                            },
                            'pipeline': [
                                {
                                    '$match': {
                                        '$expr': {
                                            '$and': [
                                                {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                                {'$eq': ["$census_static_category_id",  "$$census_static_category_id" ] }
                                            ]
                                        }
                                    }
                                },
                                {
                                    '$project':{
                                        '_id' : 0,
                                        'id': { '$ifNull': [ "$id", None ] },
                                        'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                        'census_static_category_id': { '$ifNull': [ "$census_static_category_id", None ] },
                                        'section_name': { '$ifNull': [ "$section_name", None ] },
                                        'is_enable': { '$ifNull': [ "$is_enable", None ] },
                                        'is_subheader': { '$ifNull': [ "$is_subheader", None ] },
                                        'is_recorrection': { '$ifNull': [ "$is_recorrection", None ] },
                                        'position': { '$ifNull': [ "$position", None ] },
                                        'qcount': { '$ifNull': [ "$qcount", None ] },
                                        'anscount': { '$ifNull': [ "$anscount", None ] },
                                        'questions': {
                                            "$map": {
                                            "input": "$questions",
                                            "as": "qus",
                                                "in": {
                                                    'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                                    'category_id': { '$ifNull': [ "$census_static_category_id", None ] },
                                                    'section_id': { '$ifNull': [ "$id", None ] },
                                                    'question_id': { '$ifNull': [ "$$qus.id", None ] },
                                                    'part': { '$ifNull': [ "$$part", None ] },
                                                    'qno': { '$ifNull': [ "$$qus.qno", None ] },
                                                    'title': { '$ifNull': [ "$$qus.title", None ] },
                                                    'is_required': { '$ifNull': [ "$$qus.is_required", None ] },
                                                    'answers': { '$ifNull': [ "$$qus.answers", None ] },
                                                    'position': { '$ifNull': [ "$$qus.position", None ] },
                                                    'is_read_only': { '$ifNull': [ "$$qus.is_read_only", None ] },
                                                    'is_approved': { '$ifNull': [ "$$qus.is_approved", None ] },
                                                    'is_rejected': { '$ifNull': [ "$$qus.is_rejected", None ] },
                                                    'is_reviewed_by_barangay': { '$ifNull': [ "$$qus.is_reviewed_by_barangay", None ] },
                                                    'reject_reason': { '$ifNull': [ "$$qus.reject_reason", None ] },
                                                    'approved_date': { '$ifNull': [ "$$qus.approved_date", None ] },
                                                    'rejected_date': { '$ifNull': [ "$$qus.rejected_date", None ] },
                                                    'others_status': { '$ifNull': [ "$$qus.others_status", None ] },
                                                    'is_qn_enable': { '$ifNull': [ "$$qus.is_qn_enable", None ] },                                                   
                                                    'created_at': { '$ifNull': [ "$$qus.created_at", None ] },
                                                    'updated_at': { '$ifNull': [ "$$qus.updated_at", None ] },
                                                    'is_deleted': { '$ifNull': [ "$$qus.is_deleted", None ] },
                                                }
                                            }
                                        }
                                    }
                                },
                                {
                                    '$sort':{'position':1}
                                }
                            ],
                            'as': "section"
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                            'category_name': { '$ifNull': [ "$category_name", None ] },
                            'position': { '$ifNull': [ "$position", None ] },
                            'page': { '$ifNull': [ "$page", None ] },
                            'part': { '$ifNull': [ "$part", None ] },
                            'section': { '$ifNull': [ "$section", None ] },
                        }
                    },
                    {
                        '$sort':{'position':1}
                    }
                ],
                'as':'initial_section'
            }
        },
        {
            '$unwind':{
                'path' : '$initial_section',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$lookup':
            {
                'from': "rbim_censusstaticcategory",
                'let': {
                    'survey_entry_id': "$survey_entry_id"
                },
                'pipeline': [
                    {
                        '$match': {
                            '$expr': {
                                '$and': [
                                    {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                    {'$eq': ["$part",  "interview_section" ] },
                                ]
                            }
                        }
                    },
                    {
                        '$addFields':{
                            'census_static_category_id': { '$ifNull': [ "$id", None ] },
                        }
                    },
                    {
                        '$lookup':
                        {
                            'from': "rbim_censusstaticsections",
                            'let': {
                                'survey_entry_id': "$survey_entry_id",
                                'census_static_category_id': "$census_static_category_id",
                                'part': "$part",
                            },
                            'pipeline': [
                                {
                                    '$match': {
                                        '$expr': {
                                            '$and': [
                                                {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                                {'$eq': ["$census_static_category_id",  "$$census_static_category_id" ] }
                                            ]
                                        }
                                    }
                                },
                                {
                                    '$project':{
                                        '_id' : 0,
                                        'id': { '$ifNull': [ "$id", None ] },
                                        'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                        'census_static_category_id': { '$ifNull': [ "$census_static_category_id", None ] },
                                        'section_name': { '$ifNull': [ "$section_name", None ] },
                                        'is_enable': { '$ifNull': [ "$is_enable", None ] },
                                        'is_subheader': { '$ifNull': [ "$is_subheader", None ] },
                                        'is_recorrection': { '$ifNull': [ "$is_recorrection", None ] },
                                        'position': { '$ifNull': [ "$position", None ] },
                                        'qcount': { '$ifNull': [ "$qcount", None ] },
                                        'anscount': { '$ifNull': [ "$anscount", None ] },
                                        'questions': {
                                            "$map": {
                                            "input": "$questions",
                                            "as": "qus",
                                                "in": {
                                                    'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                                    'category_id': { '$ifNull': [ "$census_static_category_id", None ] },
                                                    'section_id': { '$ifNull': [ "$id", None ] },
                                                    'question_id': { '$ifNull': [ "$$qus.id", None ] },
                                                    'part': { '$ifNull': [ "$$part", None ] },
                                                    'qno': { '$ifNull': [ "$$qus.qno", None ] },
                                                    'title': { '$ifNull': [ "$$qus.title", None ] },
                                                    'is_required': { '$ifNull': [ "$$qus.is_required", None ] },
                                                    'answers': { '$ifNull': [ "$$qus.answers", None ] },
                                                    'position': { '$ifNull': [ "$$qus.position", None ] },
                                                    'is_read_only': { '$ifNull': [ "$$qus.is_read_only", None ] },
                                                    'is_approved': { '$ifNull': [ "$$qus.is_approved", None ] },
                                                    'is_rejected': { '$ifNull': [ "$$qus.is_rejected", None ] },
                                                    'is_reviewed_by_barangay': { '$ifNull': [ "$$qus.is_reviewed_by_barangay", None ] },
                                                    'reject_reason': { '$ifNull': [ "$$qus.reject_reason", None ] },
                                                    'approved_date': { '$ifNull': [ "$$qus.approved_date", None ] },
                                                    'rejected_date': { '$ifNull': [ "$$qus.rejected_date", None ] },
                                                    'others_status': { '$ifNull': [ "$$qus.others_status", None ] },
                                                    'is_qn_enable': { '$ifNull': [ "$$qus.is_qn_enable", None ] },                                                   
                                                    'created_at': { '$ifNull': [ "$$qus.created_at", None ] },
                                                    'updated_at': { '$ifNull': [ "$$qus.updated_at", None ] },
                                                    'is_deleted': { '$ifNull': [ "$$qus.is_deleted", None ] },
                                                }
                                            }
                                        }
                                    }
                                },
                                {
                                    '$sort':{'position':1}
                                }
                            ],
                            'as': "section"
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                            'category_name': { '$ifNull': [ "$category_name", None ] },
                            'position': { '$ifNull': [ "$position", None ] },
                            'page': { '$ifNull': [ "$page", None ] },
                            'part': { '$ifNull': [ "$part", None ] },
                            'section': { '$ifNull': [ "$section", None ] },
                        }
                    },
                    {
                        '$sort':{'position':1}
                    }
                ],
                'as':'interview_section'
            }
        },
        {
            '$lookup':{
               'from': "rbim_censusmember",
                'let': {
                    'survey_entry_id': "$survey_entry_id"
                },
                'pipeline': [
                    {
                        '$match': {
                            '$expr': {
                                '$and': [
                                    {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$addFields':{
                            'census_member_id': { '$ifNull': [ "$id", None ] },
                        }
                    },
                    {
                        '$lookup':
                        {
                            'from': "rbim_censuscategory",
                            'let': {
                                'survey_entry_id': "$survey_entry_id",
                                'census_member_id': "$census_member_id",
                            },
                            'pipeline': [
                                {
                                    '$match': {
                                        '$expr': {
                                            '$and': [
                                                {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                                {'$eq': ["$census_member_id",  "$$census_member_id" ] }
                                            ]
                                        }
                                    }
                                },
                                {
                                    '$lookup':
                                    {
                                        'from': "rbim_censussections",
                                        'let': {
                                            'survey_entry_id': "$survey_entry_id",
                                            'census_category_id': "$id",
                                            'part': "$part",
                                        },
                                        'pipeline': [
                                            {
                                                '$match': {
                                                    '$expr': {
                                                        '$and': [
                                                            {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                                            {'$eq': ["$census_category_id",  "$$census_category_id" ] }
                                                        ]
                                                    }
                                                }
                                            },
                                            {
                                                '$project':{
                                                    '_id' : 0,
                                                    'id': { '$ifNull': [ "$id", None ] },
                                                    'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                                    'census_category_id': { '$ifNull': [ "$census_category_id", None ] },
                                                    'section_name': { '$ifNull': [ "$section_name", None ] },
                                                    'is_enable': { '$ifNull': [ "$is_enable", None ] },
                                                    'is_subheader': { '$ifNull': [ "$is_subheader", None ] },
                                                    'is_recorrection': { '$ifNull': [ "$is_recorrection", None ] },
                                                    'position': { '$ifNull': [ "$position", None ] },
                                                    'qcount': { '$ifNull': [ "$qcount", None ] },
                                                    'anscount': { '$ifNull': [ "$anscount", None ] },
                                                    'questions': {
                                                        "$map": {
                                                        "input": "$questions",
                                                        "as": "qus",
                                                            "in": {
                                                                'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                                                'category_id': { '$ifNull': [ "$census_category_id", None ] },
                                                                'section_id': { '$ifNull': [ "$id", None ] },
                                                                'question_id': { '$ifNull': [ "$$qus.id", None ] },
                                                                'part': { '$ifNull': [ "$$part", None ] },
                                                                'qno': { '$ifNull': [ "$$qus.qno", None ] },
                                                                'title': { '$ifNull': [ "$$qus.title", None ] },
                                                                'is_required': { '$ifNull': [ "$$qus.is_required", None ] },
                                                                'answers': { '$ifNull': [ "$$qus.answers", None ] },
                                                                'position': { '$ifNull': [ "$$qus.position", None ] },
                                                                'is_read_only': { '$ifNull': [ "$$qus.is_read_only", None ] },
                                                                'is_approved': { '$ifNull': [ "$$qus.is_approved", None ] },
                                                                'is_rejected': { '$ifNull': [ "$$qus.is_rejected", None ] },
                                                                'is_reviewed_by_barangay': { '$ifNull': [ "$$qus.is_reviewed_by_barangay", None ] },
                                                                'reject_reason': { '$ifNull': [ "$$qus.reject_reason", None ] },
                                                                'approved_date': { '$ifNull': [ "$$qus.approved_date", None ] },
                                                                'rejected_date': { '$ifNull': [ "$$qus.rejected_date", None ] },
                                                                'others_status': { '$ifNull': [ "$$qus.others_status", None ] },
                                                                'is_qn_enable': { '$ifNull': [ "$$qus.is_qn_enable", None ] },                                                              
                                                                'created_at': { '$ifNull': [ "$$qus.created_at", None ] },
                                                                'updated_at': { '$ifNull': [ "$$qus.updated_at", None ] },
                                                                'is_deleted': { '$ifNull': [ "$$qus.is_deleted", None ] },
                                                            }
                                                        }
                                                    }
                                                }
                                            },
                                            {
                                                '$sort':{'position':1}
                                            }
                                        ],
                                        'as': "section"
                                    }
                                },
                                {
                                    '$sort':{'position':1}
                                },
                                {
                                    '$group':{
                                        '_id':'$page',
                                        'page':{
                                            "$push":{
                                                'id': { '$ifNull': [ "$id", None ] },
                                                'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                                'census_member_id': { '$ifNull': [ "$census_member_id", None ] },
                                                'category_name': { '$ifNull': [ "$category_name", None ] },
                                                'position': { '$ifNull': [ "$position", None ] },
                                                'page': { '$ifNull': [ "$page", None ] },
                                                'part': { '$ifNull': [ "$part", None ] },
                                                'section': { '$ifNull': [ "$section", None ] }
                                            }
                                        }
                                    }
                                },
                                {
                                    '$sort':{'_id':1}
                                }
                            ],
                            'as': "category"
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                            'member_id': { '$ifNull': [ "$member_id", None ] },
                            'member_name': { '$ifNull': [ "$member_name", None ] },
                            'category': { '$ifNull': [ "$category", None ] },
                        }
                    }
                ],
                'as':'house_hold_member_section'
            }
        },
        {
            '$lookup':
            {
                'from': "rbim_censusstaticcategory",
                'let': {
                    'survey_entry_id': "$survey_entry_id"
                },
                'pipeline': [
                    {
                        '$match': {
                            '$expr': {
                                '$and': [
                                    {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                    {'$eq': ["$part",  "final_section" ] },
                                ]
                            }
                        }
                    },
                    {
                        '$addFields':{
                            'census_static_category_id': { '$ifNull': [ "$id", None ] },
                        }
                    },
                    {
                        '$lookup':
                        {
                            'from': "rbim_censusstaticsections",
                            'let': {
                                'survey_entry_id': "$survey_entry_id",
                                'census_static_category_id': "$census_static_category_id",
                                'part': "$part",
                            },
                            'pipeline': [
                                {
                                    '$match': {
                                        '$expr': {
                                            '$and': [
                                                {'$eq': ["$survey_entry_id",  "$$survey_entry_id" ] },
                                                {'$eq': ["$census_static_category_id",  "$$census_static_category_id" ] }
                                            ]
                                        }
                                    }
                                },
                                {
                                    '$project':{
                                        '_id' : 0,
                                        'id': { '$ifNull': [ "$id", None ] },
                                        'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                        'census_static_category_id': { '$ifNull': [ "$census_static_category_id", None ] },
                                        'section_name': { '$ifNull': [ "$section_name", None ] },
                                        'is_enable': { '$ifNull': [ "$is_enable", None ] },
                                        'is_subheader': { '$ifNull': [ "$is_subheader", None ] },
                                        'is_recorrection': { '$ifNull': [ "$is_recorrection", None ] },
                                        'position': { '$ifNull': [ "$position", None ] },
                                        'qcount': { '$ifNull': [ "$qcount", None ] },
                                        'anscount': { '$ifNull': [ "$anscount", None ] },
                                        'questions': {
                                            "$map": {
                                            "input": "$questions",
                                            "as": "qus",
                                                "in": {
                                                    'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                                                    'category_id': { '$ifNull': [ "$census_static_category_id", None ] },
                                                    'section_id': { '$ifNull': [ "$id", None ] },
                                                    'question_id': { '$ifNull': [ "$$qus.id", None ] },
                                                    'part': { '$ifNull': [ "$$part", None ] },
                                                    'qno': { '$ifNull': [ "$$qus.qno", None ] },
                                                    'title': { '$ifNull': [ "$$qus.title", None ] },
                                                    'is_required': { '$ifNull': [ "$$qus.is_required", None ] },
                                                    'answers': { '$ifNull': [ "$$qus.answers", None ] },
                                                    'position': { '$ifNull': [ "$$qus.position", None ] },
                                                    'is_read_only': { '$ifNull': [ "$$qus.is_read_only", None ] },
                                                    'is_approved': { '$ifNull': [ "$$qus.is_approved", None ] },
                                                    'is_rejected': { '$ifNull': [ "$$qus.is_rejected", None ] },
                                                    'is_reviewed_by_barangay': { '$ifNull': [ "$$qus.is_reviewed_by_barangay", None ] },
                                                    'reject_reason': { '$ifNull': [ "$$qus.reject_reason", None ] },
                                                    'approved_date': { '$ifNull': [ "$$qus.approved_date", None ] },
                                                    'rejected_date': { '$ifNull': [ "$$qus.rejected_date", None ] },
                                                    'others_status': { '$ifNull': [ "$$qus.others_status", None ] },
                                                    'is_qn_enable': { '$ifNull': [ "$$qus.is_qn_enable", None ] },                                                  
                                                    'created_at': { '$ifNull': [ "$$qus.created_at", None ] },
                                                    'updated_at': { '$ifNull': [ "$$qus.updated_at", None ] },
                                                    'is_deleted': { '$ifNull': [ "$$qus.is_deleted", None ] },
                                                }
                                            }
                                        }
                                    }
                                },
                                {
                                    '$sort':{'position':1}
                                }
                            ],
                            'as': "section"
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'survey_entry_id': { '$ifNull': [ "$survey_entry_id", None ] },
                            'category_name': { '$ifNull': [ "$category_name", None ] },
                            'position': { '$ifNull': [ "$position", None ] },
                            'page': { '$ifNull': [ "$page", None ] },
                            'part': { '$ifNull': [ "$part", None ] },
                            'section': { '$ifNull': [ "$section", None ] },
                        }
                    },
                    {
                        '$sort':{'position':1}
                    }
                ],
                'as':'final_section'
            }
        },
        {
            '$lookup':
                {
                    'from': "rbim_profile",
                    'let': {'data_collector_id': "$data_collector_id"},
                    'pipeline': [
                        {
                            '$match': {
                                '$expr': {
                                    '$and': [
                                        {'$eq': ["$user_id", "$$data_collector_id"]}
                                    ]
                                }
                            }
                        },
                        {
                            '$project': {
                                '_id': 0,
                                'id': {'$ifNull': ["$id", None]},
                                'official_number': {'$ifNull': ["$official_number", None]}
                            }
                        }
                    ],
                    'as': "data_collector"
                }
        },
        {
            '$unwind': {
                'path': '$data_collector',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$lookup':
                {
                    'from': "rbim_profile",
                    'let': {'data_reviewer_id': "$data_reviewer_id"},
                    'pipeline': [
                        {
                            '$match': {
                                '$expr': {
                                    '$and': [
                                        {'$eq': ["$user_id", "$$data_reviewer_id"]}
                                    ]
                                }
                            }
                        },
                        {
                            '$project': {
                                '_id': 0,
                                'id': {'$ifNull': ["$id", None]},
                                'official_number': {'$ifNull': ["$official_number", None]}
                            }
                        }
                    ],
                    'as': "data_reviewer"
                }
        },
        {
            '$unwind': {
                'path': '$data_reviewer',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$lookup':
                {
                    'from': "rbim_users",
                    'let': {'data_reviewer_id': "$data_reviewer_id"},
                    'pipeline': [
                        {
                            '$match': {
                                '$expr': {
                                    '$and': [
                                        {'$eq': ["$id", "$$data_reviewer_id"]}
                                    ]
                                }
                            }
                        },
                        {
                            '$project': {
                                '_id': 0,
                                'id': {'$ifNull': ["$id", None]},
                                'first_name': {'$ifNull': ["$first_name", None]}
                            }
                        }
                    ],
                    'as': "data_reviewer_name"
                }
        },
        {
            '$unwind': {
                'path': '$data_reviewer_name',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$lookup':
                {
                    'from': "rbim_users",
                    'let': {'data_collector_id': "$data_collector_id"},
                    'pipeline': [
                        {
                            '$match': {
                                '$expr': {
                                    '$and': [
                                        {'$eq': ["$id", "$$data_collector_id"]}
                                    ]
                                }
                            }
                        },
                        {
                            '$project': {
                                '_id': 0,
                                'id': {'$ifNull': ["$id", None]},
                                'first_name': {'$ifNull': ["$first_name", None]}
                            }
                        }
                    ],
                    'as': "data_collector_name"
                }
        },
        {
            '$unwind': {
                'path': '$data_collector_name',
                'preserveNullAndEmptyArrays': True
            }
        },
        {'$addFields': {'survey_date': {
            '$switch': {
                'branches': [
                    {'case': {'$eq': ['$status', param['survey_status']]}, 'then': param['survey_status_date_param']},
                ],
                'default': None
            }}
        }},

        {
            '$project':{
                '_id' : 0,
                'id': { '$ifNull': [ "$id", None ] },
                'survey_number': { '$ifNull': [ "$survey_number", None ] },
                'survey_date':  {'$dateToString': {'date': '$survey_date',
                                                    'format': '%d/%m/%Y'}},
                'survey_assigned_on': { '$ifNull': [ "$survey_assigned_on", None ] },
                'data_collector_id': { '$ifNull': [ "$data_collector_id", None ] },
                'data_reviewer_id': { '$ifNull': [ "$data_reviewer_id", None ] },
                'data_reviewer': { '$ifNull': [ "$data_reviewer", None ] },
                'data_collector': { '$ifNull': [ "$data_collector", None ] },
                'data_reviewer_name': { '$ifNull': [ "$data_reviewer_name", None ] },
                'data_collector_name': { '$ifNull': [ "$data_collector_name", None ] },
                'survey_type': { '$ifNull': [ "$survey_type", None ] },
                'status': { '$ifNull': [ "$status", None ] },
                'household_member_count': { '$ifNull': [ "$household_member_count", None ] },
                'data_collector_signature': { '$ifNull': [ "$data_collector_signature", None ] },
                'signature': { '$ifNull': [ "$signature", None ] },
                'signature_recorrection_flag': { '$ifNull': [ "$signature_recorrection_flag", None ] },
                'mobile_next_section': { '$ifNull': [ "$mobile_next_section", None ] },
                'next_section': { '$ifNull': [ "$next_section", None ] },
                'inner_next_section': { '$ifNull': [ "$inner_next_section", None ] },
                'is_recorrection_members': { '$ifNull': [ "$is_recorrection_members", False ] },
                'data_reviewer_signature': { '$ifNull': [ "$data_reviewer_signature", None ] },
                'notes': { '$ifNull': [ "$notes", None ] },
                'members': { '$ifNull': [ "$members", None ] },
                'initial_section':{ '$ifNull': [ "$initial_section", None ] },
                'interview_section':{ '$ifNull': [ "$interview_section", None ] },
                'house_hold_member_section':{ '$ifNull': [ "$house_hold_member_section", None ] },
                'final_section':{ '$ifNull': [ "$final_section", None ] },
            }
        },


        {'$match': { '$or': [
            {'survey_number':  param['text_search']},
            {'survey_type':  param['text_search']},
            {'data_reviewer.official_number':  param['text_search']},
            {'data_collector.official_number':  param['text_search']},
            {'data_reviewer_name.first_name':  param['text_search']},
            {'data_collector_name.first_name':  param['text_search']},
            {'survey_date':  param['text_search']},
            {'members.member_name':  {'$regex': param['text_search'], '$options':'i'}},
            {'initial_section.section.questions':  {'$elemMatch': { 'title': {'$regex' : param['text_search'], '$options': 'i'}}}},
            {'initial_section.section.questions.answers':  {'$elemMatch': { 'answer_value': {'$regex' : param['text_search'], '$options': 'i'}}}},
            {'interview_section.section.questions':  {'$elemMatch': { 'title': {'$regex' : param['text_search'], '$options': 'i'}}}},
            {'interview_section.section.questions.answers':  {'$elemMatch': { 'answer_value': {'$regex' : param['text_search'], '$options': 'i'}}}},
            {'house_hold_member_section.category.page.section.questions':  {'$elemMatch': { 'title': {'$regex' : param['text_search'], '$options': 'i'}}}},
            {'house_hold_member_section.category.page.section.questions.answers':  {'$elemMatch': { 'answer_value': {'$regex' : param['text_search'], '$options': 'i'}}}},
            {'final_section.section.questions':  {'$elemMatch': { 'title': {'$regex' : param['text_search'], '$options': 'i'}}}},
            {'final_section.section.questions.answers':  {'$elemMatch': { 'answer_value': {'$regex' : param['text_search'], '$options': 'i'}}}},

        ]}
        },
        {
            '$project': {
                '_id': 0,
                'id': {'$ifNull': ["$id", None]},

            }
        },
        {'$group': {'_id': 0, 'id': {'$push': '$id'}}}

    ])
    return list(survey_entry_details)