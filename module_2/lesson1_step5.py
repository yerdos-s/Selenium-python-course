from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, 'label .nowrap:nth-child(2)')
    x = x_element.text
    y = calc(x)

    form = browser.find_element(By.CLASS_NAME, 'form-control')
    form.send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.ID,'robotsRule')
    radiobutton.click()

    submit = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()

