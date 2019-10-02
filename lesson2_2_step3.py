from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time
import math

link = "http://suninjuly.github.io/selects2.html"

def calc(num1,num2):
    return str(int(num1) + int(num2))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text

    y = calc(num1, num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y))  # ищем элемент

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
