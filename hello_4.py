# -*- coding: utf-8 -*
import unittest
from selenium import webdriver
from time import sleep



search_word = "Nowy"

class SearchText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_word_Morawiecki(self):
        driver = self.driver
        driver.get("http://www.wp.pl")
        results = driver.find_elements_by_xpath('//div[contains(text(),"' + search_word + '")]')
        print(results[0].text)
        self.assertGreater(len(results), 1)

#//div[]

    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
