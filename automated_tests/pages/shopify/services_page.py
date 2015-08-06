from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webium import BasePage, Find


class ServicesPage(BasePage):
    url = 'http://block-six-analytics.myshopify.com/collections/services'

    def get_item(self, item_name):
        item_name = item_name.replace(' ', '-').replace('/', '-').lower()
        item = Find(by=By.CSS_SELECTOR, value='section > a[href*="{}"]'.format(item_name), context=self)
        item.click()
        return ServiceItemPage()


class ServiceItemPage(BasePage):
    def add_package(self, package_name):
        package = Find(by=By.XPATH, value='//td[contains(., "{}")]/a'.format(package_name), context=self)
        package.click()
        return package.get_attribute('data-id')

    def get_package_price(self, package_name):
        td = Find(by=By.XPATH, value='//td[contains(., "{}")]'.format(package_name), context=self)
        return td.text.split(':')[-1].replace('$', '$ ').strip() + '.00'

    def remove_tag(self, tag_name):
        self._driver.execute_script('$("{}").remove()'.format(tag_name))

    def get_option(self, select_name, option_value):
        option_xpath = '//label[.="{}"]/..//select/option[contains(@value,"{}")]'.format(select_name, option_value)
        option = Find(by=By.XPATH, value=option_xpath, context=self)
        return option

    def choose_duration(self, duration):
        option = self.get_option('Duration', duration)
        option.click()

    def choose_class_date(self, class_date):
        option = self.get_option('Class Date', class_date)
        option.click()
        return option.get_attribute('value')

    def choose_interview(self, interview):
        option = self.get_option('Type of interview', interview)
        option.click()

    def choose_option(self, option):
        option = Find(by=By.XPATH, value='//option[.="{}"]'.format(option), context=self)
        option.click()

    def get_service_price(self):
        return Find(by=By.CSS_SELECTOR, value='.product-price', context=self).text

    def add_service(self):
        count = self.items_in_cart()
        Find(by=By.CSS_SELECTOR, value='.add-to-cart', context=self).click()

        if not self.item_is_sold_out():
            wait = WebDriverWait(self._driver, 10)
            wait.until(lambda x: count < self.items_in_cart())

    def items_in_cart(self):
        return int(self._driver.execute_script('return $(".count").text()'))

    def item_is_sold_out(self):
        return self._driver.execute_script('return $(".add-to-cart").attr("value")') == 'Sold Out'
