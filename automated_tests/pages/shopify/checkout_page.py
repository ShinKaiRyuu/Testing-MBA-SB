from selenium.webdriver.common.by import By
from webium import BasePage, Find

BILLING_INFO = {
    'f_name': '',
    'l_name': '',
    'address': '1',
    'city': '1',
    'zip_code': '19712'
}


class CheckoutPage(BasePage):
    url = 'https://checkout.shopify.com/'
    product_image = Find(by=By.CSS_SELECTOR, value='.product img')
    product_price = Find(by=By.CSS_SELECTOR, value='.payment-due__price')

    f_name = Find(by=By.CSS_SELECTOR, value='#checkout_billing_address_first_name')
    l_name = Find(by=By.CSS_SELECTOR, value='#checkout_billing_address_last_name')
    address = Find(by=By.CSS_SELECTOR, value='#checkout_billing_address_address1')
    city = Find(by=By.CSS_SELECTOR, value='#checkout_billing_address_city')
    zip_code = Find(by=By.CSS_SELECTOR, value='#checkout_billing_address_zip')
    country = Find(by=By.XPATH, value='//option[.="United States"]')
    state = Find(by=By.XPATH, value='//option[.="Delaware"]')

    to_next_step_btn = Find(by=By.XPATH, value='//button[contains(@class, "continue")]')

    def get_product_name(self):
        return self.product_image.get_attribute('alt')

    def fill_billing_address_form(self, customer_info=None):
        for k, v in BILLING_INFO.items():
            getattr(self, k).clear()
            if not v:
                v = customer_info.get(k)
            getattr(self, k).send_keys(v)

        self.country.click()
        self.state.click()
