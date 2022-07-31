from selenium import webdriver
from selenium.webdriver.common.by import By
import os

current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

print(f'this is a path: \n{file_path}')


print(os.getcwd()) # можно и так получить путь к директории текущего исполняемого файла