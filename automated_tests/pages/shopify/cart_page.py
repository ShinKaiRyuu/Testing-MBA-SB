from selenium.webdriver.common.by import By
from webium import BasePage, Find
from webium.controls.select import Select


class CartPage(BasePage):
    url = 'http://block-six-analytics.myshopify.com/cart'

    consultant_field = Find(by=By.CSS_SELECTOR, value='#consultant_field')
    free_consultant_field = Find(by=By.CSS_SELECTOR, value='#free_consultant_field')
    update_btn = Find(by=By.CSS_SELECTOR, value='#update')
    checkout_btn = Find(by=By.CSS_SELECTOR, value='#checkout')

    def get_cart_item(self, data_id=None):
        item_selector = '.cartItem' if not data_id else '.cartItem[data-id="{}"]'.format(data_id)
        cart_item = Find(by=By.CSS_SELECTOR, value=item_selector, context=self)
        cart_item_text = (cart_item.text.encode('utf-8')
                          .replace(b'\xe2\x80\x9c', b'')
                          .replace(b'\xe2\x80\x9d', b'')
                          .replace(b'\xe2\x80\x99', b'')
                          )
        return cart_item_text.decode('utf-8').strip().replace('/', ' ')

    def consultants_selects_on_page(self):
        return self.consultant_field.is_displayed() and self.free_consultant_field.is_displayed()

    def cart_is_empty(self):
        return self._driver.execute_script('return $("#cart h3").text()') == 'Your cart is currently empty.'

    def remove_product(self, item_name):
        delete_btn = Find(by=By.XPATH, value='//tr[contains(., "{}")]//a'.format(item_name), context=self)
        delete_btn.click()

    def set_consultant(self, name, free=False):
        select_id = 'consultant_field' if not free else 'free_consultant_field'
        Find(by=By.XPATH, value='//select[@id="{}"]/option[.="{}"]'.format(select_id, name), context=self).click()

    def get_consultant(self, free=False):
        select_id = 'consultant_field' if not free else 'free_consultant_field'
        s = Find(Select, by=By.ID, value=select_id, context=self)
        return s.get_text_selected()

    def no_update_checkout_btns(self):
        return self._driver.execute_script('return $("#update").length + $("#checkout").length') == 0
