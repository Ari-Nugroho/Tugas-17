import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_login_Berhasil(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(1)

    def test_login_gagal_user(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("Salah")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("162517282")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(1)

    def test_menu(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(1)
        driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)").click()
        time.sleep(1)
        
    def tearDown(self):
        self.driver.close()

    unittest.main()