from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select

PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.aliexpress.com/")

try:
    # wating for an element to popup
    popup = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "poplayer-content"))
    )

    close_popup_el = driver.find_element_by_class_name("btn-close")
    time.sleep(2)
    close_popup_el.click()

    # hover over signin button
    time.sleep(4)
    element_to_hover_over = driver.find_element_by_id("nav-user-account")

    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()
    time.sleep(3)

    # click signin button
    sign_in_btn = driver.find_element_by_class_name("sign-btn")
    sign_in_btn.click()

    time.sleep(5)

    # get email and password fields and impute pw and email 
    email_input = driver.find_element_by_id("fm-login-id")
    password_input = driver.find_element_by_id("fm-login-password")

    print("found elements")
    email_input.send_keys("xxx")
    time.sleep(3)
    password_input.send_keys("xxx")
    time.sleep(5)
    print("sent keys")
    # click submit btn
    submit_btn = driver.find_element_by_class_name("fm-button")
    print("found submit button")
    submit_btn.click()
    time.sleep(20)

    # hover over account icon
    element_to_hover_over = driver.find_element_by_id("nav-user-account")

    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()
    time.sleep(3)

    # go to my orders
    my_orders_element = driver.find_element_by_link_text("My Orders")
    my_orders_element.click()
    time.sleep(20)

    # select 30 elements per page
    select = Select(driver.find_element_by_id('simple-pager-page-size'))
    select.select_by_value('30')

    # TODO: scrape elements, convert to class, reorganise code, add docstrings etc etc

except:
    print("someting went wrong")
    driver.quit()
