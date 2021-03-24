from behave import given, when, then
from selenium.webdriver.common.by import By


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']')")
PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')
SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
SIZE_SELECTION_BTN = (By.ID, 'dropdown_selected_size_name')
SIZE_OPTION_0 = (By.ID, 'size_name_0')
COLOR_OPTION_0 = (By.ID, 'color_name_0')
COLOR_SELECTION_BTN = (By.ID, 'variation_color_name')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    if len(context.driver.find_elements(*SIZE_TOOLTIP)) == 1:
        context.driver.find_element(*COLOR_SELECTION_BTN).click()
        context.driver.find_element(*COLOR_OPTION_0).click()
        context.driver.find_element(*ADD_TO_CART_BTN).click()
