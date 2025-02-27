from django.urls import re_path as url, path
from rbimapi.views.AuthViews import UserLoginAPIView, DataCollectorLoginAPIView, LogoutAPIView, ForgotPasswordAPIView
from rbimapi.views.AuthViews import VerifyCodeAPIView, ResetPasswordAPIView, ResendCodeAPIView, TokenUserViewAPIView
from rbimapi.views.AuthViews import LegalDocumentAgreeAPIView, OptionsCreateUpdateView, OptionsAPIView, LegalAndDocumentationAPIView
from rbimapi.views.SurveyViews import CreateSurveyMasterAPIView, GetSurveyMasterAPIView, CreateSectionAPIView, GetSectionAPIView
from rbimapi.views.SurveyViews import CreateSurveyEntryAPIView, GetSurveyListView, GetSuveryStaticAllQuestionsAPIView
from rbimapi.views.SuperadminViews import CreateSuperAdminAPIView, UpdateSuperAdminAPIView, GetDashboardDetailsAPIVIEW
from rbimapi.views.BarangayViews import LocationAPIView, BarangayRegisterView, BarangayListView, BarangayAPIView
from rbimapi.views.BarangayViews import UpdateBarangayAPIView, CityAPIView, MunicipalityToLocationsAPIView, CityListAPIView
from rbimapi.views.BarangayViews import MunicipalityListAPIView, MunicipalityCreateAPIView
from rbimapi.views.DataReviewerViews import DatareviewerRegisterView, DatareviewerListView, DatareviewerRetrieveAPIView, UpdateDataReviewerAPIView
from rbimapi.views.DataReviewerViews import SurveyReviewSubmitAPIView, OcrReviewSubmitAPIView
from rbimapi.views.DatacollectorViews import DatacollectorRegisterView, DatacollectorListView, DatacollectorRetrieveAPIView, UpdateDataCollectorAPIView
from rbimapi.views.DatacollectorViews import CreateTaskAPIView, HomeTaskDetailsAPIView, ViewTaskAPIView, DeleteTaskAPIView 
from rbimapi.views.DatacollectorViews import DataCollectorTaskListView
from rbimapi.views.CommonViews import BarangayNameListAPIViews, DatareviewerNameListAPIViews, UserRoleIDAPIView
from rbimapi.views.SurveyViews import GetViewSuveryEntryQuestionAPIView, GetSurveyListAPIView, SurveyQuestionVerificationAPIView, SurveyRecorrectionSubmitAPIView
from rbimapi.views.SurveyViews import (OngoingSurveyEntryAPIView, GetHomeDashboardAPIView, SurveyMbLocalAPIView, OcrVerificationAPIView,
                                       GetSuveryRecorrectionListAPIView,GetSuveryYearReportsListAPIView, OcrSurveyMembersUpdateAPIView)
