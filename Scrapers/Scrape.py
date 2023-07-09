from Websites import Moovx
from Websites import FullStackLabs
from datetime import datetime

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

            print(f"{company} \n {job_list} \n {location_list} \n {link_list}")


scraper = Scraper()
scraper.startScrapers()
scraper.saveData()