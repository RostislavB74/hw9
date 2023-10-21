import re
import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pprint

# base_url = " http://quotes.toscrape.com"
# second_url ="https://quotes.toscrape.com/author/"
# import requests /html/body/div/div[2]/div[1]/div[1]
# /html/body/div/div[2]/div[1]/div[1]
# /html/body/div/div[2]/div[1]/div[1]/span[2]/a


def get_url(_url):
    quotes = {}
    tags_list = []

    url = _url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.select('span[class=text]')
    for quota in quotes:
        print(quota.text)
    authors = soup.select('small[class=author]')
    for author in authors:
        print(author.text)
    tags = soup.select('div[class=tags] a[class=tag]')
    for tag in tags:
        tags_list.append(tag.text)
    print(tags_list)
    # content = soup.select()
    # quotes = soup.find_all('span', class_='text')
    # for quote in quotes:
    #     print(quote.text)
    # authors = soup.find_all('small', class_='author')
    # for author in authors:
    #     print(author.text)


# def get_url_authors(_url):

#     url = _url
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     authors = soup.find_all('h3', class_='author-title')
#     print(authors)
#     for author in authors:
#         print(author.text)
#     borns = soup.find_all('span', class_="author-born-date")
#     for born in borns:
#         print(born.text)


# def spider(urls):
#     data = []


if __name__ == "__main__":
    get_url('https://quotes.toscrape.com/')
    # get_url_authors('https://quotes.toscrape.com/author/')
# 'div[class=col-md-8] h4[class=quote] a')
