from bs4 import BeautifulSoup 
import requests

from url import weather_url 

# where we are pulling data from 
URL = weather_url

# get function is going to run a get response on the url page 
page = requests.get(URL)

# parsing information in html format 
soup = BeautifulSoup(page.text, 'html')


# web_scraping function 
def scrape_web_page()->None:
    pass


def main():
    scrape_web_page()




# point of entry 
if __name__ == "__main__":
    main()