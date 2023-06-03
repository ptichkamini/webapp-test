import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import signal

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

    def test_enter_items(self):
        driver = self.driver
        driver.get(URL)
        time.sleep(3)
        input_bar = driver.find_element(By.XPATH, "/html/body/ng-view/section/header/form/input")
        input_bar.send_keys("Hi!")
        input_bar.send_keys(Keys.RETURN)
        input_bar.send_keys("Bye!")
        input_bar.send_keys(Keys.RETURN)
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/ng-view/section/section/ul/li[1]/div/label")
        assert elem.text == "Hi!"
        elem = driver.find_element(By.XPATH, "/html/body/ng-view/section/section/ul/li[2]/div/label")
        assert elem.text == "Bye!"
        # todo: enter random elements using a loop and random

    def test_remove(self):
        driver = self.driver
        driver.get(URL)
        time.sleep(3)
        input_bar = driver.find_element(By.XPATH, "/html/body/ng-view/section/header/form/input")
        item1 = ''.join(random.sample(string.ascii_letters, 15))
        input_bar.send_keys(item1)
        input_bar.send_keys(Keys.RETURN)
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/ng-view/section/section/ul/li[1]/div/label")
        assert elem.text == item1
        a_chains = ActionChains(driver)
        a_chains.move_to_element(elem).perform()
        time.sleep(3)
        remove_button = driver.find_element(By.XPATH, "/html/body/ng-view/section/section/ul/li/div/button")
        remove_button.click()
        time.sleep(3)
        with self.assertRaises(NoSuchElementException):
            driver.find_element(By.XPATH, "/html/body/ng-view/section/section/ul/li[1]/div/label")


    def test_edit(self):
        driver = self.driver
        driver.get(URL)
        time.sleep(3)
        input_bar = driver.find_element(By.XPATH, "/html/body/ng-view/section/header/form/input")
        item1 = ''.join(random.sample(string.ascii_letters, 15))
        input_bar.send_keys(item1)
        input_bar.send_keys(Keys.RETURN)
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/ng-view/section/section/ul/li[1]/div/label")
        assert elem.text == item1
        a_chains = ActionChains(driver)
        a_chains.double_click(elem).perform()
        edit_field = driver.find_element(By.XPATH,"/html/body/ng-view/section/section/ul/li/form/input")
        edit_field.send_keys(" NEW!")
        time.sleep(3)
        input_bar.send_keys(Keys.RETURN)
        time.sleep(3)
        assert (item1 + " NEW!")

    def test_select_all(self):
        driver = self.driver
        driver.get(URL)
        time.sleep(3)
        input_bar = driver.find_element(By.XPATH, "/html/body/ng-view/section/header/form/input")
        item1 = ''.join(random.sample(string.ascii_letters, 15))
        item2 = ''.join(random.sample(string.ascii_letters, 20))
        input_bar.send_keys(item1)
        input_bar.send_keys(Keys.RETURN)
        input_bar.send_keys(item2)
        input_bar.send_keys(Keys.RETURN)
        time.sleep(3)
        select_all = driver.find_element(By.XPATH, "/html/body/ng-view/section/section/label")
        select_all.click()
        time.sleep(3)
        if driver.find_element(By.CLASS_NAME, "completed").is_displayed():
            print("Item is checked")
        else:
            print("Item is not checked")

    def test_counter(self):
        pass

    def test_refresh(self):
        pass

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()