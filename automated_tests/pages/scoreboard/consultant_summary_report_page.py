from datetime import datetime
from selenium.webdriver.common.by import By
from webium import Find, Finds
from .base_page import ScoreboardBasePage


class ConsultantSummaryReportPage(ScoreboardBasePage):
    url = ScoreboardBasePage.url.format('consultantSummaryReport')

    date_picker = Find(by=By.CSS_SELECTOR, value='#dateInput')
    summary_report_text = None
    summary_report_table = Find(by=By.CSS_SELECTOR, value='.general-report')

    current_month = Find(by=By.XPATH, value='//h2[.="{}"]'.format(datetime.now().strftime("%B")))
    table_xpath = '//h2[.="{}"]/following-sibling::div[1]'.format(datetime.now().strftime("%B"))

    def choose_first_day(self):
        self.save_summary_report_text()
        self.date_picker.click()
        Find(by=By.XPATH, value='//a[.="1"][contains(@class, "ui")]', context=self).click()
        self.wait_for_loading(15)

    def save_summary_report_text(self):
        if not self.summary_report_text:
            self.summary_report_text = self.summary_report_table.text

    def click_current_month_link(self):
        self.current_month.click()
        self.wait_for_loading(15)

    def get_invoice_months(self):
        i_xpath = self.table_xpath + '//td[6]'
        invoice_months = Finds(by=By.XPATH, value=i_xpath, context=self)
        return [i.text.split('-')[0] for i in invoice_months]

    def click_client(self):
        client_xpath = self.table_xpath + '//td[1]'
        client = Find(by=By.XPATH, value=client_xpath, context=self)
        client_name = client.text
        client.click()
        self.wait_for_loading(10)
        return client_name

    def get_clients(self):
        client_xpath = self.table_xpath + '//td[1]'
        clients = Finds(by=By.XPATH, value=client_xpath, context=self)
        return [c.text for c in clients if c.text]
