from encodings import search_function
from sqlite3 import DateFromTicks
from time import sleep
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

class otro(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("https://pubs.rsc.org/en/journals/journalissues/js#!issueid=js1862_15_0&type=archive&issnprint=0368-1769")

    def test_modular(self):
        driver = self.driver
        self.assertTrue(self.is_element_present(By.XPATH, '//*[@id="tabissues"]/div[2]'))
        self.assertTrue(self.is_element_present(By.CLASS_NAME, 'capsule capsule--article '))

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity=2)