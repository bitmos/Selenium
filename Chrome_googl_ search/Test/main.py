from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("D:\Coders_Club\Selenium\Chrome_googl_ search\chromedriver_win32\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://google.com")
search=driver.find_element_by_name("q")
search.send_keys("Automation step by Step.")
search.send_keys(Keys.RETURN)
time.sleep(4)
driver.quit()

