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
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        time.sleep(5)

    def test_user(self):
        driver = self.driver
        driver.find_element(By.XPATH, '/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element(By.LINK_TEXT, 'Log In').click()

        #Estamos buscando un botón por xpath y luego verificando que exista y se despliegue para hacer click
        create_ccount_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div/div[1]/div[2]/a')
        self.assertTrue(create_ccount_button.is_displayed() and create_ccount_button.is_enabled())
        create_ccount_button.click()

        #Vamos a comprobar que sea el mismo nombre
        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element(By.ID, 'firstname')
        middle_name = driver.find_element(By.ID, 'middlename')
        last_name = driver.find_element(By.ID, 'lastname')
        email_address = driver.find_element(By.ID, 'email_address')
        password = driver.find_element(By.ID, 'password')
        confirm_password = driver.find_element(By.ID, 'confirmation')
        newsletter_sub = driver.find_element(By.ID, 'is_subscribed')
        submit_button = driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled 
        and middle_name.is_enabled
        and last_name.is_enabled
        and email_address.is_enabled
        and password.is_enabled
        and confirm_password.is_enabled
        and newsletter_sub.is_enabled
        and submit_button.is_enabled)

        first_name.send_keys('Test')
        middle_name.send_keys('Test')
        last_name.send_keys('Test')
        email_address.send_keys('Test@gmail.com')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        submit_button.click()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)