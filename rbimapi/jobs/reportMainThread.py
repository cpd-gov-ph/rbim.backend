import threading
from rbimapi.jobs import reportConstants as constants
from rbimapi.jobs.reportPieThread import PieReports
from rbimapi.jobs.reportBarThread import BarReports
from rbim.models import ReportCategories, ReportHistory, SurveyEntry

class SurveyReportThread(threading.Thread):
    def __init__(self, survey_entry_id):
        self.survey_entry_id = survey_entry_id
        threading.Thread.__init__(self, daemon=True)

    def create_report_pie_chart_constants(self, location_id):
        for category in range(len(constants.PIE_CHART_SLUG)):
            category_obj = ReportCategories.objects.get(category_slug=constants.PIE_CHART_SLUG[category])
            ReportHistory.objects.create(
                report_category_id=category_obj.id,
                location_id=location_id,
                chart_constant_left=constants.LEFT_PIE_CHART_CONSTANTS[category],
                chart_constant_right=constants.RIGHT_PIE_CHART_CONSTANTS[category],
                chart_response_left={"type": constants.CHART_TYPE[0],
                                     "title": constants.PIE_CHART_TITLE_LEFT[category],
                                     "datasets": [{"data": [], "backgroundColor": [], "borderWidth":0,
                                                   "total_population": 0}],
                                     "labels": constants.LEFT_CHART_LABELS[category],
                                    },
                chart_response_right={"type": constants.CHART_TYPE[0],
                                      "title": constants.PIE_CHART_TITLE_RIGHT[category],
                                      "datasets": [{"data": [], "backgroundColor": [], "borderWidth":0,
                                                    "total_population": 0}],
                                      "labels": constants.RIGHT_CHART_LABELS[category],
                                     },
                chart_unique_constant_left=[],
                chart_unique_constant_right=[],
                excel_response = constants.PIE_EXCEL_RESPONSE[category],
                excel_constant = constants.PIE_EXCEL_CONSTANTS[category]
            )
        return True

    def create_report_bar_chart_constants(self, location_id):
        for category in range(len(constants.BAR_CHART_SLUG)):
            category_obj = ReportCategories.objects.get(category_slug=constants.BAR_CHART_SLUG[category])
            ReportHistory.objects.create(
                report_category_id=category_obj.id,
                location_id=location_id,
                chart_constant_left=constants.BAR_CHART_CONSTANTS[category],
                chart_constant_right={},
                chart_response_left={"type": constants.CHART_TYPE[1],
                                    "title": constants.BAR_CHART_TITLE[category],
                                    "x_axis_name": constants.BAR_CHART_X_AXIS[category],
                                    "datasets": [],
                                    "labels": constants.BAR_CHART_LABELS[category],
                                    "total_population": 0},
                chart_response_right= {},
                chart_unique_constant_left=[],
                chart_unique_constant_right=[],
                excel_response=constants.BAR_CHART_EXCEL_RESPONSE[category],
                excel_constant=constants.BAR_CHART_EXCEL_CONSTANTS[category]
            )
        return True

    def run(self):
        survey_obj = SurveyEntry.objects.get(id=self.survey_entry_id)
        if not ReportHistory.objects.filter(location_id=survey_obj.barangay.location.id).count():
            self.create_report_pie_chart_constants(location_id=survey_obj.barangay.location.id)
            self.create_report_bar_chart_constants(location_id=survey_obj.barangay.location.id)
        pie_report_process = PieReports(survey_entry_id=self.survey_entry_id)
        bar_report_process = BarReports(survey_entry_id=self.survey_entry_id)
        pie_report_process.get_household_members()
        bar_report_process.get_household_members()

def call_survey_report_thread(survey_entry_id):
    SurveyReportThread(survey_entry_id).start()