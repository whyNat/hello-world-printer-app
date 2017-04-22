import unittest
from selenium import webdriver


class SearchText(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session

        self.driver = webdriver.Chrome()
        driver = self.driver
        # driver.implicitly_wait(30)
        driver.maximize_window()
        # navigate to the application home page
        driver.get("http://www.google.com/")

    def test_search_by_text(self):
        driver = self.driver
        # get the search textbox
        search_field = driver.find_element_by_name("q")
        search_field.clear()
        # enter search keyword and submit
        search_field.send_keys("Selenium")
        search_field.submit()

    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
