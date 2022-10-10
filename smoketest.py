from encodings import search_function
from itertools import product
from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertion import AssertionTest
from searchtest import SearchTests 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

assertion_test = TestLoader().loadTestsFromTestCase(AssertionTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assertion_test, search_test])

kwargs = {
    "output": 'smoke-report'
} #usamos este diccionario para los errores

runner = HTMLTestRunner(**kwargs) #Declaramos el runner
runner.run(smoke_test) #Corremos el runner