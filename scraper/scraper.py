from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select
from random import randint
import pandas as pd

class Scraper:

    def __init__(self, account_name: str, account_password: str, driver_path: str) -> None:
        self.__account_name = account_name
        self.__account_password = account_password
        self.__driver_path = driver_path

    def wait(self, driver: object, wait_time, by: By, element_identifier: str) -> None:
        try:
            # wait for the login popup
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((by, element_identifier)))
        except:
            driver.quit()  

    def hover_action(self, driver: object, element_identifier:str) -> None:
        hover = ActionChains(driver).move_to_element(driver.find_element_by_id(element_identifier))
        hover.perform()
        time.sleep(randint(2,4))
        return None
    
    def close_popup(self, driver: object) -> None:
        close_popup_element = driver.find_element_by_class_name("btn-close")
        close_popup_element.click()
        time.sleep(randint(1,5))
        return None

    def signin(self, driver: object):
        # hover over signin button
        self.hover_action(driver, "nav-user-account")

        # click signin button
        driver.find_element_by_class_name("sign-btn").click()
        
        # waiting for signin popup
        self.wait(driver, 20, By.ID, "batman-dialog-wrap")
        
        # get email and password fields and impute pw and email 
        email_input = driver.find_element_by_id("fm-login-id")
        password_input = driver.find_element_by_id("fm-login-password")

        email_input.send_keys(self.__account_name)
        time.sleep(randint(2,4))

        password_input.send_keys(self.__account_password)
        time.sleep(randint(4, 6))

        # click submit btn
        driver.find_element_by_class_name("fm-button").click()

    def get_my_orders_page(self, driver: object) -> None:
        # hover over account icon
        self.hover_action(driver, "nav-user-account")

        # go to my orders
        driver.find_element_by_link_text("My Orders").click()
        self.wait(driver, 20, By.LINK_TEXT, 'Orders')
        time.sleep(randint(2, 4))

        # select 30 elements per page
        Select(driver.find_element_by_id('simple-pager-page-size')).select_by_value('30')
        time.sleep(20)

    def scrape_item(self, driver: object, xpath: str) -> list:
        title = item.title
        # elements = driver.find_elements_by_xpath(xpath)
        # return [x.text for x in elements]
    
    def scrape_item_attributes(self, driver: object, xpath: str, attribute: str) -> list:
        elements = driver.find_elements_by_xpath(xpath)
        return [x.get_attribute(attribute) for x in elements]

    def scraping_data(self, driver: object, xpath_text: list, xpath_attribute: list) -> None:
        
        test = self.scrape_item_text(driver, xpath_text[0])
        print(test)
        # # create empty lists
        # order_id, order_time, store_name, store_link, order_price, item_image_url, item_title, item_price, item_amount, item_property = ([] for i in range(10))
        
        # # extract lists with text
        # text_list = [order_id, order_time, store_name, order_price, item_title, item_price, item_amount, item_property]
        
        # # extract lists with attribute
        # attribute_list = [store_link, item_image_url]
        # attribute_type = ['href', 'src']

        # # note: xpath_text parametar, strings must match order of text_list
        # for i in range(len(text_list)):
        #     text_list[i] = self.scrape_item_text(driver, xpath_text[i])

        # # note: xpath_attribute parametar and attribute_type, strings must match order of attribute_list
        # for i in range(len(attribute_list)):
        #     attribute_list[i] = self.scrape_item_attributes(driver, xpath_attribute[i], attribute_type[i])

        # print(len(order_id))
        # print(len(order_time))
        # print(len(store_name))
        # print(len(store_link))
        # print(len(order_price))
        # print(len(item_image_url))
        # print(len(item_title))
        # print(len(item_price))
        # print(len(item_amount))
        # print(len(item_property))

    def main(self):
        driver = webdriver.Chrome(self.__driver_path)
        driver.get("https://www.aliexpress.com/")

        # waiting for the popup to show
        self.wait(driver, 10, By.CLASS_NAME, "poplayer-content")

        # close the popup
        self.close_popup(driver)

        # sign in to the account
        self.signin(driver)

        # waiting for the account element to appear,
        # this will tell us that we are signed in 
        self.wait(driver, 30, By.CLASS_NAME, "_2kPHY")
        time.sleep(randint(4,6))
        self.get_my_orders_page(driver)

        #scrape items
        self.scraping_data(
            driver,
            xpath_text=["//td[@class='order-info']/p[@class='first-row']/span[@class='info-body']"],
            xpath_attribute=[""]
            # xpath_text=[
            #     "//td[@class='order-info']/p[@class='first-row']/span[@class='info-body']",
            #     "//td[@class='order-info']/p[@class='second-row']/span[@class='info-body']",
            #     "//td[@class='store-info']/p[@class='first-row']/span[@class='info-body']",
            #     "//td[@class='order-amount']/div[@class='amount-body']/p[@class='amount-num']",
            #     "//td[@class='product-sets']/div[@class='product-right']/p[@class='product-title']/a",
            #     "//td[@class='product-sets']/div[@class='product-right']/p[@class='product-amount']/span[1]",
            #     "//td[@class='product-sets']/div[@class='product-right']/p[@class='product-amount']/span[2]",
            #     "//td[@class='product-sets']/div[@class='product-right']/p[@class='product-property']"
            # ],
            # xpath_attribute=[
            #     "//td[@class='store-info']/p[@class='second-row']/a[1]",
            #     "//td[@class='product-sets']/div[@class='product-left']/a[@class='pic s50']/img"
            #     ]
             )






