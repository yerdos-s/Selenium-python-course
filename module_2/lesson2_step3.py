from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(num1,num2):
    x = int(num1)+int(num2)
    return str(x) #Возвращает строковое значение числа

try:
    first_number = browser.find_element(By.ID,'num1')
    num1 = first_number.text
    second_number = browser.find_element(By.ID,'num2')
    num2 = second_number.text

    sum = calc(num1,num2)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_visible_text(sum)

    browser.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
finally:
    time.sleep(10)
    browser.quit()
