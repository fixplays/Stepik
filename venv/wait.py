from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return math.log(abs(12*math.sin(int(x))))

def test_wait():
    browser = WebDriver(executable_path = 'C://chromedriver_win32//chromedriver.exe')
    browser.implicitly_wait(5)
# говорим WebDriver искать каждый элемент в течение 5 секунд
#browser.implicitly_wait(13)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book = browser.find_element_by_id('book').click()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    print(y)
    z = str(y)
    answ_field = browser.find_element_by_id('answer').send_keys(z)
    submit = browser.find_element_by_css_selector('body > form > div > div > button').click()
    time.sleep(7)
#
