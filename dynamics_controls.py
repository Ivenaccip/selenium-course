from encodings import search_function
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class dynamics_controls(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/disappearing_elements")
        driver.maximize_window()
        time.sleep(5)

    def dynamics_controls(self):
        driver = self.driver

        #El selector de CSS es usado cuando no tenemos mucha información
        checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox > input[type=checkbox]")
        checkbox.click()

        remove_add_button = driver.find_element(By.CSS_SELECTOR, "#checkbox-example > button")
        remove_add_button.click()

        WebDriverWait(driver, timeout = 15).until(EC.element_to_be_clickable(By.CSS_SELECTOR, "#checkbox-example > button"))
        remove_add_button.click

        enable_disable_button = driver.find_element(By.CSS_SELECTOR, "#input-example > button")
        enable_disable_button.click()

        WebDriverWait(driver, timeout = 15).until(EC.element_to_be_clickable(By.CSS_SELECTOR, "#input-example > button"))

        text_area = driver.find_element(By.CSS_SELECTOR, "#input-example > input[type=text]")
        text_area.send_keys('Platzi')

        enable_disable_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)