# Ali Express Item Scraper

Packag that will help you scrape your bought items from ali-express.  

### Introduction
Package to help you scrape items from ali-express, it is a bot made in Selenium, that will login, go to your orders page and export all the items and their info into a csv file.

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

### How to use it?

1. Install the scraper

```python
pip install git+https://github.com/LeonMilosevic/aliexpress_scraper
```

2. Install prerequisites from requirements.tx

3. Import class:

```python
from scraper.scraper import Scraper
```

4. Scrape ali-express personal orders:

```python
scraper = Scraper(
    account_name = 'your_email@email.com', 
    account_password = 'your_password', 
    driver_path = '/your_path',
    num_of_pages = 5)
scraper.main()
```
##### Expected Results:

- ali_express.csv file with all scraped data in main directory 

##### Additional Info:

- You can check the docstrings and read how the Class works with its methods.

##### Note:

- Given the nature of ali-express website, when the next page is loaded, some items may be repeated and scraped twice. One solution to this is to scrape the website multiple times and combine unique results and get all the items you need.

