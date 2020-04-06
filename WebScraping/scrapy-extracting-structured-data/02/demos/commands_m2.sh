#### m2_d01
#### Logging

# Create a new project
scrapy startproject m2_d01_Logging

# cd into project dir
cd m2_d01_Logging

# Create the items.py file
# Create the spider 

# Run the spider
# All the log output is seen on stdout
scrapy crawl logger

# Create a tmp directory in which the log file will be created
mkdir tmp

# Edit the settings.py file and enable logging
# LOG Priority levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_ENABLED = True
LOG_FILE = 'tmp/log.txt'
LOG_LEVEL = 'DEBUG'

# Re-run the spider
# The log output is not visible on the terminal
scrapy crawl logger

# Check the contents of the log file created
# Note the number of lines
less -N tmp/log.txt

# Remove the log file
rm tmp/log.txt

# Edit the settings.py file and set LOG_LEVEL = 'INFO'

# Re-run the spider
# The log output is not visible on the terminal
scrapy crawl logger

# Check the contents of the log file created
# Note the number of lines - should be lower than on the previous run with LOG_LEVEL = 'DEBUG'
less -N tmp/log.txt



#### m2_d02
#### EmailNotification

# Create a new project
scrapy startproject m2_d02_EmailNotification

# cd into the project dir
cd m2_d02_EmailNotification

# Edit the spider set the start_url to a page without a response

# Login to the receiving inbox and note the lack of emails

# Run the spider
scrapy crawl email_notification

# Note there is no email and a log output to indicate there are no answers

# Set the start_url in the spider to a page which has responses to the question
# Re-run the spider
# Note that at the end there is a log output to indicate the sending of the email
scrapy crawl email_notification

# Check the recipient inbox for the email




#### m2_d03
#### BroadCrawler

# Create a new project
scrapy startproject m2_d03_BroadCrawler

# cd into project directory
cd m2_d03_BroadCrawler

# Create the items.py file
# Create the spider

# Edit the settings.py file to include the following lines
CONCURRENT_REQUESTS=20 
DOWNLOAD_TIMEOUT = 15
REDIRECT_ENABLED = False

# Feed exporters
FEED_FORMAT = 'csv'
FEED_URI = 'emails_scraped.csv'

# Open up two terminals - one to run the spider, another to monitor resource usage
# Run the spider from terminal #1
scrapy crawl scrape_emails

# On terminal #2, run the top command
top

# On terminal #1, check the contents of emails_scraped.csv
less -N emails_scraped.csv

# Delete the csv file ahead of the next run
rm emails_scraped.csv

# In settings.py, set REDIRECT_ENABLED = True

# Re-run the spider
# While it's running, keep an eye on terminal #2 for resource usage
scrapy crawl scrape_emails

# Once more, check the contents of emails_scraped.csv
# There should be many more lines due to the redirect
less -N emails_scraped.csv

# Note the time taken for the previous execution
# In settings.py set CONCURRENT_REQUESTS = 2
# Re-run the spider
scrapy crawl scrape_emails





#### m2_d04
#### Telnet Console

# Go to the directory for m2_d03_BroadCrawler
# Confirm that the number of concurrent requests is 2 in settings.py
# In one terminal, start the BroadCrawler
scrapy crawl scrape_emails

# In terminal #2, connect to the telnet console
telnet localhost 6023

# View some statistics for this crawl
crawler.stats.get_stats()

# Use the shorthand for pretty-print
p(crawler.stats.get_stats())

#view scrapy engine status
est()

# View requests in progress
p(slot.inprogress)

# pause the engine (scrapy engine)
engine.pause()

# unpause the engine (scrapy engine)
engine.unpause()

# If you let the crawler run to completion, the telnet console will get disconnected automatically

# Restart the crawler on terminal #1
scrapy crawl scrape_emails

# On terminal #2, forcibly stop the scrapy engine
engine.stop()





#### m2_d04
#### Autothrottle

# Go to the directory for m2_d03_BroadCrawler

# Open the settings.py file and comment out the CONCURRENT_REQUESTS setting
# Enter these values for Autothrottling
AUTOTHROTTLE_ENABLED=True
AUTOTHROTTLE_START_DELAY=15
AUTOTHROTTLE_TARGET_CONCURRENCY = 40
AUTOTHROTTLE_DEBUG = True

# Start the BroadCrawler in terminal #1
# Note down the start and end times
scrapy crawl scrape_emails

# In terminal #2 run the top command
top

# Set AUTOTHROTTLE_START_DELAY=3 in settings.py
# Start the BroadCrawler
# Note down the start and end times
scrapy crawl scrape_emails

# Set AUTOTHROTTLE_TARGET_CONCURRENCY = 2
# Start the BroadCrawler
# Note down the start and end times
scrapy crawl scrape_emails












