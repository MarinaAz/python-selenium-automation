from behave import given, then
from selenium.webdriver.common.by import By

TOP_LINKS = (By.CSS_SELECTOR, 'div#zg_tabs li')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text_wrapper')


@given('Open Amazon bestsellers')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers')


@then('Verify there are {expected_links} links')
def verify_links_count(context, expected_links):
    actual_links = context.driver.find_element(*TOP_LINKS)
    assert len(actual_links) == int(expected_links), f'Expected {expected_links} but get {actual_links}'

