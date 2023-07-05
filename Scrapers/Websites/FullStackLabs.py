from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Util import Offers

class FullStackLabs:

    COMPANY_NAME = "FullStack Labs"
    SITE_URL = "https://jobs.lever.co/fullstacklabs/?workplaceType=remote&department=Engineering"
    JOBS_TITLES_ELEMENT_XPATH = "//a[@class='posting-title']//h5[@data-qa='posting-name']"
    JOBS_LOCATION_ELEMENT_XPATH = ""
    JOBS_FULL_DESC_BUTTON_ELEMENT_XPATH = "//a[@class='posting-title']"
    JOB_FULL_DESCRIPTION_ELEMENT_XPATH = "//div[@class=\"section-wrapper page-full-width\"]"

    driver = ""
    jobs_list = []
    locations_list = []
    descriptions_links_list = []
    full_descriptions_list = []

    replace_list = {"We’re most proud of:": "We’re most proud of:\n",
                    "The Position:": "\nThe Position:\n",
                    "The position:": "\nThe position:\n",
                    "What We're Looking For:": "\nWhat We're Looking For:\n",
                    "You'll work with our incredible clients in one of two ways:": "You'll work with our incredible clients in one of two ways:\n",
                    "What we are looking for:": "\nWhat we are looking for:\n",
                    "Our Benefits:": "\nOur Benefits:",
                    "Benefits:": "\nBenefits:\n",
                    "Our \nBenefits:": "Our Benefits:",
                    "Learn more about our Applicants Privacy Notice.": "",
                    "\n\nAPPLY FOR THIS JOB": "",
                    "FullStack is proud to be an equal opportunity workplace. We are committed to equal employment opportunity regardless of race, color, ancestry, religion, sex, national origin, sexual orientation, age, citizenship, marital status, disability, gender identity, or Veteran status. If you have a disability or special need that requires accommodation, please let us know by completing our Accommodations for Applicants form, which can be provided upon request during our hiring and interview process.": ""}

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

        except Exception as e:
            print(e)

    def getDetailedDescriptions(self):
        try:
            for i in range(0, len(self.descriptions_links_list)):
                print(f"- Getting job detailed description ({i+1}/{len(self.descriptions_links_list)}).")

                desc_link = self.descriptions_links_list[i]
                self.driver.get(desc_link)
                
                sleep(2)

                try:
                    full_description = self.driver.find_element(By.XPATH, self.JOB_FULL_DESCRIPTION_ELEMENT_XPATH).text
                except Exception as e:
                    print(f"Error while getting full description: {desc_link} - Exception: {e}")
                    full_description = "Unknown."

                for word, replacement in self.replace_list.items():
                    full_description = full_description.replace(word, replacement).strip()
                    print(full_description)

                self.full_descriptions_list.append(full_description)

                with open(f"{i+1}.txt", "a", encoding="utf-8") as file:
                    file.write(full_description)

                sleep(3)

        except Exception as e:
            print(e)

    def generateOffers(self):
        pass

    def start(self):
        pass

scraper = FullStackLabs()
scraper.getListings()
scraper.getDetailedDescriptions()