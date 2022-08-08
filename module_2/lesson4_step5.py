from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('http://suninjuly.github.io/wait1.html')

try:
    browser.find_element(By.ID, 'verify').click()
    message = browser.find_element(By.ID, 'verify_message')
    assert 'Verification was successful!' in message.text, 'error'

finally:
    browser.quit()
