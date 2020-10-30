# Mission to Mars

![](https://github.com/ShimsyV/web-scraping-challenge/blob/main/Mission_to_Mars/readme_images/mission_mars.png)

#### My operation was to build a web application that scrapes various websites for data related to the Mission to Mars and display the information in a single HTML page.

### Scraping

Using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter , I created a Jupyter Notebook file called mission_to_mars.ipynb and used this to complete all of my scraping and analysis tasks. 

#### NASA Mars News

Scraped the NASA Mars [News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest) and collected the latest News Title and Paragraph Text. 

![](https://github.com/ShimsyV/web-scraping-challenge/blob/main/Mission_to_Mars/readme_images/Latest_news.PNG)

#### JPL Mars Space Images - Featured Image

Visited the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars). Used splinter to navigate the site and find the image url for the current Featured Mars Image and assigned the url string to a variable called *featured_image_url*. Made sure to find the image url to the full size .jpg image.Then saved a complete url string for this image. Click [here](https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23354_hires.jpg) for the link. This image is subject to change. As the website keeps updating the images , the featured images will change. 

![](https://github.com/ShimsyV/web-scraping-challenge/blob/main/Mission_to_Mars/readme_images/featured_image1.png)

#### Mars Facts

Visited the Mars Facts webpage [here](https://space-facts.com/mars/) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Used Pandas to convert the data to a HTML table string.

![](https://github.com/ShimsyV/web-scraping-challenge/blob/main/Mission_to_Mars/readme_images/mars_facts.PNG)

#### Mars Hemispheres

Visited the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres. I clicked each of the links to the hemispheres in order to find the image url to the full resolution image. Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. 

![](https://github.com/ShimsyV/web-scraping-challenge/blob/main/Mission_to_Mars/readme_images/mars_hemispheres.PNG)

### MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above. Started by converting the Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that executed all of the scraped code from above and return one Python dictionary containing all of the scraped data.

Next, created a route called /scrape that imported the scrape_mars.py script and called the scrape function.

Stored the return value in Mongo as a Python dictionary.

Created a root route / that queried the Mongo database and passed the mars data into an HTML template to display the data.

Created a template HTML file called index.html that took the mars data dictionary and displayed all of the data in the appropriate HTML elements. The scraped page looked like below

![](https://github.com/ShimsyV/web-scraping-challenge/blob/main/Mission_to_Mars/readme_images/scraped_page_a.PNG)

![](https://github.com/ShimsyV/web-scraping-challenge/blob/main/Mission_to_Mars/readme_images/scraped_page_b.PNG)










