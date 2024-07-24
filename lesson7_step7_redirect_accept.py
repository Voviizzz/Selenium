from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "https://suninjuly.github.io/redirect_accept.html"

try:


    browser = webdriver.Chrome()
    browser.get(link)

   
    first_window = browser.window_handles[0]
    
    button = browser.find_element(By.CSS_SELECTOR, ".trollface")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(int(x))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла