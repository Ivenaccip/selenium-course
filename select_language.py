from encodings import search_function
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select #Este modulo es para barras despegables
import time

class select_language(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        time.sleep(5)

    def test_select_language(self):
        exp_options = ['English', 'French', 'German']
        act_options = []

        select_language = Select(self.driver.find_element(By.ID, 'select-language'))

        self.assertEqual(3, len(select_language.options))#select_laguage.options accede a las opciones

        for option in select_language.options:
            act_options.append(option.text)

        self.assertListEqual(exp_options, act_options)

        self.assertEqual('English', select_language.first_selected_option.text)

        select_language.select_by_visible_text('German')

        self.assertTrue('store=german' in self.driver.current_url) #Estamos verificando que cambio en el jquery del url

        select_language = Select(self.driver.find_element(By.ID, 'select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)