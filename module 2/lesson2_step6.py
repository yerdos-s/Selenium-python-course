from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.select import Select

link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    number = browser.find_element(By.ID,'input_value')
    y = calc(number.text)
    form = browser.find_element(By.ID,'answer')
    browser.execute_script("arguments[0].scrollIntoView(true)", form)
    form.send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()


finally:
    time.sleep(10)
    browser.quit()
