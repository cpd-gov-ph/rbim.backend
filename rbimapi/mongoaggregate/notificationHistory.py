from rbim.models import NotificationHistory
def mdb_notification_list_count(param):
    survey_count = {}
    survey_count = NotificationHistory.mongoObjects.mongo_aggregate([
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

def mdb_notification_list(param):
    notification_list = {}
    notification_list = NotificationHistory.mongoObjects.mongo_aggregate([
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
                'title': { '$ifNull': [ "$title", None ] },
                'message': { '$ifNull': [ "$message", None ] },
                'is_seen': { '$ifNull': [ "$is_seen", None ] },
                'created_at': { '$ifNull': [ "$created_at", None ] }
            }
        }
    ])
    return list(notification_list)
   
def mdb_web_notification_list(param):
    notification_list = {}
    notification_list = NotificationHistory.mongoObjects.mongo_aggregate([
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
            '$addFields':{
                'created_at_date': { "$dateToString": { 'format': '%Y-%m-%d', 'date': '$created_at' } }
            }
        },
        {
            '$group':{
                '_id':'$created_at_date',
                'nt_data':{
                    '$push':{
                        'id': { '$ifNull': [ "$id", None ] },
                        'title': { '$ifNull': [ "$title", None ] },
                        'message': { '$ifNull': [ "$message", None ] },
                        'is_seen': { '$ifNull': [ "$is_seen", None ] },
                        'created_at': { '$ifNull': [ "$created_at", None ] }
                    }
                }
            }
        },
        {
            '$project':{
                '_id' : 0,
                'date': { '$ifNull': [ "$_id", None ] },
                'notification_data': { '$ifNull': [ "$nt_data", None ] },
            }
        }
    ])
    return list(notification_list)

def mdb_notification_header_count(param):
    notification_count = {}
    notification_count = NotificationHistory.mongoObjects.mongo_aggregate([
        {
            '$match': param['match']
        },
        {
            '$group': {
                '_id': "",
                'count': { '$sum': 1 }
            }
        },
        {
            '$project':{
                '_id' : 0,
                'count': { '$ifNull': [ "$count", None ] },
            }
        }
    ])
    count = 0
    nh_count = list(notification_count)
    if len(nh_count) > 0:
        count = nh_count[0]['count']
    return count