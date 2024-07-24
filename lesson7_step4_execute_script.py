from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math


link = "https://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x=browser.find_element(By.ID, "input_value")
    x = x.text
    y = calc(int(x))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла