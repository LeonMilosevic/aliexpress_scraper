from selenium import webdriver

PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.aliexpress.com/")