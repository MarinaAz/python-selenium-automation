from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")
NAV_TOOLS = (By.ID, 'nav-tools')
ORDER_LNK = (By.ID, 'nav-orders')


@when('Click Amazon Orders link')
def click_orders_link(context):
    context.app.sign_in_page.click_orders_link()
    # context.driver.find_element(*ORDER_LNK).click()


@when('Click Sign In from popup')
def click_sign_in_popup_btm(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN))
    e.click()


@then('Verify Sign In page is opens')
def verify_sign_in_page_opens(context):
    context.app.sign_in_page.verify_sign_in_page_opens()
    # context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin')), f'Url {context.driver.current_url} does not include https://www.amazon.com/ap/signin'


@then('Verify sign in is clickable')
def verify_sign_in_is_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN))


@then('Verify sign in is disappears')
def verify_sign_in_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN_POPUP_BTN))
    context.driver.find_elements(*NAV_TOOLS)


@when('Wait for {sec} seconds')
def sleep_sec(context, sec):
    sleep(int(sec))

