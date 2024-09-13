from rbim.models import Users
def mongo_query_data_reviewer_count(param):
    user_info_count = {}
    user_info_count = Users.mongoObjects.mongo_aggregate([
        {
            '$addFields':{
                '_id':{'$toString':'$_id' }
            }
        },
        {
            '$lookup':
                {
                'from': "rbim_profile",
                'let': { 'user_id': "$id"},
                'pipeline': [
                    {
                        '$addFields':{
                            '_id':{'$toString':'$_id' }
                        }
                    },
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': [ "$user_id",  "$$user_id" ] }
                                ]
                            }
                        }
                    }
                ],
                'as': "profile"
                }
        },
        {
            '$unwind':{
                'path' : '$profile',
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
                            'first_name': { '$ifNull': [ "$first_name", None ] }
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
            '$match': param['match']
        },
        {
            '$project':{
                '_id' : 0,
                'id': { '$ifNull': [ "$id", None ] }
            }
        }
    ])
    count = 0
    count = len(list(user_info_count))
    return count

def mongo_query_data_reviewer_list(param):
    user_info = {}
    user_info = Users.mongoObjects.mongo_aggregate([
        {
            '$addFields':{
                '_id':{'$toString':'$_id' }
            }
        },
        {
            '$lookup':
                {
                'from': "rbim_profile",
                'let': { 'user_id': "$id"},
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': [ "$user_id",  "$$user_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'user_id': { '$ifNull': [ "$user_id", None ] },
                            'dob':{ '$ifNull': [ "$dob", None ] },
                            'age': { 
                                '$divide': [{'$subtract': ["$$NOW", "$dob" ] }, 
                                        (365 * 24*60*60*1000)]
                            },
                            'gender':{ '$ifNull': [ "$gender", None ] },
                            'phone_no':{ '$ifNull': [ "$phone_no", None ] },
                            'official_number':{ '$ifNull': [ "$official_number", None ] },
                            'address':{ '$ifNull': [ "$address", None ] },
                        }
                    }
                ],
                'as': "profile"
                }
        },
        {
            '$unwind':{
                'path' : '$profile',
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
                            'first_name': { '$ifNull': [ "$first_name", None ] }
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
                'role': { '$ifNull': [ "$role", None ] },
                'first_name': { '$ifNull': [ "$first_name", None ] },
                'email': { '$ifNull': [ "$email", None ] },
                'profile':{ '$ifNull': [ "$profile", None ] },
                'barangay':{ '$ifNull': [ "$barangay", None ] },
                'barangay_id':{ '$ifNull': [ "$barangay_id", None ] },
                'created_at':{ '$ifNull': [ "$created_at", None ] },
                'updated_at':{ '$ifNull': [ "$updated_at", None ] },
            }
        }
    ])
    return list(user_info)