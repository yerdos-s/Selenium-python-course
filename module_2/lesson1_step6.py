from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/math.html')

try:
    people_radio = browser.find_element(By.ID, 'peopleRule')
    #Найдём атрибут "checked" с помощью встроенного метода get_attribute
    #и проверим его значение:
    people_checked = people_radio.get_attribute('checked')
    print('value of people radio:' ,people_checked )
    assert people_checked is not None ,'People radio is not selected by default'
finally:
    browser.quit()