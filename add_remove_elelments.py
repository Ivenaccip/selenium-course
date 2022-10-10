from encodings import search_function
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class register_user(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
        driver.maximize_window()
        time.sleep(5)

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add?: '))
        elements_remove = int(input('How many elements will you remove?: '))
        total_elements = elements_added - elements_remove

        add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')

        time.sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_remove):
            try:
                delete_button = driver.find_element(By.XPATH, '//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print("You're trying to delete more elements than existent")
                break

        if total_elements > 0:
            print(f"There are {total_elements} elements on screen")
        else:
            print("There 0 are elements on screen")

        time.sleep(3)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)