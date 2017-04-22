import unittest
from selenium import webdriver
from time import sleep


class SearchText(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session

        self.driver = webdriver.Chrome()
        driver = self.driver
        # driver.implicitly_wait(30)
        driver.maximize_window()


    def test_search_by_text(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        # get the search textbox
        #search_field = driver.find_element_by_css_selector("#block-menu-menu-wybierz-studia-w-wsb > div > ul > li:nth-child(2) > a")
        # enter search keyword and submit
        link = driver.find_element_by_link_text("Studia podyplomowe")
        link.click()
        sleep(5)


    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
