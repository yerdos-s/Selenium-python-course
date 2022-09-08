import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nquit browser..")
    driver.quit()
