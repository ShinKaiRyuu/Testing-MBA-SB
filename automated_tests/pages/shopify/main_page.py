from selenium.webdriver.common.by import By
from webium import BasePage, Find


class MainPage(BasePage):
    url = 'http://block-six-analytics.myshopify.com/'

    login_link = Find(by=By.ID, value='customer_login_link')
    cart_link = Find(by=By.CSS_SELECTOR, value='a.cart')
