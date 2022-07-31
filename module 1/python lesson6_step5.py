from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_link_text')

    link_value = str(math.ceil(math.pow(math.pi, math.e)*10000))
    input1 = browser.find_element(By.LINK_TEXT, link_value)
    input1.click()
    input2 = browser.find_element(By.TAG_NAME, 'input')
    input2.send_keys("Ivan")
    input3 = browser.find_element(By.NAME, 'last_name')
    input3.send_keys("Petrov")
    input4 = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input4.send_keys("Smolensk")
    input5 = browser.find_element(By.ID, "country")
    input5.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()