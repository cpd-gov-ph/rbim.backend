EMAIL_TEMPLATE="dynamic_template.html"

SUBJECT_ONBOARD="Welcome to RBIM! Let's get started your account."
EMAIL_MESSAGE_ONBOARD='''\
<p>Hi <b>{}</b>,</p>
<p>Your RBIM account has been created for the role of <b>{}</b>.</p>
<p>&nbsp;</p>
<p>Here are your login credentials.</p>
<p>Username: <b>{}</b></p>
<p>Password: <b>{}</b></p>
<p>&nbsp;</p>
<p>Click on the button to login to your account</p>
<p>
<div align="left" class="alignment">
   <a href="{}" style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#2291a4;border-radius:6px;width:auto;border-top:0px solid transparent;font-weight:undefined;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;font-size:14px;text-align:center;mso-border-alt:none;word-break:keep-all;width:140px;" target="_blank"><span
      style="padding-left:30px;padding-right:30px;font-size:14px;display:inline-block;letter-spacing:normal;">
   <span style="word-break: break-word;">
   <span data-mce-style=""
      style="line-height: 28px;"><strong>Login
   </strong></span></span></span></a>
</div>
</p>
'''

SUBJECT_ACCOUNT_ACTIVE="Welcome to RBIM application/ website. Your account is activated."
EMAIL_MESSAGE_ACCOUNT_ACTIVE='''\
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Hi {},</p> 
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Welcome to RBIM application/ website.</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">This application contains a lot of sensitive data. Please do not share your credentials to anyone. </p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Thanks and have a good day. </p>
'''
NT_MESSAGE_ACCOUNT_ACTIVE='''\
Hi {},
Welcome to RBIM application/ website.
This application contains a lot of sensitive data. Please do not share your credentials to anyone. 
Thanks and have a good day. 
'''


SUBJECT_PROFILE_UPDATE="RBIM - Your account details has been updated"
EMAIL_MESSAGE_PROFILE_UPDATE='''\
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Hi {},</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Your account details has been updated.</p>
<p>Please contact the admin for more details at <a href="mailto:example@rbim.com">example@rbim.com</a></p>
'''
NT_MESSAGE_PROFILE_UPDATE='''\
Hi {},
Your account details has been updated.
Please contact the admin for more details at example@rbim.com
'''



SUBJECT_DC_COMPLETE_SURVEY="RBIM - You have successfully completed your survey and submitted to a DR"
EMAIL_MESSAGE_DC_COMPLETE_SURVEY='''\
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Hi {},</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">You have successfully completed your survey and submitted to a DR. </p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Please wait for a few days to get the survey approval.</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Survey #: {}</p>
'''
NT_MESSAGE_DC_COMPLETE_SURVEY='''\
Hi {},
You have successfully completed your survey and submitted to a DR. 
Please wait for a few days to get the survey approval.
Survey #: {}
'''

SUBJECT_DR_COMPLETE_SURVEY="RBIM - You have successfully completed your survey and submitted to a BO"
EMAIL_MESSAGE_DR_COMPLETE_SURVEY='''\
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Hi {},</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">You have successfully competed approving the survey and submitted to a BO.</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Please wait for a few days to get your survey approved. </p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Survey #: {}</p>
'''
NT_MESSAGE_DR_COMPLETE_SURVEY='''\
Hi {},
You have successfully competed approving the survey and submitted to a BO.
Please wait for a few days to get your survey approved. 
Survey #: {}
'''


SUBJECT_BO_COMPLETE_SURVEY="RBIM - You have successfully completed approving the survey"
EMAIL_MESSAGE_BO_COMPLETE_SURVEY='''\
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Hi {},</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">You have successfully completed approving the survey. </p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">If in case there are any changes in the data given you'll be intimated to make changes to the survey. </p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Survey #: {}</p>
'''
NT_MESSAGE_BO_COMPLETE_SURVEY='''\
Hi {},
You have successfully completed approving the survey. 
If in case there are any changes in the data given you'll be intimated to make changes to the survey. 
Survey #: {}
'''

SUBJECT_BO_APPROVED_SURVEY="RBIM - Your survey has been approved by the BO."
EMAIL_MESSAGE_BO_APPROVED_SURVEY='''\
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Hi {},</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Your survey has been approved by the BO. </p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Survey #: {}</p>
'''
NT_MESSAGE_BO_APPROVED_SURVEY='''\
Hi {},
Your survey has been approved by the BO. 
Survey #: {}
'''

SUBJECT_DR_APPROVED_SURVEY="RBIM - Your survey has been approved by the DR."
EMAIL_MESSAGE_DR_APPROVED_SURVEY='''\
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Hi {},</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Your survey has been approved by the DR. </p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Survey #: {}</p>
'''
NT_MESSAGE_DR_APPROVED_SURVEY='''\
Hi {},
Your survey has been approved by the DR.
Survey #: {}
'''


SUBJECT_DR_REJECTED_SURVEY="RBIM - unfortunately your survey has been rejected by the DR for further correction"
EMAIL_MESSAGE_DR_REJECTED_SURVEY='''\
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Hi {},</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">unfortunately your survey has been rejected by the DR for further correction. Please check your dashboard for recorrection survey to view the rejected survey.</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Survey #: {}</p>
'''
NT_MESSAGE_DR_REJECTED_SURVEY='''\
Hi {},
unfortunately  your survey has been rejected by the DR for further correction. Please check your dashboard for recorrection survey to view the rejected survey.
Survey #: {}
'''


SUBJECT_BO_REJECTED_SURVEY="RBIM - unfortunately your survey has been rejected by the BO for further correction"
EMAIL_MESSAGE_BO_REJECTED_SURVEY='''\
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Hi {},</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">unfortunately your survey has been rejected by the BO for further correction. Please check your dashboard for recorrection survey to view the rejected survey. In case the survey needs to be updated, please reject it and assign a DC for further changes.</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Survey #: {}</p>
'''
NT_MESSAGE_BO_REJECTED_SURVEY='''\
Hi {},
unfortunately your survey has been rejected by the BO for further correction. Please check your dashboard for recorrection survey to view the rejected survey. In case the survey needs to be updated, please reject it and assign a DC for further changes.
Survey #: {}
'''

SUBJECT_BO_AND_DR_PENDING_SURVEY="RBIM - Your pending surveys"
EMAIL_MESSAGE_BO_AND_DR_PENDING_SURVEY='''\
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Hi {},</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">There are pending surveys in your dashboard.</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Survey #: {}</p>
<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 21px;">Please complete the activity and submit the survey at the earliest. </p>
'''
MESSAGE_BO_AND_DR_PENDING_SURVEY='''\
Hi {},
There are pending surveys in your dashboard.
Survey #: {}
Please complete the activity and submit the survey at the earliest. 
'''

