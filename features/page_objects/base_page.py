from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class BasePage():
    def __init__(self, url, driver):
        self.url = url
        self.web_driver = driver
        self.maximize_window()

    def maximize_window(self):
        try:
            self.web_driver.maximize_window()
        except:
            print("maximize_window() not available on this device")

    def wait(self, locator, timeout=10):
        wait = WebDriverWait(self.web_driver, timeout)
        wait.until(EC.visibility_of_element_located(locator))

    def wait_and_find_elements(self, locator):
        self.wait(locator)
        return self.web_driver.find_elements(*locator)

    def find_and_send_keys(self, locator, value):
        self.wait(locator)
        self.web_driver.find_element(*locator).send_keys(value)

    def find_and_click(self, locator):
        self.wait(locator)
        self.web_driver.find_element(*locator).click()

    def get_text(self, locator):
        self.wait(locator)
        return self.web_driver.find_element(*locator).text

    def select_by_value(self, locator, value):
        select = Select(self.web_driver.find_element(*locator))
        select.select_by_value(value)

    def select_by_text(self, locator, text):
        select = Select(self.web_driver.find_element(*locator))
        select.select_by_visible_text(text)
