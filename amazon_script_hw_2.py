from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/Users/marinaazizbajeva/python-selenium-automation/chromedriver 2')

driver.implicitly_wait(4)

driver.get('https://www.amazon.com/gp/help/customer/display.html')

search_field = driver.find_element(By.ID, 'helpsearch')
search_field.send_keys('Cancel Order', Keys.ENTER)

actual_text = driver.find_element(By.XPATH, "//b['cancel order']").text
expected_text = '"Cancel Order"'

assert 'Cancel Order' == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()






