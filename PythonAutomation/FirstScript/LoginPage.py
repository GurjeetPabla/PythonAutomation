'''
Created on Jan 23, 2018

@author: gurjeet30.singh

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
time.sleep(300)
driver.close()
'''
from   selenium import webdriver

browser=webdriver.Chrome()
browser.get("http://www.facebook.com")
username = browser.find_element_by_id( "guru99" )
password = browser.find_element_by_id( "password@123" )
submit   = browser.find_element_by_id( "submit"   )
  
username.send_keys("me")
password.send_keys( "mykewlpass" )
  
submit.click()
'''  
wait = WebDriverWait(browser, 5)
try:
page_loaded = wait.until_not(
lambda browser: browser.current_url == login_page
)
except TimeoutException:
self.fail( "Loading timeout expired" )
  
self.assertEqual(
browser.current_url,
correct_page,
msg = "Successful Login"
)
'''
