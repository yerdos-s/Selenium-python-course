from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    treasure = browser.find_element(By.XPATH,'//h2/img')
    value_x = treasure.get_attribute('valuex')
    form = browser.find_element(By.ID,'answer')
    solution = calc(value_x)
    form.send_keys(solution)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()

    submit = browser.find_element(By.XPATH, "//button[@type='submit']") #Или можно button[type="submit"] - CSS selector
    submit.click()
finally:
    time.sleep(5)
    browser.quit()