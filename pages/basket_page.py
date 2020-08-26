from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Products should not be presented in basket, but it is"

    def should_be_text_in_empty_basket(self):
        basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert basket_text == "Your basket is empty. Continue shopping", \
            "Should be specific text if basket is empty, but there is not"
