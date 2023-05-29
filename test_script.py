import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
PATH = "home/magdalena/Documents/chromedriver.exe"
URL = "https://todolist.james.am/#/"

#driver.get(URL)
#time.sleep(3)

class ToDo(unittest.TestCase):
    def setUp(self):
        self.driver = driver
    def test_enter_item(self):
        pass
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()