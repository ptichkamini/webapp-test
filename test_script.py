import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PATH = "home/magdalena/Documents/chromedriver.exe"
URL = "https://todolist.james.am/#/"

class ToDo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_enter_item(self):
        driver = self.driver
        driver.get(URL)
        time.sleep(3)
        self.assertIn("To Do List", driver.title)
        input_bar = driver.find_element(By.XPATH, "/html/body/ng-view/section/header/form/input")
        input_bar.send_keys("Hi!")
        input_bar.send_keys(Keys.RETURN)
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/ng-view/section/section/ul/li[1]/div/label")
        assert elem.text == "Hi!"
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()