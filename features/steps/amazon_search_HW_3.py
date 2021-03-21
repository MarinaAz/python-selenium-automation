from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Customer Service button')
def click_customer_service(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='=nav_cs_customerservice_74bebff5eab64735882e87c98f865eb7']").click()


@when('Input Cancel Order into Search the help library')
def input_search_the_help(context):
    search_field = context.driver.find_element(By.ID, 'helpsearch')
    search_field.send_keys('cancel order')


@then('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(By.XPATH,  "//i[@class='a-icon a-icon-search']").click()


@then('Help & Customer Service Page is appears on Amazon')
def verify_search_result(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    expected_text = "Cancel Items or Orders"
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


@then('Page URL has Cancel Order in it')
def verify_url_contains_query(context):
    assert 'Cancel Items or Orders' in context.driver.current_url, f'Cancel Items or Orders not in {context.driver.current_url}'




