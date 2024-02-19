import requests
import datetime

from bs4 import BeautifulSoup 

from url import weather_url 

# where we are pulling data from 
URL = weather_url

# get function is going to run a get response on the url page 
page = requests.get(URL)

# parsing the HTML
soup = BeautifulSoup(page.text, 'html')


def finding_information() -> None:

    # Extract desired information
    weather_button = soup.find("butotn", class_="wob_df")

    weather_data = weather_button.find('div', class_="wNE31c").get_text()

    print(weather_data)


# web_scraping function 
def scrape_web_page()->None:
    pass


def main():
    finding_information()



# point of entry 
if __name__ == "__main__":
    main()