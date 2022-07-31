from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/wait1.html')

try:
    time.sleep(2)
    browser.find_element(By.ID, 'verify').click()
    message = browser.find_element(By.ID, 'verify_message')
    assert message.text == 'Verification was successful!', 'error'
finally:
    browser.quit()
