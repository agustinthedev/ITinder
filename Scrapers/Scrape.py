from Websites import Moovx
from Websites import FullStackLabs
from datetime import datetime
from Util import Offers

class Scraper:
    job_data = []
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
            data = scraper.getData()
            self.job_data.append(data)

    def saveData(self):
        for i in range(len(self.job_data)):
            company = self.job_data[i]["company"]
            job_list = self.job_data[i]["job_list"]
            location_list = self.job_data[i]["location_list"]
            link_list = self.job_data[i]["link_list"]
            full_descriptions = self.job_data[i]["full_descriptions"]

            for x in range(len(job_list)):
                position_title = job_list[x]
                position_location = location_list[x]
                position_link = link_list[x]
                position_description = full_descriptions[x]

                offer = Offers.Offer(company, position_title, position_location, position_link, position_description)
                offer.loadOffer()


scraper = Scraper()
scraper.startScrapers()
scraper.saveData()