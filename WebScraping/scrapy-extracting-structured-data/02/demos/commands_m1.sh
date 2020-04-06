#### m01_d01
#### Scrapy installation and exploring scrapy commands

#Installhome-brew(ifnotinstalled)
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

#Installpython3
brew install python3

#Installscrapy
pip3 install scrapy

# Check scrapy installation
scrapy

#You should see a list of commands available
#Exploring command line
#Bench mark test - ​built-in benchmark test to see how it performs on your hardware
scrapy bench

# Fetch the HTML contents of a page
scrapy fetch --nolog https://www.example.com/some/page.html

# View scrapy settings
# Empty by default
scrapy settings

# Check Scrapy version
scrapy version

# Open a URL in a browser as seen by scrapy
scrapy view https://quotes.toscrape.com/page/1/

# Scrapy by itself cannot scrape dynamic content from a webpage
# Open this URL in a browser first and note the list of Pluralsight authors
# Then run the scrapy view command - notice only part of the website is scraped
scrapy view https://www.pluralsight.com/authors




#### m01_d02
#### Scrapy shell

# launch shell 
scrapy shell 'http://quotes.toscrape.com/page/1/'

# scrapy location 
scrapy

# crawler object location 
crawler  

# item object - usually empty 
item

# request information type and URL 
request  

# response - status code and url  
response

#only response status 
response.status

#print url of the response 
response.url

#settings object - currently empty 
settings  
# getting the settings value using the key (defined in setting.py) for eg. BOT_NAME
settings.get('BOT_NAME')

#spider  - default spider object 
spider 

# fetch - fetch an url and redirect=True by default
fetch('https://www.un.org')

#print url of the updated response 
response.url

# print the HTML code of URL 
from pprint import pprint 
pprint(response.text)

# print header of the url 
pprint(response.headers)

# view the url in the browser (downloaded page)
# Copy the URL of the downloaded from the browser - will be used at the end of this demo
view(response)

#get the help screen (start ) 
shelp()

#exit the shell
exit()

# Show that Scrapy can also be used to scrape a downloaded HTML file
# Use the URL of the file copied just before exiting from the Scrapy shell
scrapy shell file:///private/var/folders/k1/cs73nb7s0157jb0g25yz3y6h0000gn/T/tmpl1yecdnr.html


#### m01_d03
#### Exploring the use of selectors

#start the the shell to execute the commands on the quotes webpage
scrapy shell 'http://quotes.toscrape.com/'

# Navigate to URL and check out the elements of the page
# Note the page title, the divs containing the quote text and authors

# Get the title of the page
response.css('title')

# The above command returns a list of Selector objects. 
# To view the data of the Selector, we'll extract it from the object
response.css('title').extract()

# We still get the data with the HTML tags
# To only get the actual text of the title, we specify the CSS pseudo element
# A pseudo element is a reference to a specific part of an HTML element
response.css('title::text').extract()

## Class Selectors

# View the list of authors of the quotes
# Since author is the name of a class, we can query by class using the dot notation
# All elements with the class name "author" will be scraped
response.css('.author')

# Get the type of object returned
type(response.css('.author'))

# Extract the data from the SelectorList
response.css('.author').extract()

# View the type of object extracted
type(response.css('.author').extract())

# Since it's a list, we can access individual elements by their index
response.css('.author').extract()[0]

# Alternatively, we can use the extract_first() method to get the first element
response.css('.author').extract_first()

# What are the element types in this list?
type(response.css('.author').extract_first())

# We can specify the CSS pseudo element to get the actual names of each author
# Note that we now get a list of strings with only the author name
response.css('.author::text').extract()

# We can also use the tag name to reference a class 
# Useful if there are different tags with class author and you only want to scrape specific tags
response.css('small.author::text').extract()


## Child Selectors
# There may be multiple classes in an HTML page, but you only want to scrape ones with a specific parent
# You can make use of the parent/child relationship between elements to scrape the required data
response.css('.quote > .text').extract()

# The list of authors can also be extracted this way
response.css('.quote > span > .author::text').extract()


## nth child
# If a parent element has multiple children, you can refer to the children by the index
# The "row" class has a div element whithin which all the quotes are present
# We access the nth child of that div element to extract the nth quote on the page
# This will scrape quote #2
response.css('.row > div > div:nth-child(2) > .text::text').extract()

# And now to scrape quote #5
response.css('.row > div > div:nth-child(5) > .text::text').extract()

# Attribute selector
# Extract all links on this page by scraping all the href values
response.css('a::attr(href)').extract()

# Extract the links from the footer
response.css('.footer > .container > p > a::attr(href)').extract()

# Extract the 2nd link from this div using the nth-child syntax
response.css('.footer > .container > p:nth-child(2) > a::attr(href)').extract()


