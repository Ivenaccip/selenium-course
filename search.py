from encodings import search_function
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class HelloWorld(unittest.TestCase):
    
    def setUp(self): #Inicio de la prueba
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_search_text_field(self):
        search_field = self.driver.find_element(By.ID, "search")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element(By.NAME, "q")

    def test_search_text_field_class_name(self):
        search_field = self.driver.find_element(By.CLASS_NAME, "input-text")

    def test_search_button_enable(self):
        button = self.driver.find_element(By.CLASS_NAME, "button")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element(By.CLASS_NAME, "promos")
        banners = banner_list.find_elements(By.TAG_NAME, 'img') #tienes que considerar la s en elements
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        vip_promo = self.driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element(By.CSS_SELECTOR, "div.header-minicart span.icon")

    def tearDown(self): #Final de la prueba
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)