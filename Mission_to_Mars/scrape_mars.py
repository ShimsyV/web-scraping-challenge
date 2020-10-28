# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pymongo
import pandas as pd
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_data = {}

    # Latest Mars news
    print('Finding latest NASA Mars news... ')
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', class_='list_text')

    news_title = results[0].find('a').text
    news_p = soup.find('div', class_='article_teaser_body').text

    # Display scrapped data 

    print(f'Latest news: {news_title}')
    print(f'Latest Teaser: {news_p}')

    # JPL Mars Space Image - Featured image
    print('Looking for featured NASA JPL mars space image...')
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    browser.click_link_by_partial_text('FULL IMAGE')
    url_jpl2 = 'https://www.jpl.nasa.gov' + soup.find('a', class_='button')['data-link']
    browser.visit(url_jpl2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_url = 'https://www.jpl.nasa.gov' + soup.find('figure', class_='lede').a['href']
    print(f'Complete image url: {featured_image_url}\n')

    


