import unittest

from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            "D:\Coders_Club\Selenium\Chrome_googl_ search\chromedriver_win32\chromedriver.exe")
        self.driver.get("http://python.org")

    def test_search(self):
        mainPage=page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element= "pycon"
        mainPage.click_go_button()
        search_result_page= page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()


    def tearDown(self):
        self.driver.close()
if __name__=="__main__":
    unittest.main()