from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

APP_LINK_BTN = (By.CSS_SELECTOR, "a[href*='/gp/feature.html?docId=1000625601']")
AMZ_APP_ING = (By.CSS_SELECTOR, "img[src*='https://images-na.ssl-images-amazon.com/images/G/01/red-cs/MM/landingpage/01a_desktop_HeaderImage_NOIC']")


@given('Open Amazon T&C page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
    sleep(2)


@when('Store original windows')
def store_windows(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)
    sleep(2)


@then('Click on Amazon applications link')
def click_on_amazon_link(context):
    context.driver.find_element(*APP_LINK_BTN).click()
    sleep(2)


@then('Switch to the newly opened window')
def switch_to_newly_window(context):
    context.driver.wait_until(EC.new_window_is_opened)
    print(context.driver.window_handles)
    context.driver.switch_to.window(context.driver.window_handles[1])
    sleep(2)


@then('Amazon app page is opened')
def amazon_app_page_is_opened(context):
    context.driver.find_element(*AMZ_APP_ING).click()
    sleep(2)



