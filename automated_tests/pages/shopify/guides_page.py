from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webium import BasePage, Find


class GuidesPage(BasePage):
    url = 'http://block-six-analytics.myshopify.com/collections/guides'

    guides_menu = Find(by=By.CSS_SELECTOR, value='a[href*="guides"] span.dd')

    def choose_guide(self, item_name):
        item_name = item_name.replace('mbaMission ', '').replace(' ', '-').replace('\'', '-').lower()
        item = Find(by=By.CSS_SELECTOR, value='.sub-menu a[href*="{}"]'.format(item_name), context=self)
        ActionChains(self._driver).move_to_element(self.guides_menu).click(item).perform()
        return GuidesSubPage()


class GuidesSubPage(BasePage):
    def get_item(self, item_name):
        item = Find(by=By.XPATH, value='//h3[contains(., "{}")]/..//a'.format(item_name), context=self)
        item.click()
        return GuideItemPage()


class GuideItemPage(BasePage):
    def get_guide_price(self):
        return Find(by=By.CSS_SELECTOR, value='.product-price', context=self).text

    def add_guide(self):
        count = self.items_in_cart()
        Find(by=By.CSS_SELECTOR, value='.add-to-cart', context=self).click()

        if not self.item_is_sold_out():
            wait = WebDriverWait(self._driver, 10)
            wait.until(lambda x: count < self.items_in_cart())

    def items_in_cart(self):
        return int(self._driver.execute_script('return $(".count").text()'))

    def item_is_sold_out(self):
        return self._driver.execute_script('return $(".add-to-cart").attr("value")') == 'Sold Out'
