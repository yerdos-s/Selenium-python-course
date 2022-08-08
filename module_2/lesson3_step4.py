from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.select import Select

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element(By.ID,'input_value').text
    y = calc(x)
    form = browser.find_element(By.CSS_SELECTOR, 'input[name="text"]')
    form.send_keys(y)
    browser.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
finally:
    time.sleep(10)
    browser.quit()