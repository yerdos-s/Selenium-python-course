from selenium import webdriver
from selenium.webdriver.common.by import By
link = 'http://selenium1py.pythonanywhere.com/'

class TestMainPage1():

    @classmethod
    def setup_class(self):
        print('\nStart browser for test suite1...')
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print('\nQuit browser for test suite1...')
        self.browser.quit()

    def test_guest_should_see_login(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR,'#login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR,".basket-mini .btn-group > a")

class TestMainPage2():

    def setup_method(self):
        print('\nStart browser for test suite2...')
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print('\nQuit browser for test suite2...')
        self.browser.quit()

    def test_guest_should_see_login(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR,
                                  ".basket-mini .btn-group > a")
