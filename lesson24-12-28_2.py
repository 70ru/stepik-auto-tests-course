from selenium import webdriver
from math import log, sin
import time


link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element_by_css_selector("button.btn-primary")
    button1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)
    x = int(browser.find_element_by_id("input_value").text)
    result = log(abs(12*sin(x)))
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(result)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # firstname.send_keys("ГАЛА")
    # lastname = browser.find_element_by_name("lastname")
    # lastname.send_keys("Ублюдова")
    # email = browser.find_element_by_name("email")
    # email.send_keys("70ru@mail.ru")
    # file = browser.find_element_by_id("file")
    # current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    # file_path = os.path.join(current_dir, 'MANUAL Python.txt')           # добавляем к этому пути имя файла 
    # file.send_keys(file_path)
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()


   
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()