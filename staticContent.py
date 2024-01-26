def email_trigger_param(title, email, html_content, template, message):
    param = {
        "subject":title,
        "message":message,
        "email":email,
        "context":{
            "html_content":html_content
        },
        "template":template
    }
    return param

def push_notification_trigger_param(title, fcm_token, html_content):
    param = {
        "subject":title,
        "fcm_token":fcm_token,
        "html_content":html_content      
    }
    return param

def push_notification_header(FCM_API):
    header = {
        "Content-Type":"application/json",
        "Authorization": "key="+ FCM_API
    }
    return header

def push_notification_payload(param):
    payload ={
        "to": param["fcm_token"],
        "notification": {
            "title": param["subject"],
            "body": param["html_content"],
            "mutable_content": True,
            "sound": True
        }
    }
    return payload

def forgot_password_param(email, code, template, message, ):
    param = {
            "subject":"Verification Code",
            "message": message,
            "email":email,
            "context":{
                'Username': email,
                'Code': code
            },
            "template": template
        }
    return param

def notification_param(sender, receiver, title, nt_message, email_message, email):
    param = {
        "sender":sender,
        "receiver":receiver,
        "title": title,
        "message":nt_message,
        "email_message":email_message,
        "email":email
    }
    return param

def pagination_param(total_records, num_pages, page, obj_info):
    paginator = {
        "total_records": total_records,
        "total_pages":num_pages,
        "current_page":page,
        "current_page_size": len(obj_info),
        'next_page': None if (num_pages == page or total_records == 0) else (page+1),
        'previous_page': (page-1),
    }
    return paginator

def survey_report_param(survey_entry_ids, survey_status, barangay_id):
    param = {
        "match": {
            "id": {'$in': survey_entry_ids},
            "status": survey_status, #survey_completed
            "barangay_id":barangay_id
        }
    }
    return param

def survey_report_select_all_param(survey_status, barangay_id):
    param = {
        "match": {
            "status": survey_status, #survey_completed
            "barangay_id":barangay_id,
        }
    }
    return param
