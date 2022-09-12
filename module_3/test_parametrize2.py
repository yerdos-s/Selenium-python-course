import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.mark.parametrize('endpoint', \
                         ['236895', '236896', '236897', '236898', '236899',
                          '236903', '236904', '236905'])
class Test_website():
    def test_website(self, browser, endpoint):
        answer = str(math.log(int(time.time() + 0.092)))
        link = f'https://stepik.org/lesson/{endpoint}/step/1'
        browser.get(link)
        # говорим Selenium проверять в течение 10 секунд, пока кнопка не станет кликабельной
        textarea = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.textarea')))
        textarea.send_keys(answer)
        browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
        hint = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '.smart-hints.ember-view.lesson__hint'))).text
        assert hint == 'Correct!', 'Hint is displaying wrong values!'
