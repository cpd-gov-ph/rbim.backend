from rbim.models import SurveyEntry
def mdb_suvery_completed_reports(param):
    suvery_completed_reports = SurveyEntry.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$addFields': {
                'survey_entry_id': {'$ifNull': ["$id", None]},
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
                                        {'$eq': ["$survey_entry_id", "$$survey_entry_id"]},
                                        {'$eq': ["$part", "initial_section"]},
                                    ]
                                }
                            }
                        },
                        {
                            '$addFields': {
                                'census_static_category_id': {'$ifNull': ["$id", None]},
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
                                                        {'$eq': ["$survey_entry_id", "$$survey_entry_id"]},
                                                        {'$eq': ["$census_static_category_id",
                                                                 "$$census_static_category_id"]}
                                                    ]
                                                }
                                            }
                                        },
                                        {
                                            '$unwind': {
                                                'path': '$questions',
                                                'preserveNullAndEmptyArrays': True
                                            }
                                        },
                                        {
                                            '$project': {
                                                '_id': 0,
                                                'id': {'$ifNull': ["$id", None]},
                                                'qno': {'$ifNull': ["$questions.qno", None]},
                                                'position': {'$ifNull': ["$questions.position", None]},
                                                'answers': {
                                                    "$map": {
                                                        "input": "$questions.answers",
                                                        "as": "ans",
                                                        "in": {
                                                            'id': {'$ifNull': ["$$ans.id", None]},
                                                            'dtype': {'$ifNull': ["$$ans.dtype", None]},
                                                            'answer_value': {
                                                                '$cond': {
                                                                    'if': { '$and': [{ '$isArray': "$$ans.answer_value"}]},
                                                                    'then': {
                                                                        '$reduce': {
                                                                            'input': '$$ans.answer_value',
                                                                            'initialValue': '',
                                                                            'in': {
                                                                                '$concat': [
                                                                                    '$$value',
                                                                                    {'$cond': [{'$eq': ['$$value', '']},
                                                                                               '', ', ']},
                                                                                    '$$this']
                                                                            }
                                                                        }
                                                                    },
                                                                    'else': "$$ans.answer_value"
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            '$sort': {'position': 1}
                                        }
                                    ],
                                    'as': "section"
                                }
                        },
                        {
                            '$unwind': {
                                'path': '$section',
                                'preserveNullAndEmptyArrays': True
                            }
                        },
                        {
                            '$sort': {'position': 1}
                        },
                        {
                            '$project': {
                                '_id': 0,
                                'id': {'$ifNull': ["$section.id", None]},
                                'qno': {'$ifNull': ["$section.qno", None]},
                                'answers': {'$ifNull': ["$section.answers", None]},
                            }
                        }
                    ],
                    'as': 'initial_section'
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
                                        {'$eq': ["$survey_entry_id", "$$survey_entry_id"]},
                                        {'$eq': ["$part", "interview_section"]},
                                    ]
                                }
                            }
                        },
                        {
                            '$addFields': {
                                'census_static_category_id': {'$ifNull': ["$id", None]},
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
                                                        {'$eq': ["$survey_entry_id", "$$survey_entry_id"]},
                                                        {'$eq': ["$census_static_category_id",
                                                                 "$$census_static_category_id"]}
                                                    ]
                                                }
                                            }
                                        },
                                        {
                                            '$unwind': {
                                                'path': '$questions',
                                                'preserveNullAndEmptyArrays': True
                                            }
                                        },
                                        {
                                            '$project': {
                                                '_id': 0,
                                                'id': {'$ifNull': ["$id", None]},
                                                'qno': {'$ifNull': ["$questions.qno", None]},
                                                'position': {'$ifNull': ["$questions.position", None]},
                                                'answers': {
                                                    "$map": {
                                                        "input": "$questions.answers",
                                                        "as": "ans",
                                                        "in": {
                                                            'id': {'$ifNull': ["$$ans.id", None]},
                                                            'dtype': {'$ifNull': ["$$ans.dtype", None]},
                                                            'answer_value': {
                                                                '$cond': {
                                                                    'if': { '$and': [{ '$isArray': "$$ans.answer_value"}]},
                                                                    'then': {
                                                                        '$reduce': {
                                                                            'input': '$$ans.answer_value',
                                                                            'initialValue': '',
                                                                            'in': {
                                                                                '$concat': [
                                                                                    '$$value',
                                                                                    {'$cond': [{'$eq': ['$$value', '']},
                                                                                               '', ', ']},
                                                                                    '$$this']
                                                                            }
                                                                        }
                                                                    },
                                                                    'else': "$$ans.answer_value"
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            '$sort': {'position': 1}
                                        }
                                    ],
                                    'as': "section"
                                }
                        },
                        {
                            '$unwind': {
                                'path': '$section',
                                'preserveNullAndEmptyArrays': True
                            }
                        },
                        {
                            '$sort': {'position': 1}
                        },
                        {
                            '$project': {
                                '_id': 0,
                                'id': {'$ifNull': ["$section.id", None]},
                                'qno': {'$ifNull': ["$section.qno", None]},
                                'answers': {'$ifNull': ["$section.answers", None]},
                            }
                        }
                    ],
                    'as': 'interview_section'
                }
        },
        {
            '$lookup': {
                'from': "rbim_censusmember",
                'let': {
                    'survey_entry_id': "$survey_entry_id"
                },
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
                        '$addFields': {
                            'census_member_id': {'$ifNull': ["$id", None]},
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
                                                    {'$eq': ["$survey_entry_id", "$$survey_entry_id"]},
                                                    {'$eq': ["$census_member_id", "$$census_member_id"]}
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
                                                                    {'$eq': ["$survey_entry_id", "$$survey_entry_id"]},
                                                                    {'$eq': ["$census_category_id",
                                                                             "$$census_category_id"]}
                                                                ]
                                                            }
                                                        }
                                                    },
                                                    {
                                                        '$unwind': {
                                                            'path': '$questions',
                                                            'preserveNullAndEmptyArrays': True
                                                        }
                                                    },
                                                    {
                                                        '$project': {
                                                            '_id': 0,
                                                            'id': {'$ifNull': ["$id", None]},
                                                            'qno': {'$ifNull': ["$questions.qno", None]},
                                                            'position': {'$ifNull': ["$questions.position", None]},
                                                            'answers': {
                                                                "$map": {
                                                                    "input": "$questions.answers",
                                                                    "as": "ans",
                                                                    "in": {
                                                                        'id': {'$ifNull': ["$$ans.id", None]},
                                                                        'dtype': {'$ifNull': ["$$ans.dtype", None]},
                                                                        'answer_value': {
                                                                            '$cond': {
                                                                                'if': { '$and': [{ '$isArray': "$$ans.answer_value"}]},
                                                                                'then': {
                                                                                    '$reduce': {
                                                                                        'input': '$$ans.answer_value',
                                                                                        'initialValue': '',
                                                                                        'in': {
                                                                                            '$concat': [
                                                                                                '$$value',
                                                                                                {'$cond': [{'$eq': ['$$value', '']},
                                                                                                           '', ', ']},
                                                                                                '$$this']
                                                                                        }
                                                                                    }
                                                                                },
                                                                                'else': "$$ans.answer_value"
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    },
                                                    {
                                                        '$sort': {'position': 1}
                                                    }
                                                ],
                                                'as': "section"
                                            }
                                    },
                                    {
                                        '$unwind': {
                                            'path': '$section',
                                            'preserveNullAndEmptyArrays': True
                                        }
                                    },
                                    {
                                        '$sort': {'position': 1}
                                    },
                                    {
                                        '$project': {
                                            '_id': 0,
                                            'id': {'$ifNull': ["$section.id", None]},
                                            'qno': {'$ifNull': ["$section.qno", None]},
                                            'answers': {'$ifNull': ["$section.answers", None]},
                                        }
                                    }
                                ],
                                'as': "category"
                            }
                    },
                    {
                        '$project': {
                            '_id': 0,
                            'id': {'$ifNull': ["$id", None]},
                            'survey_entry_id': {'$ifNull': ["$survey_entry_id", None]},
                            'member_id': {'$ifNull': ["$member_id", None]},
                            'member_name': {'$ifNull': ["$member_name", None]},
                            'category': {'$ifNull': ["$category", None]},
                        }
                    }
                ],
                'as': 'house_hold_member_section'
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
                                        {'$eq': ["$survey_entry_id", "$$survey_entry_id"]},
                                        {'$eq': ["$part", "final_section"]},
                                    ]
                                }
                            }
                        },
                        {
                            '$addFields': {
                                'census_static_category_id': {'$ifNull': ["$id", None]},
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
                                                        {'$eq': ["$survey_entry_id", "$$survey_entry_id"]},
                                                        {'$eq': ["$census_static_category_id",
                                                                 "$$census_static_category_id"]}
                                                    ]
                                                }
                                            }
                                        },
                                        {
                                            '$unwind': {
                                                'path': '$questions',
                                                'preserveNullAndEmptyArrays': True
                                            }
                                        },
                                        {
                                            '$project': {
                                                '_id': 0,
                                                'id': {'$ifNull': ["$id", None]},
                                                'qno': {'$ifNull': ["$questions.qno", None]},
                                                'position': {'$ifNull': ["$questions.position", None]},
                                                'answers': {
                                                    "$map": {
                                                        "input": "$questions.answers",
                                                        "as": "ans",
                                                        "in": {
                                                            'id': {'$ifNull': ["$$ans.id", None]},
                                                            'dtype': {'$ifNull': ["$$ans.dtype", None]},
                                                            'answer_value': {
                                                                '$cond': {
                                                                    'if': { '$and': [{ '$isArray': "$$ans.answer_value"}]},
                                                                    'then': {
                                                                        '$reduce': {
                                                                            'input': '$$ans.answer_value',
                                                                            'initialValue': '',
                                                                            'in': {
                                                                                '$concat': [
                                                                                    '$$value',
                                                                                    {'$cond': [{'$eq': ['$$value', '']},
                                                                                               '', ', ']},
                                                                                    '$$this']
                                                                            }
                                                                        }
                                                                    },
                                                                    'else': "$$ans.answer_value"
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            '$sort': {'position': 1}
                                        }
                                    ],
                                    'as': "section"
                                }
                        },
                        {
                            '$unwind': {
                                'path': '$section',
                                'preserveNullAndEmptyArrays': True
                            }
                        },
                        {
                            '$sort': {'position': 1}
                        },
                        {
                            '$project': {
                                '_id': 0,
                                'id': {'$ifNull': ["$section.id", None]},
                                'qno': {'$ifNull': ["$section.qno", None]},
                                'answers': {'$ifNull': ["$section.answers", None]}
                            }
                        }
                    ],
                    'as': 'final_section'
                }
        },
        {
            '$sort': {'position': 1}
        },
        {
            '$unwind': {
                'path': '$house_hold_member_section',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$addFields': {
                'question_items': {
                    '$cond': {
                        'if': { '$and': [
                            { '$isArray': "$initial_section"},
                            { '$isArray': "$interview_section"},
                            { '$isArray': "$house_hold_member_section.category"},
                            { '$isArray': "$final_section"}
                        ]},
                        'then': { '$concatArrays': ["$initial_section", "$interview_section", "$house_hold_member_section.category", "$final_section"]},
                        'else': []
                    }
                }
            }
        },
        {
            '$addFields': {
                'question_items': {
                    "$map": {
                        "input": "$question_items",
                        "as": "qs",
                        "in": {
                            'qno': {'$ifNull': ["$$qs.qno", None]},
                            'index': {'$ifNull': ["$$qs.id", None]},
                            'answer': {
                                '$reduce': {
                                    'input': {
                                        '$filter': {
                                            'input': "$$qs.answers.answer_value",
                                            'as': "d",
                                            'cond': {
                                                '$ne': ["$$d", False]
                                            }
                                        }
                                    },
                                    'initialValue': "",
                                    'in': {
                                        '$concat': [
                                            "$$value",
                                            {'$cond': [{'$eq': ["$$value", ""]}, "", ", "]},
                                            {'$toString': "$$this"}
                                        ]
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        {
            '$addFields': {
                "members": [
                    {
                        "qno": 'Member Name',
                        "index": '$house_hold_member_section.id',
                        "answer": {'$ifNull': ["$house_hold_member_section.member_name", None]},
                    }
                ]
            }
        },
        {
            '$addFields': {
                'question_items': {
                    '$cond': {
                        'if': {'$and': [
                            {'$isArray': "$members"},
                            {'$isArray': "$question_items"}
                        ]},
                        'then': {'$concatArrays': ["$members", "$question_items"]},
                        'else': []
                    }
                }
            }
        },
        {
            '$project':{
                '_id' : 0,
                'id': { '$ifNull': [ "$id", None ] },
                'survey_number': { '$ifNull': [ "$survey_number", None ] },
                'question_items': {'$ifNull': ["$question_items", None]},
            }
        },
        {
            '$unwind': {
                'path': '$question_items',
                'includeArrayIndex': "arrayIndex",
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$project':{
                '_id' : 0,
                'id': { '$ifNull': [ "$id", None ] },
                'qno': { '$ifNull': [ "$question_items.qno", None ] },
                'answer': {'$ifNull': ["$question_items.answer", None]},
                'arrayIndex': {'$ifNull': ["$arrayIndex", None]},
            }
        },
        {
            '$sort': { 'arrayIndex': -1 }
        },
        { 
            "$group": {
            "_id": "$qno",
            "max": { "$max": "$arrayIndex" },
            "answer": { "$push": "$answer" }
        }},
        {
            '$sort': { 'max': 1 }
        },
        { "$group": {
            "_id": None,
            "data": {
                "$push": { "k": "$_id", "v": "$answer" }
            }
        }},
        { "$replaceRoot": {
            "newRoot": { "$arrayToObject": "$data" }
        }}
    ])
    return list(suvery_completed_reports)