# XPath selector
# Use absolute path 
response.xpath('/html/head/title').extract()

# Search for a particular tag using //
# This will return all results matching that tag
response.xpath('//title').extract()

# Extract one author using the Xpath
# Inspect the element using the browser and copy over its XPath
response.xpath('/html/body/div/div[2]/div[1]/div[8]/span[2]/small').extract()

# Just get rid of the array indices to scrape all authors 
response.xpath('/html/body/div/div/div/div/span/small').extract()

# Extract just the text
response.xpath('/html/body/div/div/div/div/span/small/text()').extract()

# Select a tag by specifying an attribute
# Syntax is //<tag_name>[@att_name='att_value']
# Here, we specify the class name
response.xpath("//span[@class='text']").extract()

# Get the text contents
response.xpath("//span[@class='text']/text()").extract()

# Extract the author names with this notation
response.xpath("//small[@itemprop='author']/text()").extract()



#### m1_d04
#### Finding patterns in a page

# Scrape the 2nd quotes page
scrapy shell 'http://quotes.toscrape.com/page/2/'

## The page has a number of quotes containing "friend". We try to scrape those
response.xpath("//*[contains(text(), 'friend')]/text()")

# Extract the data contents from the returned values
response.xpath("//*[contains(text(), 'friend')]/text()").extract()

# Get the "friend" quotes by referencing the text class
response.xpath("//*[@class='text'][contains(text(), 'friend')]/text()").extract()


# The equivalent when using CSS selector
response.css(".text:contains('friend')::text").extract()

# Extract Authors whose first name begins with A
# Look for Authors in the small tag
# Name begins with uppercase A, followed by 0 or more alphabets([a-z]*) (e.g. A Einstein should be picked up)
# First name followed by a space (/s) followed by 1 or more alphanumeric chars (\w)
response.css('.author::text').re('A[a-z]*\s\w+')

# With xpaths, we can also make use of the starts-with function
response.xpath("//*[@class='author'][starts-with(text(), 'A')]/text()").extract()



#### m1_d05
#### Scrapy Spiders

# Create a new Scrapy project
scrapy startproject m1_d05_intro_spider

# cd into the project directory
cd m1_d05_intro_spider

# View contents of directory
ls -n

# cd into the m1_d5_intro_spider directory
cd m1_d05_intro_spider

# View contents of directory
ls -n

# cd into spiders directory
cd spiders

# View contents of directory
ls -n

# Open up Sublime Text and write code for the Spider
# Save it in the m1_d5_intro_spider/m1_d5_intro_spider/spiders directory
# cd to the root directory of the project
cd ../..

# Execute the spider
scrapy crawl intro_spider

# Check that the book_titles.txt has been created 
ls -n

# View contents of book_titles.txt
# Show 100 titles have been scraped from the 5 pages
less -N book_titles.txt




#### m1_d06
#### CrawlSpiders & LinkExtractors

## Navigate to http://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html
## Right-click on one of the programme names (e.g. UNICEF) and inspect the element
## Note that the programme name can be extracted with this selector: div.field-item.even > h4::text
## Also note that the links at the top right of the page go to different language versions of the same page

# Create a new Scrapy project
scrapy startproject m1_d06_un_programme_crawler

# cd into spiders directory
cd m1_d06_un_programme_crawler/m1_d06_un_programme_crawler/spiders

# Open up Sublime Text and write code for the Spider
# Save it in the m1_d5_intro_spider/m1_d5_intro_spider/spiders directory
# cd to the root directory of the project
cd ../..

# Execute the spider
scrapy crawl un_programme_crawler

# Confirm the creation of the agencies file
ls -n

# Examine contents of file
# Contains a lot more than just the agencies
less -N un_agencies.txt

## Modify spider file to include allow rule
# Remove the un_agencies.txt file
rm un_agencies.txt

# Execute the spider again
scrapy crawl un_programme_crawler

# Examine contents of file
# Contains fewer rows, but lists agencies in multiple languages
less -N un_agencies.txt

## Modify spider file to include deny rule
# Remove the un_agencies.txt file
rm un_agencies.txt

# Execute the spider again
scrapy crawl un_programme_crawler

# Examine contents of file
# Contains fewer rows, with agency names in only specific languages
less -N un_agencies.txt


#### m1_d07
#### Generic Spider

# Create a new Scrapy project
scrapy startproject m1_d07_csv_spider

# cd into spiders directory
cd m1_d07_csv_spider/m1_d07_csv_spider/spiders

# Open up Sublime Text and write code for the Spider
# Save it in the m1_d5_intro_spider/m1_d5_intro_spider/spiders directory
# cd to the root directory of the project
cd ../..

# Execute the spider
scrapy crawl csv_spider


#### m1_d08
#### Nested Selectors

# Scrape amazon.in by searching or the term "macbook"
scrapy shell 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=macbook'

