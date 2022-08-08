import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_registration1():
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        first_name = browser.find_element(By.CSS_SELECTOR,
                                          'input:required.form-control.first')
        first_name.send_keys('Elon')
        last_name = browser.find_element(By.CSS_SELECTOR,
                                         'input:required.form-control.second')
        last_name.send_keys('Musk')
        email = browser.find_element(By.CSS_SELECTOR,
                                     'input:required.form-control.third')
        email.send_keys('Musk@spacex.com')
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert welcome_text == 'Congratulations! You have successfully registered!', \
            'the text does not match'
    finally:
        browser.quit()

def test_registration2():
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        first_name = browser.find_element(By.CSS_SELECTOR,
                                          'input:required.form-control.first')
        first_name.send_keys('Elon')
        last_name = browser.find_element(By.CSS_SELECTOR,
                                         'input:required.form-control.second')
        last_name.send_keys('Musk')
        email = browser.find_element(By.CSS_SELECTOR,
                                     'input:required.form-control.third')
        email.send_keys('Musk@spacex.com')
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert welcome_text == 'Congratulations! You have successfully registered!', \
            'the text does not match'
    finally:
        browser.quit()


if __name__ == '__main__':
    pytest.main()
