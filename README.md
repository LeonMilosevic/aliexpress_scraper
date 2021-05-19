# Ali Express Item Scraper

Packag that will help you scrape your bought items from ali-express.  

### Introduction
Package to help you scrape items from ali-express, it is a bot made in Selenium, that will login, go to your orders page and export all the items and ther info into a csv file.

### What does it scrape?

- order id
- order time
- store name
- store link
- order price
- item title
- item image url
- item price
- item amount
- item property

### How to use it?

Install prerequisites from requirements.txt

Import class:
```python
from scraper.scraper import Scraper
```

##### Scrape ebay for phones:

```python
scraper = Scraper(
    account_name = 'email@email.com', 
    account_password = 'password', 
    driver_path = '/usr/bin/chromedriver',
    num_of_pages = 5)
scraper.main()
```
##### Expected Results:

- ali_express.csv file with all scraped data in main directory 

##### Additional Info:

- You can check the docstrings and read how the Class works with its methods.

##### Note:

- Given the nature of ali-express website, when the next page is loaded, some items may be repeated and scraped twice. One solution to this is to scrape the website multiple times and combine unique results and get all the items you need.

