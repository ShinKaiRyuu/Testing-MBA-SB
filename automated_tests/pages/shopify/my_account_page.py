from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webium import BasePage, Find
from pages.shopify.main_page import MainPage


class MyAccountPage(BasePage):
    url = 'http://block-six-analytics.myshopify.com/account'

    menu = Find(by=By.CSS_SELECTOR, value='.alignright')
    logout_btn = Find(by=By.ID, value='logoutLink')
    customer_name = Find(by=By.CSS_SELECTOR, value='.customer-name')

    def log_out(self):
        ActionChains(self._driver).move_to_element(self.menu).click(self.logout_btn).perform()
        return MainPage()