# Import the pprint module
from pprint import pprint

# Right-click at the top of the search results and notice the container with the individual results
# This is a ul with class name s-result-list
# We store this in an object called search_results
search_results = response.css('ul.s-result-list > li') 

# search_results is a SelectorList
type(search_results)

# Inspect the title of the top macbook in the search results
# Extract the titles of all macbooks
pprint(response.css('.s-access-title::text').extract())

# Instead of scanning the full response object, we can get these titles from our search_results
# So we have used a selector within our SelectorList
# This is a nested Selector
search_results.css('.s-access-title::text').extract()




#### m1_d09
#### Items Intro


# Scrape amazon.in by searching or the term "macbook"
scrapy shell 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=macbook'

# Within the shell, define an Item to store product information
import scrapy

class ProductItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()

# Create a new product
product1 = ProductItem()

# Import the pprint module
from pprint import pprint

# We create a SelectorList with all the search results
search_results = response.css('ul.s-result-list') 

# Inspect the title of the top macbook in the search results
# Extract the titles of all macbooks
pprint(search_results.css('.s-access-title::text').extract())

# Extract the title of the top macbook
pprint(search_results.css('.s-access-title::text').extract_first())

# Assign this title to the Item instance we created
product1['title'] = search_results.css('.s-access-title::text').extract_first()

# View the value of the field we just set
product1['title']

# Extract the link to the product page
search_results.css('a.s-access-detail-page::attr(href)').extract_first()

# Assign this to the Item instance
product1['link'] = search_results.css('a.s-access-detail-page::attr(href)').extract_first()

# View the value of the field we just set
product1['link']

# Check the value of the "price" field in the Item
# No value is set so we get a KeyError
product1['price']

# Set a value for it
product1['price'] = search_results.css('.s-price::text').extract_first()

# Now view the value
product1['price']

# Try to set a value for a field which doesn't exist
# Should get this message: KeyError: 'ProductItem does not support field: imageLink'
product1['imageLink'] = search_results.css('img.s-access-image::attr(src)').extract_first()


#### m1_d10
#### Items in a Spider

# Create a new project
scrapy startproject m1_d10_Items

# cd into the directory with items.py
cd m1_d10_Items/m1_d10_Items/

# Open up items.py in SublimeText or some text editor
# The file should consist of these lines
import scrapy

class ProductItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()

# Open up SumbimeText or some text editor and code up the product_scraper.py

# cd into the root directory of the project
cd ..

scrapy crawl amazon_product_scraper




#### m1_d11
#### ItemLoaders

# Create a new project
scrapy startproject m1_d11_ItemLoader

# cd into the directory with items.py
cd m1_d11_ItemLoader/m1_d11_ItemLoader/

# Create the items.py file with the ItemLoader
# Create a product_scraper.py spider

# Run the spider
# Make the changes such as adding default input and output processors and run again
scrapy crawl amazon_product_scraper_itemloader






#### m1_d12
#### Pipelines

# Create a new project
scrapy startproject m1_d12_Pipeline

# cd into the directory with items.py
cd m1_d12_Pipeline/m1_d12_Pipeline/

# items.py will be the same as the ones used in m1_d11 for ItemLoader
# Spider in the spiders directory will be slightly modified - the truncate_text function is not there

# Edit the pipelines.py and settings.py files

# cd to the root of the project
cd ..

# Run the spider
scrapy crawl product_scraper_pipeline

# Switch the order of the first two pipelines
# Note the error when checking the price of some of the products
# Re-run the spider




#### m1_d13
#### FeedExport

# Create a new project
scrapy startproject m1_d13_FeedExport

# cd into the directory with items.py
cd m1_d13_FeedExport/m1_d13_FeedExport/

# Copy over the items.py and pipelines.py from m1_d12_Pipelines
# Copy over the spider from m1_d12 and modify the exported item and spider name

# Modify the settings.py file to include the pipelines and feed exports
# Add these lines to the file
ITEM_PIPELINES = {
    'm1_d13_FeedExport.pipelines.MacbookCheck': 100,
    'm1_d13_FeedExport.pipelines.PriceCheck': 200,
    'm1_d13_FeedExport.pipelines.MarkAsViable': 300,
}

# Feed exporters
FEED_FORMAT = 'json'
FEED_URI = 'tmp/macbooks.json'

# cd to the root project directory
cd ..

# Run the spider
scrapy crawl product_scraper_feedexport

# View the feed export file
less tmp/macbooks.json

# Remove the feed export file
rm tmp/macbooks.json

# Edit the pipelines.py file to include the DropItem() code

# Re-run the spider
# Note that there is a warning about items being dropped
scrapy crawl product_scraper_feedexport

# View the feed export file
# The dropped items are no longer here
less tmp/macbooks.json



