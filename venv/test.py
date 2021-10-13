from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import math

def calc(x):
    return math.log(abs(12*math.sin(int(x))))

def test():
    driver = WebDriver(executable_path = 'C://chromedriver_win32//chromedriver.exe')
    driver.get('http://suninjuly.github.io/redirect_accept.html')

    button_click = driver.find_element_by_xpath('/html/body/form/div/div/button').click()
    time.sleep(1)
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    x_element = driver.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    print(y)
    z = str(y)
    answ_field = driver.find_element_by_id('answer').send_keys(z)
    submit = driver.find_element_by_css_selector('body > form > div > div > button').click()
    time.sleep(7)
