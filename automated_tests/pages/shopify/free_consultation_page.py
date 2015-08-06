from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds
import time


class FreeConsultationPage(BasePage):
    url = 'http://54.200.35.118/scoreboard/scoreboard/web/site/free-consultation'
    # url = 'http://block-six-analytics.myshopify.com/pages/free-consultation'
    # iframe = Find(by=By.CSS_SELECTOR, value='#freeConsultationForm')

    f_name = Find(by=By.CSS_SELECTOR, value='#freeconsultation-first_name')
    l_name = Find(by=By.CSS_SELECTOR, value='#freeconsultation-last_name')
    email = Find(by=By.CSS_SELECTOR, value='#freeconsultation-email')
    phone = Find(by=By.CSS_SELECTOR, value='#freeconsultation-phone')
    password = Find(by=By.CSS_SELECTOR, value='#freeconsultation-password')
    repeat_pass = Find(by=By.CSS_SELECTOR, value='#freeconsultation-password2')

    hear_how = Finds(by=By.CSS_SELECTOR, value='#freeconsultation-hear_how option')
    cons_name = Find(by=By.CSS_SELECTOR, value='#freeconsultation-consultant_name')
    subscr = Finds(by=By.CSS_SELECTOR, value='#freeconsultation-subscribe label')
    programs = Finds(by=By.CSS_SELECTOR, value='p.field-freeconsultation-programs input[type="text"]')
    month = Find(by=By.CSS_SELECTOR, value='#freeconsultation-whenmonth')
    year = Find(by=By.CSS_SELECTOR, value='#freeconsultation-whenyear')

    instit = Find(by=By.CSS_SELECTOR, value='#freeconsultation-institution_u')
    gpa = Find(by=By.CSS_SELECTOR, value='#freeconsultation-institution_gpa')
    major = Find(by=By.CSS_SELECTOR, value='#freeconsultation-institution_major')
    YoG = Finds(by=By.CSS_SELECTOR, value='#freeconsultation-institution_year option')

    gmat_gre = Finds(by=By.CSS_SELECTOR, value='#freeconsultation-gmat_gre label')
    resume = Find(by=By.CSS_SELECTOR, value='#freeconsultation-resume')
    comments = Find(by=By.CSS_SELECTOR, value='#freeconsultation-comments')
    goals = Find(by=By.CSS_SELECTOR, value='#freeconsultation-goal')

    submit_btn = Find(by=By.CSS_SELECTOR, value='input[value="Submit Form"]')
    reset_btn = Find(by=By.CSS_SELECTOR, value='input[value="Reset Form"]')

    captcha = Find(by=By.CSS_SELECTOR, value='#freeconsultation-captcha')
    s_message_element = Find(by=By.XPATH, value='//div[@class="container"]/p[1]')
    success_message = 'Thank you for submitting your request for a free mbaMission consultation!'

    def fill_contact_information(self, first=None, **kwargs):
        if first:
            self.clear_send_keys('f_name', kwargs)
            self.clear_send_keys('l_name', kwargs)
            self.clear_send_keys('email', kwargs)
            self.clear_send_keys('phone', kwargs)
            self.clear_send_keys('password', kwargs)
            self.clear_send_keys('repeat_pass', kwargs)
        else:
            self.select_option_or_radio('hear_how', kwargs)
            self.clear_send_keys('cons_name', kwargs)
            self.select_option_or_radio('subscr', kwargs)
            self.multiple_clear_send_keys('programs', kwargs)
            self.clear_send_keys('month', kwargs)
            self.clear_send_keys('year', kwargs)

    def fill_academic_information(self, **kwargs):
        self.clear_send_keys('instit', kwargs)
        self.clear_send_keys('gpa', kwargs)
        self.clear_send_keys('major', kwargs)
        self.select_option_or_radio('YoG', kwargs)

    def clear_send_keys(self, element_name, kwargs):
        value = kwargs.get(element_name)
        element = getattr(self, element_name)
        element.clear()
        element.send_keys(value)

    def multiple_clear_send_keys(self, element_name, kwargs):
        values = kwargs.get(element_name)
        elements = getattr(self, element_name)
        for v, el in zip(values, elements):
            el.clear()
            el.send_keys(v)

    def select_option_or_radio(self, element_name, kwargs):
        value = kwargs.get(element_name)
        if value:
            options = getattr(self, element_name)
            option = next(filter(lambda x: value.lower() in x.text.lower(), options))
            option.click()

    def submit(self):
        self.submit_btn.click()
        time.sleep(1)

    def get_error_messages(self):
        errors_xpath = (
            '//label[@class="error" or @class="customError"][not(contains(@style, "display"))][string-length(.) > 0]')
        errors = Finds(by=By.XPATH, value=errors_xpath, context=self)
        return [e.text for e in errors]
