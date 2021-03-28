from selenium.webdriver.support.wait import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver
        # self.base_url = 'https://www.amazon.com/'

    def click(self, *locator):
        self.driver.find_element(*locator).click()
        self.driver.wait = WebDriverWait(self.driver, 10)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_url(self, url):
        self.driver.get(url)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_url_contains_query(self, query):
        assert query in self.driver.current_url, f'Watches not in {context.driver.current_url}'
