from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(executable_path='/Users/marinaazizbajeva/python-selenium-automation/chromedriver 2')

# driver.implicitly_wait(4)

driver.get('https://www.amazon.com/')

search_field = driver.find_element(By.ID, 'twotabsearchtextbox')
search_field.send_keys('Watches')

driver.wait = WebDriverWait(driver, 10)
e = driver.wait.until(EC.element_to_be_clickable((By.ID, 'nav-search-submit-button')))

e.click()

actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
expected_text = '"Watches"'

assert '"Watches"' == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()