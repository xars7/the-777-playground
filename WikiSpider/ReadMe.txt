WikiSpider v1.0.0 

Made on 1/4/22

REQUIREMENTS -

    In order to run this program you need to import he modules BeautifulSoup4 and the Requests module using pip
    here are some resources to help you install these modules and pip if you don't already have it

    How to install pip - https://pip.pypa.io/en/stable/installation/
    How to install BeautifulSoup4 - https://www.geeksforgeeks.org/beautifulsoup-installation-python/
    How to install Requests - https://www.geeksforgeeks.org/how-to-install-requests-in-python-for-windows-linux-mac/

I cannot take full credit on this one, because I used some awesome peoples code to help me out!
Check these links to find the websites I used to help me make this WikiSpider
Please give them a visit they deserve the love!

https://www.freecodecamp.org/news/scraping-wikipedia-articles-with-python/

https://programmersought.com/article/23943196472/

DESCRIPTION --

    This WikiSpider will start on one wikipedia webpage. It will find all the current links on that page

    then sift through them and find the ones that are wikipedia articles and skip the ones that aren't
    then it will randomly choose a wikipedia article to go through. 

    It will randomly choose an article to go to, print the header of the article, and then repeat the same process over and over until it chooses
    a link it can't access or it gets stuck.

    If either of these happen the program will then go into a sleep mode giving the server time to respond to another request

    If the spider is stuck and sleeps 2 times in a row it will then traverse back to the startingURL and start over choosing another and most of the time 
    a different path to go down.

    I personally love this project, it's so interesting to see what wiki pages the spider will go to. 

WHY I MADE THIS PROJECT -

    I wanted to make a webscraper/webcrawler and decided to do some research on how to do it.

    I then found the freecodecamp article on how to make the wikipedia scraper.

    I copied and pasted the code into an empty py script, and it worked great!

    After the crawler found a few links and displayed them, it set off a list of weird HTTPS errors.

    Did some more research and found the programmersought article and found the solution to the problem.

    The crawler was either scraping pages too fast, or it would find a link that it's not permitted to
    go to, which is totally understandable.

    I then frankenstiend the code together and added a few finishing touches and the WikiSpider was born!


Anyway I hope you enjoy this program as much as I did making it, see you in the next one!

    

Peace,

Kevin Flynn/xars7

email: kevinflynn808@gmail.com
twitter: @kevinflynn808
reddit: u/xars77