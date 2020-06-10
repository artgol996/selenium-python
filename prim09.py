import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
time.sleep(5)
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Users\\bin\\chromedriver.exe')

    def test_search_in_google_com(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("google")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()