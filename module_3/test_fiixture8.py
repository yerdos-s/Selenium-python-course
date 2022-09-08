import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

class Test:
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, "#login_link")
    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

