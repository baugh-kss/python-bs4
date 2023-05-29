# Import Libraries
from bs4 import BeautifulSoup
import requests

# Set URL for where BeautifulSoup will scrape for data
URL = 'https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/'

# gives the url request a header, which makes amazon think it is a web browser requesting the webpage and not a robot
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36', 'Accept-Encoding':'gzip, deflate', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'DNT':'1','Connection':'close', 'Upgrade-Insecure-Requests':'1'}

# Sets up webrequest with the URL and Header above and stores the request in a variable called webpage
webpage = requests.get(URL, headers=headers)

# Uses the webpage variable above to fetch all the data from the page in the URL and stores it in a variable called soup
soup = BeautifulSoup(webpage.content, 'html.parser')

# uses the beautiful soup library to search the "soup" to find the title and price of the item
get_title = soup.find('span', attrs={'id':'productTitle'})
get_price = soup.find('span', class_='a-offscreen')

print("This is the output of the get_title and the get_price variables:" + "\n")

print(get_title)
print(get_price)

# cleans up the price and title to include on the title and price and none of the html compile
# when you run the program, look at the differnce between between the first two lines of output
# and the last two lines of output.
title = get_title.text.strip()
price = get_price.text.strip()

print("-----------------------------------------------------------------------------------------------------------") 
print("This is the output of title and price variables:" + "\n")
print(title)
print(price)

