from selenium.webdriver.common.by import By
import time
from webium import Find, Finds
from webium.controls.select import Select

from .base_page import ScoreboardBasePage


class ManageBillingPage(ScoreboardBasePage):
    url = ScoreboardBasePage.url.format('manageBilling')

    add_record_widget = Find(by=By.XPATH, value='//div[@id="editmodbillingGrid"][contains(., "Add Record")]')
    edit_record_widget = Find(by=By.XPATH, value='//div[@id="editmodbillingGrid"][contains(., "Edit Record")]')
    view_record_widget = Find(by=By.XPATH, value='//div[@id="viewmodbillingGrid"][contains(., "View Record")]')
    delete_widget = Find(by=By.XPATH, value='//div[@id="delmodbillingGrid"][contains(., "Delete")]')
    search_records_widget = Find(by=By.XPATH, value='//div[@id="searchmodfbox_billingGrid"][contains(., "Search...")]')
    copy_record_widget = Find(by=By.XPATH, value='//div[@id="edithdbillingGrid"][contains(., "Copy Record")]')
    auditing_of_the_user_widget = Find(by=By.XPATH, value='//span[@id="ui-dialog-title-auditDialog"]/../..')

    row_xpath = '//tr[@role="row"][@id]'
    cell = 'td[aria-describedby="{}"]'

    search_input = Find(by=By.CSS_SELECTOR, value='input.input-elm')
    search_widget_close_btn = Find(by=By.CSS_SELECTOR, value='span.ui-icon-closethick')

    first_name_field = Find(by=By.ID, value='firstname')
    last_name_field = Find(by=By.ID, value='lastname')
    email_field = Find(by=By.ID, value='email')
    amount_field = Find(by=By.ID, value='amount')

    def close_confirmation_widget(self):
        time.sleep(2)
        Finds(by=By.CSS_SELECTOR, value='span.ui-icon-closethick', context=self)[-1].click()
        self.wait_for_loading()

    def get_row_data(self, row_number=0):
        # TODO extend row data
        data = {
            'first_name': Finds(
                by=By.CSS_SELECTOR,
                value=self.cell.format('billingGrid_firstname'),
                context=self)[row_number].text,
            'last_name': Finds(
                by=By.CSS_SELECTOR,
                value=self.cell.format('billingGrid_lastname'),
                context=self)[row_number].text,
            'email': Finds(
                by=By.CSS_SELECTOR,
                value=self.cell.format('billingGrid_email'),
                context=self)[row_number].text,
            'fiscal_year': Finds(
                by=By.CSS_SELECTOR,
                value=self.cell.format('billingGrid_finyearid'),
                context=self)[row_number].text,
            'service': Finds(
                by=By.CSS_SELECTOR,
                value=self.cell.format('billingGrid_serviceid'),
                context=self)[row_number].text,
            'amount': Finds(
                by=By.CSS_SELECTOR,
                value=self.cell.format('billingGrid_amount'),
                context=self)[row_number].text
        }
        return data

    def add_row(self, data):
        if data.get('first_name'):
            self.first_name_field.clear()
            self.first_name_field.send_keys(data.get('first_name'))
        if data.get('last_name'):
            self.last_name_field.clear()
            self.last_name_field.send_keys(data.get('last_name'))
        if data.get('email'):
            self.email_field.clear()
            self.email_field.send_keys(data.get('email'))
        if data.get('fiscal_year'):
            Find(
                by=By.XPATH,
                value='//select[@id="finyearid"]/option[.="{}"]'.format(data.get('fiscal_year')),
                context=self
            ).click()
        if data.get('service'):
            Find(
                by=By.XPATH,
                value='//select[@id="serviceid"]/option[.="{}"]'.format(data.get('service')),
                context=self
            ).click()
        if data.get('amount'):
            self.amount_field.clear()
            self.amount_field.send_keys(data.get('amount')[1:-3])

    def select_row(self):
        self.wait_for_loading()
        Find(by=By.XPATH, value=self.row_xpath, context=self).click()

    def get_row_data_widget(self):
        service = Find(Select, by=By.ID, value='serviceid', context=self)
        fiscal_year = Find(Select, by=By.ID, value='finyearid', context=self)
        data = {
            'first_name': self.first_name_field.get_attribute('value'),
            'last_name': self.last_name_field.get_attribute('value'),
            'email': self.email_field.get_attribute('value'),
            'fiscal_year': fiscal_year.get_text_selected(),
            'service': service.get_text_selected(),
            'amount': self.amount_field.get_attribute('value')
        }
        return data

    def get_active_widget_text(self):
        return self._driver.execute_script("return $('div[role=dialog][style*=\"display: block\"]').text()")
