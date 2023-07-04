from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Util import Offers

class FullStackLabs:

    COMPANY_NAME = "FullStackLabs"
    SITE_URL = "https://jobs.lever.co/fullstacklabs/?workplaceType=remote&department=Engineering"
    JOBS_TITLES_ELEMENT_XPATH = "//a[@class='posting-title']//h5[@data-qa='posting-name']"
    JOBS_LOCATION_ELEMENT_XPATH = ""
    JOBS_FULL_DESC_BUTTON_ELEMENT_XPATH = "//a[@class='posting-title']"
    JOB_FULL_DESCRIPTION_ELEMENT_XPATH = ""

    driver = ""
    jobs_list = []
    locations_list = []
    descriptions_links_list = []
    full_descriptions_list = []

    replace_list = {}

    def __init__(self):
        pass

    def getListings(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.SITE_URL)

        sleep(3)

        try:
            jobs = self.driver.find_elements(By.XPATH, self.JOBS_TITLES_ELEMENT_XPATH)
            description_links = self.driver.find_elements(By.XPATH, self.JOBS_FULL_DESC_BUTTON_ELEMENT_XPATH)

            temp_titles = []
            temp_desc_links = []

            for i in range(len(jobs)):
                title = jobs[i].text
                temp_titles.append(title)
                print(title)

            for i in range(len(description_links)):
                description_link = description_links[i].get_attribute("href")
                temp_desc_links.append(description_link)
                print(description_link)

            

        except Exception as e:
            print(e)

        




    def getDetailedDescriptions(self):
        pass

    def generateOffers(self):
        pass

    def start(self):
        pass

scraper = FullStackLabs()
scraper.getListings()