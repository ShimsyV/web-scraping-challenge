from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data = {}
    num = 3

    
    # NASA Latest Mars News
    print('Finding latest NASA Mars news.....\n')
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(num)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all('div', class_='list_text')

    # print(len(articles))

    news_title = articles[0].find('a').text
    print(f'Latest News: {news_title}')

    news_p = articles[0].find('div', class_='article_teaser_body').text
    print(f'Latest Teaser: {news_p}\n')

    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p

    print(f'Current Mars Data Dict is: {mars_data}\n\n')

    # JPL Mars Space Images - Featured Image
    print('Finding featured NASA JPL Mars space image.....\n')

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    time.sleep(num)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    browser.click_link_by_partial_text('FULL IMAGE')
    url_jpl2 = 'https://www.jpl.nasa.gov' + soup.find('a', class_='button')['data-link']
    browser.visit(url_jpl2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_url = 'https://www.jpl.nasa.gov' + soup.find('figure', class_='lede').a['href']
    print(featured_image_url)

    mars_data['featured_image_url'] = featured_image_url

    print(f'Current Mars Data Dict is: {mars_data}\n\n')


    # Mars Facts
    print('Finding Mars facts.....\n')

    mars_tbl_info = []


    url = 'https://space-facts.com/mars/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    table_info = soup.find('table', class_='tablepress tablepress-id-p-mars')

    for info in table_info.find_all('tr'):
        data = info.find('td', class_="column-1").text
        name = data.replace(':', '').rstrip()       
    
        val = info.find('td', class_="column-2").text

        mars_tbl_info.append({'name': name, 'value': val})
    
    print(mars_tbl_info)
  
    mars_data['mars_tbl_info'] = mars_tbl_info
   
    print(f'Current Mars Data Dict is: {mars_data}\n\n')  
    

    ### Mars Hemispheres
    print('Finding Mars hemispheres.....\n')

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # response = requests.get(url)
    browser.visit(url)
    html_hemispheres = browser.html
    soup = BeautifulSoup(html_hemispheres, 'html.parser')

    time.sleep(num)

    items = soup.find_all('div', class_='item')
    print(len(items))

    hemisphere_main_url = 'https://astrogeology.usgs.gov'
    hemisphere_image_urls = []

    for i in items:
        title = i.find('h3').text
    
    # Store link that leads to full image website
        partial_img_url = i.find('a', class_='itemLink product-item')['href']
    
    # Visit the link that contains the full image website 
        browser.visit(hemisphere_main_url + partial_img_url)
    
    # HTML Object of individual hemisphere information website 
        partial_img_html = browser.html
    
    # Parse HTML with Beautiful Soup for every individual hemisphere information website 
        soup = BeautifulSoup( partial_img_html, 'html.parser')
    
    # Retrieve full image source 
        img_url = hemisphere_main_url + soup.find('img', class_='wide-image')['src']
    
    # Append the retreived information into a list of dictionaries 
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})

            
        

    print(f'List of hemisphere urls: {hemisphere_image_urls}')
    
    mars_data['hemisphere_image_urls'] = hemisphere_image_urls
    print(f'Current Mars Data Dict is: {mars_data}\n\n') 
    
    browser.quit()

    return mars_data