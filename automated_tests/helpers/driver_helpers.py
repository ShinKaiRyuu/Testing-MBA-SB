import requests
from webium.driver import get_driver
from pages.shopify import MainPage

P_URL = 'http://block-six-analytics.myshopify.com/password'
PASSWORD = 'drieli'
PAYLOAD = {
    'form_type': 'storefront_password',
    'utf8': '%E2%9C%93',
    'password': PASSWORD,
    'commit': 'Enter'
}


def get_shopify_initial_cookies():
    s = requests.Session()
    r = s.post(P_URL, data=PAYLOAD)
    assert 'A la Carte Hourly Services' in r.content.decode("utf-8")
    return s.cookies


def get_updated_driver():
    r_cookies = get_shopify_initial_cookies()
    driver = get_driver()
    driver.set_page_load_timeout(60)
    driver.maximize_window()
    MainPage().open()

    r_cookie = next((c for c in r_cookies if c.name == 'storefront_digest'))
    driver.add_cookie({'name': r_cookie.name, 'value': r_cookie.value, 'domain': r_cookie.domain})

    return driver
