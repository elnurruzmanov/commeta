from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--no-sandbox")  


service = Service('/path/to/chromedriver')  
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://id.commeta.uz/login")

    email_input = driver.find_element(By.NAME, "email")  
    number_input = driver.find_element(By.NAME, "number")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")  


    email_input.clear()
    number_input.clear()
    login_button.click()

    
    time.sleep(3)

    
    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message") 
    assert "Пожалуйста, заполните это поле" in error_message.text

    print("Тест пройден: Поля обязательны для заполнения.")
    
except AssertionError:
    print("Ошибка: Поля не являются обязательными для заполнения.")
    
finally:
    driver.quit()



