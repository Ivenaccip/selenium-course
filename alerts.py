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
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        time.sleep(5)

    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

        driver.find_element(By.CLASS_NAME, "link-compare").click()
        driver.find_element(By.LINK_TEXT, "Clear All").click()#Nos va a permitir identificar algo por su texto

        alert = driver.switch_to.alert#Actualizado
        alert_text = alert.text

        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        alert.accept()#Da en el boton aceptar

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)