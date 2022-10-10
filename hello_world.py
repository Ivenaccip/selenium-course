import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class HelloWorld(unittest.TestCase):
    
    def setUp(self): #Inicio de la prueba
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

    def test_hello_world(self): #Acciones de la prueba
        driver = self.driver
        driver.get("http://www.platzi.com")

    def test_visit_wikipedia(self):
        self.driver.get("https://wikipedia.org")

    def tearDown(self): #Final de la prueba
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report')) #Estamos llamando a main y mandamos las banderas verbosity