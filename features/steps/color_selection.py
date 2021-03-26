from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

COLOR_OPTION = (By.CSS_SELECTOR, '#variation_color_name li')
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
SIZE_SELECTION_BTN = (By.ID, 'dropdown_selected_size_name')
SIZE_OPTION_0 = (By.ID, 'size_name_0')
SELECTED_COLOR = (By.ID, 'color_name_5')
CART = (By.ID, 'nav-cart-count')


@given('Open Amazon page of product B07BJKRR25')
def open_amazon_product_page(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')


@when('Verify user can click through colors')
def verify_can_select_colors(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Vintage', 'Dark Wash', 'Indigo Wash', 'Light Vintage', \
                       'Light Wash', 'Medium Vintage', 'Medium Wash', 'Rinse', 'Rinsed Vintage', 'Vintage Light Wash', \
                       'Washed Black']
    colors = context.driver.find_elements(*COLOR_OPTION)

    for i in range(len(colors)):
        colors[i].click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        assert expected_colors[5] == selected_color
        sleep(2)


@then('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


# @then('Click on Add to cart button')
# def click_add_to_cart(context):
#     context.driver.find_element(*ADD_TO_CART_BTN).click()
#     if len(context.driver.find_elements(*SIZE_TOOLTIP)) == 1:
#         context.driver.find_element(*SIZE_SELECTION_BTN).click()
#         context.driver.find_element(*SIZE_OPTION_0).click()
#         sleep(2)
#         context.driver.find_element(*ADD_TO_CART_BTN).click()


@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    cart_count = context.driver.find_element(*CART).text
    assert expected_count == cart_count, f'Expected {expected_count} items but has {cart_count}'





