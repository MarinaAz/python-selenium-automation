from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Cart Icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart').click()


@when('Cart page is appears on Amazon')
def verify_search_result(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
    expected_text = 'Your Amazon Cart is empty'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


@then('Page URL has Your Amazon Cart is empty in it')
def verify_url_contains_query(context):
    assert 'Your Amazon Cart is empty' in context.driver.current_url, f'Your Amazon Cart is empty not in {context.driver.current_url}'




