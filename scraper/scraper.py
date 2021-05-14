from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select
from random import randint

class Scraper:

    def __init__(self, account_name: str, account_password: str, driver_path: str):
        self.__account_name = account_name
        self.__account_password = account_password
        self.__driver_path = driver_path

    def close_popup(self, driver: object):
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "poplayer-content"))
            )
            close_popup_element = driver.find_element_by_class_name("btn-close")
            close_popup_element.click()
            time.sleep(randint(1,5))
        except:
            print("someting went wrong")
            driver.quit()



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
    email_input.send_keys("leonn.milosevic@gmail.com")
    time.sleep(3)
    password_input.send_keys("rolex187liu")
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
    time.sleep(10)

    order_id_elements = driver.find_elements_by_xpath("//td[@class='order-info']/p[@class='first-row']/span[@class='info-body']")
    order_ids = [x.text for x in order_id_elements]

    order_time_elements = driver.find_elements_by_xpath("//td[@class='order-info']/p[@class='second-row']/span[@class='info-body']")
    order_times = [x.text for x in order_time_elements]

    store_name_elements = driver.find_elements_by_xpath("//td[@class='store-info']/p[@class='first-row']/span[@class='info-body']")
    store_names = [x.text for x in store_name_elements]

    store_link_elements = driver.find_elements_by_xpath("//td[@class='store-info']/p[@class='second-row']/a[1]")
    store_links = [x.get_attribute('href') for x in store_link_elements]

    order_price_elements = driver.find_elements_by_xpath("//td[@class='order-amount']/div[@class='amount-body']/p[@class='amount-num']")
    order_prices = [x.text for x in order_price_elements]

    item_image_elements = driver.find_elements_by_xpath("//td[@class='product-sets']/div[@class='product-left']/a[@class='pic s50']/img")
    item_images = [x.get_attribute('src') for x in item_image_elements]

    item_title_elements = driver.find_elements_by_xpath("//td[@class='product-sets']/div[@class='product-right']/p[@class='product-title']/a")
    item_titles = [x.text for x in item_title_elements]

    item_price_elements = driver.find_elements_by_xpath("//td[@class='product-sets']/div[@class='product-right']/p[@class='product-amount']/span[1]")
    item_prices = [x.text for x in item_price_elements]

    item_price_elements = driver.find_elements_by_xpath("//td[@class='product-sets']/div[@class='product-right']/p[@class='product-amount']/span[1]")
    item_prices = [x.text for x in item_price_elements]

    item_amount_elements = driver.find_elements_by_xpath("//td[@class='product-sets']/div[@class='product-right']/p[@class='product-amount']/span[2]")
    item_amounts = [x.text for x in item_amount_elements]

    item_property_elements = driver.find_elements_by_xpath("//td[@class='product-sets']/div[@class='product-right']/p[@class='product-property']")
    item_properties = [x.text for x in item_property_elements]

    print(len(order_ids))
    print(len(order_times))
    print(len(store_names))
    print(len(store_links))
    print(len(order_prices))
    print(len(item_images))
    print(len(item_titles))

    # TODO: convert to class, create dataframe, return

except:
    print("someting went wrong")
    driver.quit()
