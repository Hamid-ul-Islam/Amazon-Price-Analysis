import requests
from bs4 import BeautifulSoup
import pandas
import matplotlib.pyplot as plt
import time
import datetime
import random


# Headers to bypass detection
header = ({
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Accept-Language':'en-US,en;q=0.9'})

# Saving files to CSV
def saving():
    now = datetime.datetime.now()
    timing = now.strftime("%H-%M-%S_%d-%m-%Y")
    path = './Data/'
    df = pandas.DataFrame(product_list)
    df.to_csv(path + f'{timing}-product_list.csv')
    print("File Saved.Check 'Data' Folder")


try:
    def scraping(page):
        url = f'https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A281407&qid=1656794217&ref=sr_pg_{page}'
        r = requests.get(url, headers=header)
        soup = BeautifulSoup(r.content, 'html.parser')
        time.sleep(0.5)
        # printing  all products

        all_title = soup.find_all(
            'div', class_='a-section a-spacing-small s-padding-left-small s-padding-right-small')

        # a = 0
        for title in all_title:
            titles = title.find('span', class_='a-size-base-plus').text
            try:
                price = title.find('span', class_='a-offscreen').text
            except:
                price = 'No Price Given'
            try:
                discount = title.find('span', class_='s-color-discount').text
            except:
                discount = 'No Discount'

            product = {
                'Name': titles,
                'Price': price,
                'Discount': discount
            }
            products = product_list.append(product)
            # a = a+1
            # print(f'{a}. {titles}\n{price}\n{discount}\n')

    product_list = []
    page_to_scrap = int(input("Collect Data for How Many Pages: "))
    for i in range(1, page_to_scrap+1):
        print(f'Collecting Data for page {i}')
        scraping(i)

    saving()

except:
    saving()
