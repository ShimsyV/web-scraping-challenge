from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time

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
    image = soup.find_all('article', class_='carousel_item')

    # print(len(image))

    s_url = 'https://www.jpl.nasa.gov'
    e_url = image[0].find('a', class_='button fancybox')['data-fancybox-href']
    print(f'Partial image url: {e_url}')

    featured_image_url = s_url + e_url
    print(f'Complete image url: {featured_image_url}\n')

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
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    time.sleep(num)

    links = soup.find_all('div', class_='item')
    print(len(links))

    b_url = 'https://astrogeology.usgs.gov'
    page_list = []

    for link in links:
        img_page = link.find('a', class_='itemLink product-item')['href']
        print(f'Partial image url: {img_page}')
        page_url = b_url + img_page
        page_list.append(page_url)

    print(f'List of pages: {page_list}')

    hemisphere_image_urls = []
    
    for url in page_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('div', class_='downloads')
        hemi_img_url = data[0].find('a')['href']
        
        print(f'Complete image url: {hemi_img_url}')

        data = soup.find_all('section', class_='block metadata')
        title = data[0].find('h2', class_='title').text
        hemi_title = title.replace('Enhanced', '').rstrip()
        
        print(hemi_title)
        
        hemisphere_image_urls.append({'title': hemi_title, 'img_url': hemi_img_url})

    print(f'List of hemisphere urls: {hemisphere_image_urls}')
    
    mars_data['hemisphere_image_urls'] = hemisphere_image_urls
    print(f'Current Mars Data Dict is: {mars_data}\n\n') 
    
    browser.quit()

    return mars_data