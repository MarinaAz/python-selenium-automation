from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartEmpty(Page):
    CART_BTN = (By.ID, 'nav-cart')
    ERR_MSG = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2")

    def click_cart_icon(self):
        self.click(*self.CART_BTN)

    def cart_page_appears(self):
        self.verify_text(*self.ERR_MSG)


