from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class LoginPage(BasePage):
    url = 'http://block-six-analytics.myshopify.com/account/login'

    username = Find(by=By.ID, value='customer_email')
    password = Find(by=By.ID, value='customer_password')
    login_btn = Find(by=By.XPATH, value='//input[@value="Login" or @value="Sign In"]')
    errors = Finds(by=By.CSS_SELECTOR, value='.errors li')

    def login_with(self, kwargs):
        self.clear_send_keys('username', kwargs)
        self.clear_send_keys('password', kwargs)
        self.login_btn.click()

    def clear_send_keys(self, element_name, kwargs):
        value = kwargs.get(element_name)
        element = getattr(self, element_name)
        element.clear()
        element.send_keys(value)

    def get_error_messages(self):
        return [e.text for e in self.errors]
