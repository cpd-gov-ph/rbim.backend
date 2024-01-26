from rbim.models import SurveyEntry, Users, Location
def barangay_list(param):
    barangay_details = {}
    barangay_details = SurveyEntry.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
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
            '$project': {
                "_id":0,
                "id": { '$ifNull': [ "$barangay.id", None ] },
                "first_name": { '$ifNull': [ "$barangay.first_name", None ] }
            }
        }
    ])
    return list(barangay_details)

def location_barangay_list(param):
    barangay_details = {}
    barangay_details = Users.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$lookup':
            {
                'from': "rbim_users",
                'let': { 'id': "$id"},
                'pipeline': [
                    { 
                        '$match': { 
                            '$expr': { 
                                '$and': [
                                    {'$eq': [ "$id",  "$$id" ] }
                                ]
                            }
                        }
                    },
                    {
                        '$project':{
                            '_id' : 0,
                            'id': { '$ifNull': [ "$id", None ] },
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
            '$project': {
                "_id":0,
                "id": { '$ifNull': [ "$barangay.id", None ] },
            }
        },
        {'$group': { '_id': 0, 'id':{'$push': '$id'}}}
    ])
    return list(barangay_details)

def location_list(param):
    location_details = {}
    location_details = Location.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$skip':param['skip']
        },
        {
            '$limit':param['page_size']
        },
        {
            '$project': {
                "_id":0,
                "id": { '$ifNull': [ "$id", None ] },
                "name": { '$ifNull': [ "$name", None ] }
            }
        }
    ])
    return list(location_details)