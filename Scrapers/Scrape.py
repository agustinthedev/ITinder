from Websites import Moovx
from datetime import datetime

class Scraper:
    def __init__(self):
        pass

    def getDateTime(self):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return date

    def startMoovxScraper(self):
        date = self.getDateTime()

        print(f"{date} - Started Moovx Scraper")

        scraper = Moovx.Moovx()
        scraper.start()
        
        print(f"{date} - Finished Moovx Scraper")

#scraper = Scraper()
#scraper.startMoovxScraper()