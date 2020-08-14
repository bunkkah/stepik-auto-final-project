from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def guest_can_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def product_should_be_in_basket(self):
        actual_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_product_name = self.browser.find_element(*ProductPageLocators.CONFIRM_MESSAGE_PRODUCT_NAME).text
        assert actual_product_name == basket_product_name, "Product name is not correct"

    def price_should_be_equal(self):
        actual_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_product_price = self.browser.find_element(*ProductPageLocators.CONFIRM_MESSAGE_PRODUCT_PRICE).text
        assert actual_product_price == basket_product_price, "Product price is not correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.CONFIRM_MESSAGE_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.CONFIRM_MESSAGE_PRODUCT_NAME), \
            "Success message does not disappear as it should"

