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
            repeated_positions = []

            for i in range(len(jobs)):
                title = jobs[i].text
                temp_titles.append(title)

            for i in range(len(description_links)):
                description_link = description_links[i].get_attribute("href")
                temp_desc_links.append(description_link)

            for i in range(0, len(temp_titles)):
                if "Latin America" in temp_titles[i]:
                    if temp_titles[i] not in repeated_positions:
                        repeated_positions.append(temp_titles[i])
                        self.jobs_list.append(temp_titles[i].replace("- Remote ", ""))
                        self.locations_list.append("Remote")
                        self.descriptions_links_list.append(temp_desc_links[i])

                        print(f"{temp_titles[i].replace('- Remote ', '')} // {temp_desc_links[i]}")

            print(f"Total positions: {len(self.jobs_list)} // Total description links: {len(self.descriptions_links_list)}")

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