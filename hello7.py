# -*- coding: utf-8" -*
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



"""
1. Wejdz na https://wizzair.com/pl-pl/main-page#/
2. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
3. Wybierz rejestracja
4. Wprowadź imię
5. Wprowadź nazwisko
6. Wybierz płeć
7. Wprowadź nr tel
8. Wprowadź błędny adres email - brak znaku @
9. Wprowadź hasło
10. Wybierz kraj
11. Akceptuj politykę prywatności
12. Kliknij przycisk ZAREJESTRUJ SIĘ"

"""

valid_name = "Dick"
valid_surname = "Laurent"
telefon = "123123123"
invalid_email = "hhjkj.pl"
valid_password = "Qshiukk12"


class WizzairRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_registration_wrong_email(self):
        driver = self.driver
        driver.get("https://wizzair.com/#/")
        zaloguj_btn = driver.find_element_by_css_selector("li.navigation__item:nth-child(3) > button:nth-child(1)").click()
        rejestracja_btn = driver.find_element_by_css_selector("p.login-form__footer:nth-child(6) > button:nth-child(1)").click
        imie_field = driver.find_element_by_xpath("//input[@placeholder='First name']")

    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
