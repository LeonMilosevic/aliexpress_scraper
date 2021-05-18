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
    def __init__(self, account_name: str, account_password: str, driver_path: str, num_of_pages: int) -> None:
        self.__account_name = account_name
        self.__account_password = account_password
        self.__driver_path = driver_path
        self.__num_of_pages = num_of_pages

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
    
    def scrape_items(self, driver: object) -> list:

        items = []

        # get order elements
        orders = driver.find_elements_by_tag_name('tbody')

        # loop over each order
        for order in orders:
            
            # get orders specifications
            order_id = order.find_element_by_xpath(".//tr[@class='order-head']/td[@class='order-info']/p[@class='first-row']/span[@class='info-body']").text
            order_time = order.find_element_by_xpath(".//td[@class='order-info']/p[@class='second-row']/span[@class='info-body']").text
            store_name = order.find_element_by_xpath(".//td[@class='store-info']/p[@class='first-row']/span[@class='info-body']").text
            store_link = order.find_element_by_xpath(".//td[@class='store-info']/p[@class='second-row']/a[1]").get_attribute("href")
            order_price = order.find_element_by_xpath(".//td[@class='order-amount']/div[@class='amount-body']/p[@class='amount-num']").text

            # get items from orders
            order_items = order.find_elements_by_xpath(".//tr[@class='order-body']")

            # loop over each item in order
            for item in order_items:
                # scrape item specifications
                item_title = item.find_element_by_xpath(".//td[@class='product-sets']/div[@class='product-right']/p[@class='product-title']/a").text
                item_image_url = item.find_element_by_xpath(".//td[@class='product-sets']/div[@class='product-left']/a[@class='pic s50']/img").get_attribute("src")
                item_price = item.find_element_by_xpath(".//td[@class='product-sets']/div[@class='product-right']/p[@class='product-amount']/span[1]").text
                item_amount = item.find_element_by_xpath(".//td[@class='product-sets']/div[@class='product-right']/p[@class='product-amount']/span[2]").text
                item_property = item.find_element_by_xpath(".//td[@class='product-sets']/div[@class='product-right']/p[@class='product-property']").text
                
                # create new object of an item
                new_item = {
                    "order_id": order_id,
                    "order_time": order_time,
                    "store_name": store_name,
                    "store_link": store_link,
                    "order_price": order_price,
                    "item_title": item_title,
                    "item_image_url": item_image_url,
                    "item_price": item_price,
                    "item_amount": item_amount,
                    "item_property": item_property
                }

                items.append(new_item)

        return items

    def get_all_items(self, driver: object) -> list:
        all_items = []
        
        # scrape each page
        for _ in range(self.__num_of_pages):
            items = self.scrape_items(driver)

            all_items.extend(items)

            self.get_next_page(driver)
        
        return all_items

    def get_next_page(self, driver: object) -> None:
        # click next page element
        driver.find_element_by_xpath("//div[@class='ui-pagination-navi util-left']/*[last()]").click()
        time.sleep(randint(12, 15))

    def export_csv(self, items: list) -> None:
        df = pd.DataFrame(items)
        df.to_csv('aliexpress_csv', index=False)

    def main(self) -> None:
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

        # scrape all items from the account
        all_items = self.get_all_items(driver)
        
        # export to csv file
        self.export_csv(all_items)