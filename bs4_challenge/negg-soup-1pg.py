# Import Libraries
from bs4 import BeautifulSoup
import requests

# Set URL for where BeautifulSoup will scrape for data
URL = "https://www.newegg.ca/p/pl?d=sata+ssd"

# gives the url request a header, which makes amazon think it is a web browser requesting the webpage and not a robot
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36', 'Accept-Encoding':'gzip, deflate', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'DNT':'1','Connection':'close', 'Upgrade-Insecure-Requests':'1'}

# Sets up webrequest with the URL and Header above and stores the request in a variable called webpage
webpage = requests.get(URL, headers=headers)

# Uses the webpage variable above to fetch all the data from the page in the URL and stores it in a variable called soup
soup = BeautifulSoup(webpage.text, 'html.parser')

# uses the BeautifulSoup library to find all items on a page and stores them in a list variable called results
results = soup.find_all("div", class_="item-cell")

# uses a for loop to iterate through all the items in the results list and pulls the title and price from each item and prints each one on the screen
for result in results:
    item = result.find("a", class_="item-title")
    price = result.find("li", class_="price-current")
    if price:
        print(price.text.strip())
    else:
        print("No price found for item", item.text.strip())
    try:
        print(item.text.strip())
    except AttributeError:
        print("No price found for item", item.text.strip())
