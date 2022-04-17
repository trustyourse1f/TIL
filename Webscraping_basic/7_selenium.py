from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://naver.com")

elem = browser.find_element_by_xpath('//*[@id="query"]')
elem.click()
elem.send_keys("야구")
elem.send_keys(Keys.ENTER)