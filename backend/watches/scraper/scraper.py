from watches.models import Watch, Price
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set up Selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")

def scrape_watch_prices():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Get all watches from the database
    watches = Watch.objects.all()

    for watch in watches:        
        driver.get(watch.amazon_link)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        price_element = soup.select_one("div#corePrice_feature_div span.a-offscreen")
        if price_element:
            price = float(price_element.text.strip("$"))

            # Save the price to the database
            Price.objects.create(watch=watch, amount=price, timestamp=datetime.now())
            # Log as info when price is found
            logging.info(f"Found price for {watch.name} - {price}")
        else:
            logging.error(f"No price element found for {watch.name}. Exiting now :(")
            exit(-1)
    driver.quit()