scraper = Scraper(
    account_name="x",
    account_password="x",
    driver_path="/usr/bin/chromedriver"
)
scraper.main()






# PATH = "/usr/bin/chromedriver"
# driver = webdriver.Chrome(PATH)

# driver.get("https://www.aliexpress.com/")

# try:
#     # wating for an element to popup
#     popup = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "poplayer-content"))
#     )

#     close_popup_el = driver.find_element_by_class_name("btn-close")
#     time.sleep(2)
#     close_popup_el.click()

#     # hover over signin button
#     time.sleep(4)
#     element_to_hover_over = driver.find_element_by_id("nav-user-account")

#     hover = ActionChains(driver).move_to_element(element_to_hover_over)
#     hover.perform()
#     time.sleep(3)

#     # click signin button
#     sign_in_btn = driver.find_element_by_class_name("sign-btn")
#     sign_in_btn.click()

#     time.sleep(5)

#     # get email and password fields and impute pw and email 
#     email_input = driver.find_element_by_id("fm-login-id")
#     password_input = driver.find_element_by_id("fm-login-password")

#     print("found elements")
#     email_input.send_keys("leonn.milosevic@gmail.com")
#     time.sleep(3)
#     password_input.send_keys("rolex187liu")
#     time.sleep(5)
#     print("sent keys")
#     # click submit btn
#     submit_btn = driver.find_element_by_class_name("fm-button")
#     print("found submit button")
#     submit_btn.click()
#     time.sleep(20)

#     # hover over account icon
#     element_to_hover_over = driver.find_element_by_id("nav-user-account")

#     hover = ActionChains(driver).move_to_element(element_to_hover_over)
#     hover.perform()
#     time.sleep(3)

#     # go to my orders
#     my_orders_element = driver.find_element_by_link_text("My Orders")
#     my_orders_element.click()
#     time.sleep(20)

#     # select 30 elements per page
#     select = Select(driver.find_element_by_id('simple-pager-page-size'))
#     select.select_by_value('30')
#     time.sleep(10)

#     order_id_elements = driver.find_elements_by_xpath("//td[@class='order-info']/p[@class='first-row']/span[@class='info-body']")
#     order_ids = [x.text for x in order_id_elements]

#     order_time_elements = driver.find_elements_by_xpath("//td[@class='order-info']/p[@class='second-row']/span[@class='info-body']")
#     order_times = [x.text for x in order_time_elements]

#     store_name_elements = driver.find_elements_by_xpath("//td[@class='store-info']/p[@class='first-row']/span[@class='info-body']")
#     store_names = [x.text for x in store_name_elements]

#     store_link_elements = driver.find_elements_by_xpath("//td[@class='store-info']/p[@class='second-row']/a[1]")
#     store_links = [x.get_attribute('href') for x in store_link_elements]

#     order_price_elements = driver.find_elements_by_xpath("//td[@class='order-amount']/div[@class='amount-body']/p[@class='amount-num']")
#     order_prices = [x.text for x in order_price_elements]

#     item_image_elements = driver.find_elements_by_xpath("//td[@class='product-sets']/div[@class='product-left']/a[@class='pic s50']/img")
#     item_images = [x.get_attribute('src') for x in item_image_elements]

#     item_title_elements = driver.find_elements_by_xpath("//td[@class='product-sets']/div[@class='product-right']/p[@class='product-title']/a")
#     item_titles = [x.text for x in item_title_elements]

#     item_price_elements = driver.find_elements_by_xpath("//td[@class='product-sets']/div[@class='product-right']/p[@class='product-amount']/span[1]")
#     item_prices = [x.text for x in item_price_elements]

#     item_price_elements = driver.find_elements_by_xpath("//td[@class='product-sets']/div[@class='product-right']/p[@class='product-amount']/span[1]")
#     item_prices = [x.text for x in item_price_elements]

#     item_amount_elements = driver.find_elements_by_xpath("//td[@class='product-sets']/div[@class='product-right']/p[@class='product-amount']/span[2]")
#     item_amounts = [x.text for x in item_amount_elements]

#     item_property_elements = driver.find_elements_by_xpath("//td[@class='product-sets']/div[@class='product-right']/p[@class='product-property']")
#     item_properties = [x.text for x in item_property_elements]

#     print(len(order_ids))
#     print(len(order_times))
#     print(len(store_names))
#     print(len(store_links))
#     print(len(order_prices))
#     print(len(item_images))
#     print(len(item_titles))

#     # TODO: convert to class, create dataframe, return

# except:
#     print("someting went wrong")
#     driver.quit()
