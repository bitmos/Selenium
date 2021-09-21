from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("D:\Coders_Club\Selenium\Chrome_googl_ search\chromedriver_win32\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(5)

cookie= driver.find_element_by_id("bigCookie")
count_cookies= driver.find_element_by_id("cookies")
items=[driver.find_element_by_id("product"+str(i)) for i in range(1,-1,-1)]
actions= ActionChains(driver)
actions.click(cookie)
cursor="Cursor\n"
for i in range(50):
    actions.perform()
    count=int(count_cookies.text.split(" ")[0])
    for item in items:
        if cursor in item.text :
            v=(item.text).split("\n")
            value=int(v[1])
        else:
            value=int(float(str(item.text).replace("???\n", "")))
        if value<= count:
            upgrade_actions= ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()