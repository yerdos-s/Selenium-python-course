from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions import alert_text,calc


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    price = WebDriverWait(browser,15).until(
        EC.text_to_be_present_in_element((By.ID,'price'),'$100')
    )
    browser.find_element(By.ID,'book').click()
    
    x = browser.find_element(By.ID,'input_value').text
    form = browser.find_element(By.CSS_SELECTOR,'input[name="text"]')

    form.send_keys(calc(x))
    browser.find_element(By.ID,'solve').click()

    print(alert_text(browser))

finally:
    browser.quit()

