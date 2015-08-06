from selenium.webdriver.common.by import By
from webium import Find, Finds
from .base_page import ScoreboardBasePage

FIELDS_MAP = {
    'Fiscal year': 'clientBilling_finYearId',
    'Contract status': 'clientBilling_contractStatus',
    'Consultant': 'clientBilling_consultantId',
    'Free Consultant': 'clientBilling_freeConsultantId'
}


class ConsultantDashboardPage(ScoreboardBasePage):
    url = ScoreboardBasePage.url.format('consultantDashboard')
    date_picker = Find(by=By.CSS_SELECTOR, value='#dateInput')
    consultant_billing_table = Find(by=By.ID, value='consultantBilling')
    consultant_billing_table_text = None

    row_xpath = '//div[contains(., "{}")][@class="ui-jqgrid-view"]//tr[contains(@class, "content")]'
    client_pluses = Finds(by=By.CSS_SELECTOR, value='span.ui-icon-plus')

    statuses = Finds(by=By.XPATH, value='//td[@aria-describedby="daytodayactivities_clientOpen"]//a')

    school_name = Find(by=By.CSS_SELECTOR, value='input[name="schoolName"]')
    interview_option_xpath = '//select[@name="interview"]/option[.="{}"]'
    status_option_xpath = '//select[@name="clientStatus"]/option[.="{}"]'
    acceptance_option_xpath = '//select[@name="acceptance"]/option[.="{}"]'
    date_field = Find(by=By.CSS_SELECTOR, value='input[name="invoiceDate"]')
    now_bnt = Find(by=By.CSS_SELECTOR, value='.ui-datepicker-current')

    def choose_first_day(self):
        self.save_consultant_billing_text()
        self.date_picker.click()
        Find(by=By.XPATH, value='//a[.="1"][contains(@class, "ui")]', context=self).click()
        self.wait_for_loading(15)

    def save_consultant_billing_text(self):
        if not self.consultant_billing_table_text:
            self.consultant_billing_table_text = self.consultant_billing_table.text

    def get_row(self, table_name):
        return Find(by=By.XPATH, value=self.row_xpath.format(table_name), context=self)

    def select_row(self, table_name):
        self.get_row(table_name).click()

    def update_field(self, field_name, field_value):
        aria_describedby = FIELDS_MAP[field_name]
        Find(
            by=By.XPATH,
            value='//td[@aria-describedby="{}"]/select/option[.="{}"]'.format(aria_describedby, field_value),
            context=self
        ).click()

    def get_row_data(self, table_name='Client Billing'):
        self.wait_for_loading(10)
        cell_xpath = self.row_xpath.format(table_name) + '[1]/td'
        cells = Finds(by=By.XPATH, value=cell_xpath, context=self)
        return [c.text for c in cells]

    def get_active_client_number(self):
        self.wait_for_loading(10)
        statuses = [e.get_attribute('title') for e in self.statuses]
        number = None
        for i, s in enumerate(statuses):
            if s == 'Close this client':
                number = i
                break

        if number is None:
            number = 0
            self.activate_first_client()
        return number

    def activate_first_client(self):
        switcher = Find(by=By.CSS_SELECTOR, value='.iSwitcher a', context=self)
        switcher.click()
        term = Find(by=By.XPATH, value='//span[.="Long Term"]', context=self)
        term.click()
        self.wait_for_loading(5)

    def click_client_plus(self, number):
        self.client_pluses[number].click()
        self.wait_for_loading(10)

    def click_transaction_plus(self):
        transaction_plus = Find(by=By.CSS_SELECTOR, value='.subgrid-data span.ui-icon-plus', context=self)
        transaction_plus.click()
        self.wait_for_loading(10)

    def add_invoice(self, data):
        self.school_name.send_keys(data.get('schoolName'))
        Find(by=By.XPATH, value=self.interview_option_xpath.format(data.get('interview')), context=self).click()
        Find(by=By.XPATH, value=self.status_option_xpath.format(data.get('clientStatus')), context=self).click()
        Find(by=By.XPATH, value=self.acceptance_option_xpath.format(data.get('acceptance')), context=self).click()
        self.date_field.click()
        self.now_bnt.click()
        self.wait_for_loading(10)

    def get_invoice_text(self):
        self.wait_for_loading(10)
        invoices = Finds(by=By.CSS_SELECTOR, value='.subgrid-data tr.ui-row-ltr', context=self)
        return invoices[-1].text
