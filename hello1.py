import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#try:
browser = webdriver.Firefox(executable_path=r"C:\WebDrivers\geckodriver\geckodriver.exe")
browser.implicitly_wait(5)
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

pric = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element ((By.ID, "price"), "$100")
    )
button_pric = browser.find_element_by_tag_name('button').click()
def calc(x):
    return str(math.log(abs(12*math.sin(int(x))))) 

element = browser.find_element_by_id("input_value")
x = element.text
y = calc(x)
input0 = browser.find_element_by_id("answer")
input0.send_keys(y)
button_click = browser.find_element_by_id("solve").click()
#finally:
time.sleep(30)
browser.quit()
