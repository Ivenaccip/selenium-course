from encodings import search_function
from time import sleep
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException # Sirve como excepción en presencia de un elemento

class AssertionTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, "select-language"))

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__ == "__main__":
    unittest.main(verbosity=2)