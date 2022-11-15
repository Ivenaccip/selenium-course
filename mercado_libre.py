from encodings import search_function
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from google_page import GooglePage
import time

class TestingMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("https://www.mercadolibre.com")
        driver.maximize_window()
        time.sleep(5)

    def test_search_ps4(self):
        driver = self.driver
        country = driver.find_element(By.ID, 'CO')
        country.click()
        accept_cookie_button = driver.find_element(
            By.XPATH, '/html/body/div[2]/div[1]/div[2]/button[1]')
        accept_cookie_button.click()
        time.sleep(2)
        search_input = driver.find_element(By.NAME, 'as_word')
        search_input.click()
        search_input.clear()
        search_input.send_keys('playstation 4')
        search_input.submit()
        time.sleep(2)
        location = driver.find_element(By.PARTIAL_LINK_TEXT, 'Bogotá D.C.')
        location.click()
        time.sleep(2)
        condition = driver.find_element(By.PARTIAL_LINK_TEXT, 'Nuevo')
        condition.click()
        time.sleep(2)
        order_menu = driver.find_element(
            By.CLASS_NAME, 'andes-dropdown__trigger')
        order_menu.click()
        higher_price = driver.find_element(
            By.CSS_SELECTOR, '#andes-dropdown-más-relevantes-list-option-price_desc')
        higher_price.click()

        article_elements = driver.find_elements(
            By.CSS_SELECTOR, 'div.ui-search-result__content-wrapper h2.ui-search-item__title')
        price_elements = driver.find_elements(
            By.CSS_SELECTOR, 'div.ui-search-result__content-wrapper div.ui-search-price--size-medium div.ui-search-price__second-line span.price-tag-fraction')
        item_count = len(article_elements)
        data = [{'article': article_elements[i].text, 'price': price_elements[i].text}
                for i in range(item_count)]
        print(f'\nFound {item_count} items.')
        print('\nData: ', data)



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)