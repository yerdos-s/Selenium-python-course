import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test(unittest.TestCase):
    def test_registration1(self):
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
        self.assertEqual(welcome_text,'Congratulations! You have successfully registered!', \
                             'the text does not match')

    def test_registration2(self):
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
        self.assertEqual(welcome_text,'Congratulations! You have successfully registered!', \
                             'the text does not match')
if __name__ == '__main__':
    unittest.main()