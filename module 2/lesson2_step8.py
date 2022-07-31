from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = 'http://suninjuly.github.io/file_input.html'
browser =  webdriver.Chrome()
browser.get(link)

try:
    firstname = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    firstname.send_keys('Elon')
    last_name = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    last_name.send_keys('Musk')
    email= browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email.send_keys('email@email.com')

    attachment = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')

    #Создаем любой файл для того чтобы прикрепить его:
    with open('file.txt', 'w') as file:
        file.write('any text')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir,'file.txt')  # добавляем к этому пути имя файла

    attachment.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()

    os.remove(file_path) #Удаляем наш файл. Можно и не удалять
finally:
    time.sleep(5)
    browser.quit()