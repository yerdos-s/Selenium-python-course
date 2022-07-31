from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('http://suninjuly.github.io/cats.html')

try:
    browser.find_element(By.ID, 'button')
finally:
    browser.quit()