from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
import threading
import requests
import json
import staticContent
class ThreadManager:
    def email_trigger_jobs(param):
        thread_process = threading.Thread(target=DoThreadManager.do_email, args=(param,), kwargs={})
        thread_process.daemon = True
        thread_process.start()
        return None
    
    def push_notification_trigger_jobs(param):
        thread_process = threading.Thread(target=DoThreadManager.do_push_notification, args=(param,), kwargs={})
        thread_process.daemon = True
        thread_process.start()
        return None

class DoThreadManager:
    def do_email(param):
        message = ""
        htmly = get_template(param["template"])
        html_content = htmly.render(param["context"])
        msg = EmailMultiAlternatives(param["subject"], message, settings.EMAIL_HOST_USER, [param["email"]])
        msg.attach_alternative(html_content, "text/html")
        msg.send()  
        return None

    def do_push_notification(param):
        url = settings.FCM_URL
        payload = staticContent.push_notification_payload(param)
        requests.post(url, data=json.dumps(payload), headers=staticContent.push_notification_header(FCM_API = settings.FCM_API))
        return None