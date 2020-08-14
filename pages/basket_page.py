from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_not_contain_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Product is in basket, but should not be"

    def should_be_text_in_empty_basket(self):
        basket_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        assert basket_text == "Your basket is empty. Continue shopping", \
            "Text in empty basket is missing"
