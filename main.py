import re
import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pprint

# base_url = " http://quotes.toscrape.com"

# import requests


def get_url(_url):

    url = _url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span', class_='text')
    for quote in quotes:
        print(quote.text)
    authors = soup.find_all('small', class_='author')

    for author in authors:
        print(author.text)


if __name__ == "__main__":
    get_url('https://quotes.toscrape.com/')
# 'div[class=col-md-8] h4[class=quote] a')
