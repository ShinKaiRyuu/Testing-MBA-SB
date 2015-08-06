import random
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from webium import Finds, Find
from .base_page import ScoreboardBasePage

COLUMNS_MAP = {
    'Purchase Type': 4
}


class ClientReportingPage(ScoreboardBasePage):
    url = ScoreboardBasePage.url.format('spotreporting')
    search_btns = Finds(by=By.CSS_SELECTOR, value='input[value="Search for Client Information"]')

    client_info = Find(by=By.CSS_SELECTOR, value='div[ng-show="hubspot"] table.ps')

    cell_xpath = '//tr[contains(@ng-repeat, "client in")]/td[{}]'

    def search_btn_click(self):
        self.search_btns[-1].click()
        time.sleep(1)

    def get_data(self, column):
        cells = Finds(by=By.XPATH, value=self.cell_xpath.format(COLUMNS_MAP[column]), context=self)
        return [c.text for c in cells if c.text]

    def get_all_page_data(self):
        row_xpath = '//tr[contains(@ng-repeat, "client in")]'
        rows = Finds(by=By.XPATH, value=row_xpath, context=self)
        return [row.text for row in rows]

    def to_next_page(self):
        time.sleep(4)
        page = Find(by=By.XPATH, value='//div[@id="clientsList"]//div[.=" >"]', context=self)
        page.click()
        time.sleep(2)

    def to_previous_page(self):
        time.sleep(4)
        page = Find(by=By.XPATH, value='//div[@id="clientsList"]//div[.=" <"]', context=self)
        page.click()
        time.sleep(2)

    def set_date_and_search(self):
        date_field = Find(by=By.CSS_SELECTOR, value='input[ng-model="billingDateFrom"]', context=self)
        date_field.clear()
        date_field.send_keys('2015-01-01')
        self.search_btn_click()
        time.sleep(5)

    def random_client_row_click(self):
        time.sleep(10)
        rows = Finds(by=By.XPATH, value='//tr[contains(@ng-repeat, "client in")]', context=self)
        client_number = random.randint(1, 19)
        rows[client_number].click()
        time.sleep(5)

    def default_wait(self, seconds=30):
        wait = WebDriverWait(self._driver, seconds)
        wait.until(
            lambda x: self._driver.execute_script('return $("#clientsList table.ps tbody tr:nth-of-type(1)").text()'))

    def choose_option_of_select(self, option, select_label):
        options = Finds(
            by=By.XPATH,
            value='(//span[@id]|//label)[starts-with(., "{}")]/..//option[.="{}"]'.format(select_label, option),
            context=self
        )
        options[-1].click()
