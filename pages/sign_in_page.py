from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    ORDER_LNK = (By.ID, 'nav-orders')

    def click_orders_link(self):
        self.click(*self.ORDER_LNK)

    def verify_sign_in_page_opens(self):
        self.open_url('https://www.amazon.com/ap/signin')
