from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webium import Find, Finds
from webium.driver import get_driver

from .base_page import ScoreboardBasePage


class MainPage(ScoreboardBasePage):
    url = ScoreboardBasePage.url.format('homepage')

    username = Find(by=By.ID, value='loginUsername')
    password = Find(by=By.ID, value='loginPassword')
    login_btn = Find(by=By.ID, value='loginButton')
    errors = Finds(by=By.CSS_SELECTOR, value='#loginError')

    def login_with(self, kwargs):
        self.clear_send_keys('username', kwargs)
        self.clear_send_keys('password', kwargs)
        self.login_btn.click()
        if kwargs['success']:
            WebDriverWait(get_driver(), 10).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, 'a.scoreboardLogoutButton'))
            )

    def clear_send_keys(self, element_name, kwargs):
        value = kwargs.get(element_name)
        element = getattr(self, element_name)
        element.clear()
        element.send_keys(value)

    def get_error_messages(self):
        return [e.text for e in self.errors]
