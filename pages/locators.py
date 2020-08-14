from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class MainPageLocators():
    pass

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    CONFIRM_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in strong")
    CONFIRM_MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in strong")
