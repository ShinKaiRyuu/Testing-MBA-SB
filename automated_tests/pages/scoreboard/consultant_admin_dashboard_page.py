from selenium.webdriver.common.by import By
from webium import Find, Finds
from .base_page import ScoreboardBasePage


class ConsultantAdminDashboardPage(ScoreboardBasePage):
    url = ScoreboardBasePage.url.format('consultantAdminDashboard')

    date_picker = Find(by=By.CSS_SELECTOR, value='#dateInput')
    summary_consultants_text = None
    summary_consultants_table = Find(by=By.CSS_SELECTOR, value='#gview_summaryConsultantsData')

    consultant_num = 3

    def choose_first_day(self):
        self.save_summary_consultants_text()
        self.date_picker.click()
        Find(by=By.XPATH, value='//a[.="1"][contains(@class, "ui")]', context=self).click()
        self.wait_for_loading(15)

    def save_summary_consultants_text(self):
        if not self.summary_consultants_text:
            self.summary_consultants_text = self.summary_consultants_table.text

    def select_consultant(self):
        self.wait_for_loading(15)
        consultants = Finds(by=By.CSS_SELECTOR, value='.consultantDashboard', context=self)
        consultant_name = consultants[self.consultant_num].text
        consultants[self.consultant_num].click()
        return consultant_name
