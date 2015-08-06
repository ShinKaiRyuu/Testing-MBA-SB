from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class RegistrationPage(BasePage):
    url = 'http://block-six-analytics.myshopify.com/account/login'

    f_name = Find(by=By.CSS_SELECTOR, value='input#first_name')
    l_name = Find(by=By.CSS_SELECTOR, value='input#last_name')
    email = Find(by=By.CSS_SELECTOR, value='input#email')
    password = Find(by=By.CSS_SELECTOR, value='input#password')
    create_btn = Find(by=By.CSS_SELECTOR, value='input[value="Register"]')
    errors = Finds(by=By.CSS_SELECTOR, value='.errors li')

    def register_with(self, kwargs):
        self.clear_send_keys('f_name', kwargs)
        self.clear_send_keys('l_name', kwargs)
        self.clear_send_keys('email', kwargs)
        self.clear_send_keys('password', kwargs)
        self.create_btn.click()

    def clear_send_keys(self, element_name, kwargs):
        value = kwargs.get(element_name)
        element = getattr(self, element_name)
        element.clear()
        element.send_keys(value)

    def get_error_messages(self):
        return [e.text for e in self.errors]
