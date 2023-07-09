from Websites import Moovx
from Websites import FullStackLabs
from datetime import datetime

class Scraper:
    data = []
    scrapers = []

    def __init__(self):
        fullstacklabs_scraper = FullStackLabs.FullStackLabs()
        self.scrapers.append(fullstacklabs_scraper)

    def getDateTime(self):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return date
    
    def startScrapers(self):
        for scraper in self.scrapers:
            scraper.startScraping()

scraper = Scraper()
scraper.startScrapers()