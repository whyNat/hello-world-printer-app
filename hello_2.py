# -*- coding: utf-8 -*
import unittest
from selenium import webdriver

class WsbPlCheck(unittest.TestCase):

    # warunki wstepne
    def setUp(self):
        self.driver = webdriver.Firefox()

    # przypadek uzycia
    def test_wsb_title(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        self.assertIn("Wyższe Szkoły Bankowe".decode("utf-8"), driver.title)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
