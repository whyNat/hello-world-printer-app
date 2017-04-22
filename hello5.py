# -*- coding: utf-8 -*
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
Open page wp.pl
Go to "poczta"
Login to user "testerwsb_t1"
Password "adam1234"
Check if there is a word "Odebrane"

Do the same with wrong Password
Do the same with the wrong username
Do the same with wrong password and user
'''

valid_username = "testerwsb_t1"
valid_password = "adam1234"
wrong_username = "tester"
wrong_password = "adam"
search_word = "Odebrane"

class WpPlSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_mail(self):
        driver = self.driver
        driver.get("http://www.wp.pl")
        driver.find_element_by_link_text("POCZTA").click()
        #login_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.ID, "login"))
        login_field = driver.find_element_by_id("login")
        login_field.send_keys(valid_username)
        password_field = driver.find_element_by_id("password")
        password_field.send_keys(valid_password)
        driver.find_element_by_id("btnSubmit").click()
        driver.find_elements_by_xpath('//div[contains(text(),"' + search_word + '")]')

    def test_mail_2(self):
        driver = self.driver
        driver.get("http://www.wp.pl")
        driver.find_element_by_link_text("POCZTA").click()
        #login_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.ID, "login"))
        login_field = driver.find_element_by_id("login")
        login_field.send_keys(wrong_username)
        password_field = driver.find_element_by_id("password")
        password_field.send_keys(wrong_password)
        driver.find_element_by_id("btnSubmit").click()



    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
