from encodings import search_function
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class typos(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/typos")
        driver.maximize_window()
        time.sleep(5)

    def test_find_typos(self):
        driver = self.driver

        paragraph_to_check = driver.find_element(By.CSS_SELECTOR, "#content > div > p:nth-child(3)")
        text_to_check = paragraph_to_check.text
        print(text_to_check)

        tries = 1
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element(By.CSS_SELECTOR, "#content > div > p:nth-child(3)")
            paragraph_to_check = driver.find_element(By.CSS_SELECTOR, "#content > div > p:nth-child(3)")
            text_to_check = paragraph_to_check.text
            driver.refresh()
            tries += 1

        print(f"Tardo {tries} intentos")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)