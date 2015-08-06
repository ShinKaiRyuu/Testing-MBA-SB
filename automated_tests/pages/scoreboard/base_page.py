from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webium import BasePage, Find, Finds


class ScoreboardBasePage(BasePage):
    url = 'http://mbamission.scoreboard-qa.selfip.com1/pages/{}'
    logout_btn = Find(by=By.CSS_SELECTOR, value='a.scoreboardLogoutButton')
    to_login_form_btn = Find(by=By.CSS_SELECTOR, value='a.scoreboardLoginButton')

    def log_out(self):
        self.logout_btn.click()
        wait = WebDriverWait(self._driver, 10)
        wait.until(lambda x: self.is_logged_out() is True)
        return self

    def is_logged_out(self):
        return 'pages/logout' in self._driver.current_url

    def choose_option_of_select(self, option, select_label):
        Find(
            by=By.XPATH,
            value='(//span[@id]|//label)[starts-with(., "{}")]/..//option[.="{}"]'.format(select_label, option),
            context=self
        ).click()

    def click_btn_by_text(self, btn_text):
        self.wait_for_loading()
        Find(by=By.XPATH, value='//button[.="{}"]'.format(btn_text), context=self).click()

    def click_btn_by_title(self, btn_title):
        self.wait_for_loading()
        Finds(
            by=By.XPATH,
            value='//td[@title="{0}"]//span | //div[.="{0}"]/span'.format(btn_title),
            context=self
        )[-1].click()

    def click_by_text(self, text):
        self.wait_for_loading()
        Find(by=By.XPATH, value='//a[.="{}"]'.format(text), context=self).click()

    def wait_for_loading(self, seconds=180):
        wait = WebDriverWait(self._driver, seconds)
        wait.until(lambda x: self._driver.execute_script('return jQuery.active == 0') is True)

    def get_message(self):
        self.wait_for_loading(10)
        return Find(by=By.CSS_SELECTOR, value='h2', context=self).text

    def replace_bad_elements(self):
        self._driver.execute_script("$('span.break').replaceWith(' '); $('br').replaceWith(' ')")
        self._driver.execute_script("$('br').replaceWith(' ')")
