from encodings import search_function
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class CompareProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://google.com")
        driver.maximize_window()
        time.sleep(5)

    def test_browser_navegation(self):
        driver = self.driver

        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        driver.back()
        time.sleep(1)
        driver.forward()
        driver.refresh()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)