# This is a simple Wikipedia web crawler that I made tweaking the code I found in online tutorials
# Kevin Flynn (xars7) 
#
# You can find the tutorial I found the original code from at this website: 
# https://www.freecodecamp.org/news/scraping-wikipedia-articles-with-python/
#
#
# Why did I tweak the Code?
#
# When I copy and pasted the code into a new py script it did work as intended. Unfortunatley 
# after the spider would find a couple pages they would then run into an HTTPS error.
# After googling the issue I found a solution on the internet that fit this code perfectly
# you can find the website where I found the solution to this problem here:
#
# https://programmersought.com/article/23943196472/
#
#
# Basically the spider tries to connect to the next article it can find by scraping 
# all of the links on the Wikipedia webpage. If it can't find another article, or
# the server denies it's request, the spider goes into sleep mode for 5 seconds.
# If it still cannot access the next page due to whateve reason
# It will return to the startingURL and start the proccess over again, looking 
# for more wikipedia pages to go to
#
# This program only works with wikipedia, but you can tweak this code to work with whatever
# website you would like to scrape/crawl.
#
# This was a fun project to make/tweak. Please please check out the websits I linked above.
# They deserve the love! 
#
# If you want to run this program on your computer you will need to have the following things installed
#
# 1. pip
# 2. BeautifulSoup
# 3. requests

import requests
from bs4 import BeautifulSoup
import random
import time

#   You can change this Url to any wikipedia page you specify. This will tell
#   the web spider where to start, and if the spider is stuck
#   they will return back to this Url
startingURL = "https://en.wikipedia.org/wiki/Web_scraping"
# create a function to scrape the article
def scrapeWikiArticle(url):
    # this creates a global variable called timesSlept
    # everytime the spider goes into sleep timesSlept
    # is incremented by one.
    global timesSlept
    timesSlept = 0
    # this is our main while loop
    while True:
        # try to request the next url
        try:
            # request the url
            response = requests.get(url=url,)
            # create a beautiful soup object that contains the content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            # assigns the title to the first heading in the webpage
            title = soup.find(id="firstHeading")
            # prints the title
            print(title.text)
            # sleeps for 1 second to give time to make another request
            time.sleep(1)
            # creates a variable called allLinks that finds every possible link on the page
            allLinks = soup.find(id="bodyContent").find_all("a")
            # shuffles the links to pick a random one
            random.shuffle(allLinks)
            # creates the linktoScrape variable
            linkToScrape = 0
            # iterable for loop that runs the same amount of times as the number of all the links
            for link in allLinks:
                # We are only interested in other wiki articles
                # if the link isn't a wiki article we want to skip it
                if link['href'].find("/wiki/") == -1:
                    continue
                # Use this link to scrape
                linkToScrape = link
                break
            # scrape the next wiki article using the linkToScrape
            scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])
        # if we can't make a request or if we're stuck go to sleep for 5 seconds
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            # adds 1 to the timesSlept variable
            timesSlept = timesSlept + 1
            # if we sleep 2 times in a row, we go back to the startingURL because we are stuck
            if timesSlept == 2:
                print("I'm stuck I gotta go back to the start")
                scrapeWikiArticle(startingURL)

            continue  
# starts the crawling proccess by sending the spider to the startingURL   
scrapeWikiArticle(startingURL)