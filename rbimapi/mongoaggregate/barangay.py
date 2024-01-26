from rbim.models import Users
def mongo_query_barangay_count(param):
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
                'from': "rbim_location",
                'let': { 'location_id': "$location_id"},
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': [ "$id",  "$$location_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'name': { '$ifNull': [ "$name", None ] },
                            'code':{ '$ifNull': [ "$code", None ] }
                        }
                    }
                ],
                'as': "location"
             }
        },
        {
            '$unwind':{
                'path' : '$location',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$lookup':
            {
                'from': "rbim_city",
                'let': { 'city_id': "$city_id"},
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': [ "$id",  "$$city_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'name': { '$ifNull': [ "$name", None ] },
                            'code':{ '$ifNull': [ "$code", None ] }
                        }
                    }
                ],
                'as': "city"
             }
        },
        {
            '$unwind':{
                'path' : '$city',
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

def mongo_query_barangay_list(param):
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
                'let': {'user_id': "$id"},
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
                            'age': { '$dateDiff': { 'startDate': "$dob", 'endDate': "$$NOW", 'unit': "year" } },
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
                'from': "rbim_city",
                'let': { 'city_id': "$city_id"},
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': [ "$id",  "$$city_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'name': { '$ifNull': [ "$name", None ] },
                            'code':{ '$ifNull': [ "$code", None ] }
                        }
                    }
                ],
                'as': "city_info"
             }
        },
        {
            '$unwind':{
                'path' : '$city_info',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$lookup':
            {
                'from': "rbim_municipality",
                'let': { 'municipality_id': "$municipality_id"},
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': [ "$id",  "$$municipality_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'name': { '$ifNull': [ "$name", None ] },
                            'code':{ '$ifNull': [ "$code", None ] }
                        }
                    }
                ],
                'as': "municipality_info"
             }
        },
        {
            '$unwind':{
                'path' : '$municipality_info',
                'preserveNullAndEmptyArrays': True
            }
        },
        {
            '$lookup':
            {
                'from': "rbim_location",
                'let': { 'location_id': "$location_id"},
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': [ "$id",  "$$location_id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
                            'name': { '$ifNull': [ "$name", None ] },
                            'code':{ '$ifNull': [ "$code", None ] }
                        }
                    }
                ],
                'as': "location_info"
             }
        },
        {
            '$unwind':{
                'path' : '$location_info',
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
                'city':{ '$ifNull': [ "$city_id", None ] },
                'city_info':{ '$ifNull': [ "$city_info", None ] },
                'municipality':{ '$ifNull': [ "$municipality_id", None ] },
                'municipality_info':{ '$ifNull': [ "$municipality_info", None ] },
                'location':{ '$ifNull': [ "$location_id", None ] },
                'location_info':{ '$ifNull': [ "$location_info", None ] },
                'profile':{ '$ifNull': [ "$profile", None ] },
                'created_at':{ '$ifNull': [ "$created_at", None ] },
                'updated_at':{ '$ifNull': [ "$updated_at", None ] },
            }
        }
    ])
    return list(user_info)