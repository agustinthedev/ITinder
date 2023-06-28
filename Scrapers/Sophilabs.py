from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Offers import Offer

class Sophilabs:
    SITE_URL = "https://sophilabs.com/careers"
    SHOW_ALL_POSITIONS_BUTTON_XPATH = "//span[text()='Show All Positions']"
    JOBS_TITLES_ELEMENT_XPATH = "//main//section//div//div//ul//li//a//h3"
    JOBS_LOCATION_ELEMENT_XPATH = "//main//section//div//div//ul//li//a//h3//em"
    JOBS_FULL_DESCRIPTION_LINK_XPATH = "//main//section//div//div//ul//li//a"

    driver = ""
    jobs_list = [] # List of titles for open positions
    locations_list = [] # List of locations available for the open positons (remote/on-site)
    descriptions_links_list = [] # Link to the full description of the position
    full_descriptions_list = [] # Full description of the positions

    replace_list = {}

    def __init__(self):
        pass

    def getListings(self):
        try:
            self.driver = webdriver.Chrome()
            self.driver.get(self.SITE_URL)

            sleep(3)

            show_all = self.driver.find_element(By.XPATH, self.SHOW_ALL_POSITIONS_BUTTON_XPATH)
            show_all.click()

            sleep(2)

            jobs = self.driver.find_elements(By.XPATH, self.JOBS_TITLES_ELEMENT_XPATH)
            locations = self.driver.find_elements(By.XPATH, self.JOBS_LOCATION_ELEMENT_XPATH)
            description_links = self.driver.find_elements(By.XPATH, self.JOBS_FULL_DESCRIPTION_LINK_XPATH)

            try:
                for i in range(0, len(jobs)):
                    print(f"- Getting job title ({i+1}/{len(jobs)}).")

                    full_job = jobs[i].text
                    title_and_location_list = full_job.split("\n")
                    location = title_and_location_list[0]
                    title = title_and_location_list[1]

                    print(f"Title: {title} // Location: {location}")

                    
                    
            except Exception as e:
                print(f"Error 2: {e}")
        except Exception as e:
            print(f"Error: {e}")
            


scraper = Sophilabs()
scraper.getListings()