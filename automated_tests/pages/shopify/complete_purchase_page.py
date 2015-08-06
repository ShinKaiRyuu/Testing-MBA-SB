from selenium.webdriver.common.by import By
from webium import BasePage, Find

PAYMENT_INFO = {
    'credit_card_number': '4242424242424242',
    'ccv': '321',
    'name_on_card': 'Some Name',
    'card_expiry': '0118'
}

PURCHASE_COMPLETED = 'Thank you for your purchase!'


class CompletePurchasePage(BasePage):
    url = 'https://checkout.shopify.com/'
    credit_card_number = Find(by=By.CSS_SELECTOR, value='#checkout_credit_card_number')
    name_on_card = Find(by=By.ID, value='checkout_credit_card_name')
    card_expiry = Find(by=By.ID, value='checkout_credit_card_expiry')
    ccv = Find(by=By.CSS_SELECTOR, value='#checkout_credit_card_verification_value')

    complete_btn = Find(by=By.XPATH, value='//button[contains(., "Complete order")]')

    def fill_payment_info(self):
        for k, v in PAYMENT_INFO.items():
            getattr(self, k).clear()
            getattr(self, k).send_keys(v)

    def purchase_completed(self):
        section_title = Find(by=By.CSS_SELECTOR, value='.section__title', context=self)
        return section_title.text.strip() == PURCHASE_COMPLETED
