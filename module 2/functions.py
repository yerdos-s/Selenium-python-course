import math
from selenium import webdriver

class Webdriver:
    def __init__(self,browser):
        self.browser = browser

    def set_chrome(self):
        self.browser = webdriver.Chrome()

def calc(x) -> float:
    return str(math.log(abs(12 * math.sin(int(x)))))

def alert_text(browser):
    answer = browser.switch_to.alert.text.split()  # метод сплит разделяет строку на множество и сохраняет в массив
    return answer[-1]