from rbimapi.views.OcrView import (CensusImageUploadAPIView, OcrOptionsAPIView,)
from rbimapi.views.DataReviewerViews import SurveryEntryAPIView
from rbimapi.views.NotificationViews import GetNotificationListView, GetWebHeaderNotificationListView, GetWebViewAllNotificationListView, ClearAllNotificationView
from rbimapi.views.CronViews import GetPendingSurveyAPIView
from rbimapi.views.NotificationViews import DeleteNotificationView, SeenAllNotificationView, GetNotificationHeaderCount
from rbimapi.views.ReportViews import ReportCategoryListAPIView, BarangayListAPIView, GetReportAPIView, BarangayCompletedSurveyChartReportsAPIView, LocationListAPIView
from rbimapi.views.BarangayReportViews import BarangayCompletedSurveyReportsAPIView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^login/$',
        UserLoginAPIView.as_view(),
        name = "superadmin login"),
    url(r'^dc-login/$',
        DataCollectorLoginAPIView.as_view(),
        name='Data Collector Login'),
    url(r'^logout/$',
        LogoutAPIView.as_view(),
        name = "user logout"),
    url(r'^forgot-password/$',
        ForgotPasswordAPIView.as_view(),
        name='Forgot Password'),
    url(r'^verify-code/$',
        VerifyCodeAPIView.as_view(),
        name='Verify Code'),
    url(r'^reset-password/$',
        ResetPasswordAPIView.as_view(),
        name='Reset Password'),
    url(r'^resend-code/$',
        ResendCodeAPIView.as_view(),
        name='Resend Verificationc Code'),
    url(r'^create-survey-master/$', 
        CreateSurveyMasterAPIView.as_view(),
        name='Create Survey Master'),
    url(r'^get-survey-master/$',
        GetSurveyMasterAPIView.as_view(),
        name='Get Survey Master'),
    url(r'^create-survey-section/$',
        CreateSectionAPIView.as_view(),
        name = "Create Section"),
    url(r'^superadmin-register/$',
        CreateSuperAdminAPIView.as_view(),
        name = "superadmin register"),
    url(r'^token-user-view/$',
        TokenUserViewAPIView.as_view(),
        name='superadmin view'),
    url(r'^superadmin-update/(?P<id>.+)/$',
        UpdateSuperAdminAPIView.as_view(),
        name='Update Superadmin'),
    url(r'^location/$',
        LocationAPIView.as_view(),
        name = "Create location"),
    url(r'^create-barangay/$',
        BarangayRegisterView.as_view(),
        name = "Create barangay"),
    url(r'list-barangay/$',
        BarangayListView.as_view(),
        name = "list-barangay"),
    url(r'^view-barangay/(?P<id>.+)/$',
        BarangayAPIView.as_view(),
        name='view-barangay'),
    url(r'^create-datareviewer/$',
        DatareviewerRegisterView.as_view(),
        name='Create DataReviewer'),
    url(r'^list-data-reviewer/$',
        DatareviewerListView.as_view(),
        name='Data Reviewer List'),
    url(r'^view-data-reviewer/(?P<id>.+)/$',
        DatareviewerRetrieveAPIView.as_view(),
        name='view-data-reviewer'),
    url(r'^create-data-collector/$',
        DatacollectorRegisterView.as_view(),
        name='Create DataCollector'),
    url(r'^list-data-collector/$',
        DatacollectorListView.as_view(),
        name='List Data Collector'),
    url(r'^view-data-collector/(?P<id>.+)/$',
        DatacollectorRetrieveAPIView.as_view(),
        name='View Data Collector'),
    url(r'^barangay-name-List/$',
        BarangayNameListAPIViews.as_view(),
        name='Barangay Name List '),
    url(r'^data-reviewer-name-list/(?P<barangay_id>.+)/$',
        DatareviewerNameListAPIViews.as_view(),
        name='Datareviewer Name List'),
    url(r'^legal-document-agree/$',
        LegalDocumentAgreeAPIView.as_view(),
        name = "Legal Document Agree"),  
    url(r'^barangay-update/(?P<id>.+)/$',
        UpdateBarangayAPIView.as_view(),
        name='Update Barangay'),
    url(r'^data-reviewer-update/(?P<id>.+)/$',
        UpdateDataReviewerAPIView.as_view(),
        name='Update Data Reviewer'),
    url(r'^data-collector-update/(?P<id>.+)/$',
        UpdateDataCollectorAPIView.as_view(),
        name='Update Data Collector'),
    url(r'^city/$',
        CityAPIView.as_view(),
        name = "Create City"),
    url(r'^municipality-to-locations/(?P<municipality>.+)/$',
        MunicipalityToLocationsAPIView.as_view(),
        name = "City to location"),
    url(r'^city-list/$',
        CityListAPIView.as_view(),
        name = "City List"),
    url(r'^city-to-municipality/(?P<city>.+)/$',
        MunicipalityListAPIView.as_view(),
        name = "City to Municipality"),
    url(r'^municipality/$',
        MunicipalityCreateAPIView.as_view(),
        name = "City List"),  
    url(r'^create-task/$',
        CreateTaskAPIView.as_view(),
        name = "Create Task"),
    url(r'^home-task-details/$',
        HomeTaskDetailsAPIView.as_view(),
        name='Home Task Details'),
    url(r'^view-task/(?P<id>.+)/$',
        ViewTaskAPIView.as_view(),
        name='View Task'),
    url(r'^delete-task/(?P<id>.+)/$',
        DeleteTaskAPIView.as_view(),
        name='Delete Task'),
    url(r'^data-collector-task-list/$',
        DataCollectorTaskListView.as_view(),
        name='Task List'),
    url(r'^options-update-or-create/$',
        OptionsCreateUpdateView.as_view(),
        name = "options create"),
    url(r'^view-options/(?P<meta_key>.+)/$',
        OptionsAPIView.as_view(),
        name='view-options'),
    url(r'^legal-and-documentation/$',
        LegalAndDocumentationAPIView.as_view(),
        name='view-options'),
    url(r'^get-section-details/(?P<id>.+)/$',
        GetSectionAPIView.as_view(),
        name='Get Section Details'),
    url(r'^create-survey-entry/$',
        CreateSurveyEntryAPIView.as_view(),
        name='Create Survey Entry'),
    url(r'^get-survey-list/$',
        GetSurveyListView.as_view(),
        name='Get Survey List'),
    url(r'^get-suvery-static-all-questions/$',
        GetSuveryStaticAllQuestionsAPIView.as_view(),
        name='Get Suvery Static All Questions'),
    url(r'^get-dashboard-detailes/$',
        GetDashboardDetailsAPIVIEW.as_view(),
        name='Get Dashboard Informations'),
    url(r'^view-suvery-entry-question/(?P<survey_entry_id>.+)/$',
        GetViewSuveryEntryQuestionAPIView.as_view(),
        name='view-suvery-entry-question'),
    url(r'^get-mb-survey-list/$',
        GetSurveyListAPIView.as_view(),
        name='get-mb-survey-list'),
    url(r'^survey-question-verification/$',
        SurveyQuestionVerificationAPIView.as_view(),
        name='survey-question-verification'),
    url(r'^survey-recorrection-submit/$',
        SurveyRecorrectionSubmitAPIView.as_view(),
        name='survey-recorrection-submit'),
    url(r'^ongoing-survey-entry-submit/$',
        OngoingSurveyEntryAPIView.as_view(),
        name='ongoing-survey-entry-submit'),
    url(r'^home-dashboard-details/$',
        GetHomeDashboardAPIView.as_view(),
        name='home-dashboard-details'),
    url(r'^survey-entry-details/(?P<id>.+)/$',
        SurveryEntryAPIView.as_view(),
        name='survey-entry-details'),
    url(r'^survey-review-submit/$',
        SurveyReviewSubmitAPIView.as_view(),
        name='survey-review-submit'),
    url(r'^survey-mb-local/(?P<survey_entry_id>.+)/$',
        SurveyMbLocalAPIView.as_view(),
        name='survey-review-submit'),
    url(r'^ocr-question-verification/$',
        OcrVerificationAPIView.as_view(),
        name='ocr-question-verification'),
    url(r'^ocr-review-submit/$',
        OcrReviewSubmitAPIView.as_view(),
        name='survey-review-submit'),
    url(r'^suvery-recorrection-list/$',
        GetSuveryRecorrectionListAPIView.as_view(),
        name='suvery-recorrection-list'),
    url(r'^get-notification-list/$',
        GetNotificationListView.as_view(),
        name='Get notification List'),
    url(r'^get-pending-survey-list/$',
        GetPendingSurveyAPIView.as_view(),
        name='Get Pending Survey'),
    url(r'^get-web-header-notification-list/$',
        GetWebHeaderNotificationListView.as_view(),
        name='Get Web Header Notification'),
    url(r'^get-web-viewall-notification-list/$',
        GetWebViewAllNotificationListView.as_view(),
        name='Get Web View All Notification'),
    url(r'^clear-all-notification/$',
        ClearAllNotificationView.as_view(),
        name='Clear All Notification'),
    url(r'^delete-notification/(?P<id>.+)/$',
        DeleteNotificationView.as_view(),
        name='Delete Notification'),
    url(r'^suvery-year-reports/$',
        GetSuveryYearReportsListAPIView.as_view(),
        name='Suvery Year Reports'),
    url(r'^seen-all-notification/$',
        SeenAllNotificationView.as_view(),
        name='Seen All Notification'),
    url(r'^get-notification-header-count/$',
        GetNotificationHeaderCount.as_view(),
        name='Get Notification Header Count'),
    url(r'^barangay-completed-survey-reports/$',
        BarangayCompletedSurveyReportsAPIView.as_view(),
        name='Barangay Completed Survey Reports'),
    url(r'^ocr-survey-entry/$',
        CensusImageUploadAPIView.as_view(),
        name='ocr-survey-entry'),
    url(r'^ocr-survey-entry/(?P<survey_entry_id>.+)/$',
        CensusImageUploadAPIView.as_view(),
        name='cr-survey-entry-images'),
    url(r'^ocr-options/$',
        OcrOptionsAPIView.as_view(),
        name='ocr-options'),
    url(r'^update-ocr-survey-members/$',
        OcrSurveyMembersUpdateAPIView.as_view(),
        name='update-ocr-survey-members'),
    url(r'^get-report-category-list/$',
        ReportCategoryListAPIView.as_view(),
        name='Get Report Category List'),
    url(r'^get-barangay-list/$',
        BarangayListAPIView.as_view(),
        name='Get Barangay List'),
    url(r'^get-report-details/$',
        GetReportAPIView.as_view(),
        name='Get Report Details'),
    url(r'^get-survey-report-excel/$',
        BarangayCompletedSurveyChartReportsAPIView.as_view(),
        name='Survey-Report-Excel'),
    url(r'^get-location-list/$',
        LocationListAPIView.as_view(),
        name='Get Location List'),
    url(r'^get-official-id/$',
        UserRoleIDAPIView.as_view(),
        name='Get Official ID'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
