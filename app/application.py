from pages.main_page import MainPage
from pages.search_results_page import SearchResultPage
from pages.cart_empty import CartEmpty
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultPage(self.driver)
        self.cart_empty = CartEmpty(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        # self.result_page = MainPage(self.driver)