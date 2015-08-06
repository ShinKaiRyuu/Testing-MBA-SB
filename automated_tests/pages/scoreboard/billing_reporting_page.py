from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webium import Find, Finds

from .base_page import ScoreboardBasePage


class BillingReportingPage(ScoreboardBasePage):
    url = ScoreboardBasePage.url.format('billingReporting')

    row_names_selects_map = {
        'Purchase Type': 'Service Purchased'
    }

    values_map = {
        'Hourly': 'Hour'
    }

    billing_report_table = Find(by=By.ID, value='gview_billingGrid')
    billing_report_table_text = None
    fields = Finds(by=By.XPATH, value='//tr[@role="row"][@id][1]/td[text()]')
    view_record_widget = Find(by=By.ID, value='viewcntbillingGrid')
    search_record_widget = Find(
        by=By.XPATH, value='//div[contains(@class, "ui-widget")][contains(., "Search...")][@role]')
    search_input = Find(by=By.CSS_SELECTOR, value='input.input-elm')
    search_widget_close_btn = Find(by=By.CSS_SELECTOR, value='span.ui-icon-closethick')

    def get_normalized_value(self, value):
        return self.values_map.get(value, value)

    def get_filtered_data(self, table_name, column):
        self.replace_bad_elements()
        column_name = self.row_names_selects_map.get(column, column)
        column = Find(
            by=By.XPATH,
            value='//span[contains(., "{}")]/../..//div[.="{}"]/parent::th'.format(table_name, column_name),
            context=self
        )
        column_id = column.get_attribute('id')
        rows = Finds(by=By.CSS_SELECTOR, value='td[aria-describedby="{}"]'.format(column_id), context=self)
        rows_text = [r.text for r in rows]
        return set(filter(lambda x: x.strip() and 'Clients' not in x, rows_text))

    def set_date(self, date_type, date_value):
        assert date_type.lower() in ['start', 'end']
        input_id = 'billing_searchMonthFrom' if date_type.lower() == 'start' else 'billing_searchMonthTo'
        date_field = Find(by=By.ID, value=input_id, context=self)
        date_field.clear()
        date_field.send_keys(date_value)

    def save_table(self):
        if not self.billing_report_table_text:
            self.billing_report_table_text = self.billing_report_table.text

    def wait_for_table_change(self):
        wait = WebDriverWait(self._driver, 15)
        wait.until(lambda x: self.billing_report_table_text != self.billing_report_table.text)

    def get_row_data(self):
        self.replace_bad_elements()
        return [f.text for f in self.fields if f.text]

    def select_row(self):
        self.wait_for_loading(seconds=10)
        self.fields[0].click()

    def get_num_of_records(self):
        info = Find(by=By.CSS_SELECTOR, value='.ui-paging-info', context=self)
        return int(info.text.split()[-1])
