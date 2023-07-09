from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Util import Offers

class FullStackLabs:

    COMPANY_NAME = "FullStack Labs"
    SITE_URL = "https://jobs.lever.co/fullstacklabs/?workplaceType=remote&department=Engineering" # Job listing website
    JOBS_TITLES_ELEMENT_XPATH = "//a[@class='posting-title']//h5[@data-qa='posting-name']" # XPATH for the position title element
    JOBS_LOCATION_ELEMENT_XPATH = "" # XPATH for the position location element is not needed, all positions are remote
    JOBS_FULL_DESC_BUTTON_ELEMENT_XPATH = "//a[@class='posting-title']" # XPATH for the position full description link (get href attribute for this element)
    JOB_FULL_DESCRIPTION_ELEMENT_XPATH = "//div[@class=\"section-wrapper page-full-width\"]" # XPATH for full position description

    driver = "" # Chrome driver
    jobs_list = [] # List of titles for open positions
    locations_list = [] # List of locations available for the open positons (remote/on-site)
    descriptions_links_list = [] # Link to the full description of the position
    full_descriptions_list = [] # Full description of the positions

    # Dictionary to replace words/phrases in the full position description
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

    # Get listings from FullStack Labs site
    def getListings(self):
        # Open browser and go to URL
        self.driver = webdriver.Chrome()
        self.driver.get(self.SITE_URL)

        sleep(3)

        try:
            # Find elements for positions and links for full descriptions of the positions
            jobs = self.driver.find_elements(By.XPATH, self.JOBS_TITLES_ELEMENT_XPATH)
            description_links = self.driver.find_elements(By.XPATH, self.JOBS_FULL_DESC_BUTTON_ELEMENT_XPATH)

            # Temporary variables to store data and perform actions before moving it to the adecuate variables (defined above)
            temp_titles = []
            temp_desc_links = []
            repeated_positions = []

            # Get position text from element and store in temp var
            for i in range(len(jobs)):
                title = jobs[i].text
                temp_titles.append(title)

            # Get position full description link and store in temp var
            for i in range(len(description_links)):
                description_link = description_links[i].get_attribute("href")
                temp_desc_links.append(description_link)
            
            for i in range(0, len(temp_titles)):
                # If position include 'Latin America' in title add to temp var, if not, exclude
                if "Latin America" in temp_titles[i]:
                    # Exclude duplicated positions (website lists positions with the same exact name but for different cities)
                    if temp_titles[i] not in repeated_positions:
                        repeated_positions.append(temp_titles[i])
                        self.jobs_list.append(temp_titles[i].replace("- Remote ", "")) # Remove 'Remote' from title, all positions are remote
                        self.locations_list.append("Remote")
                        self.descriptions_links_list.append(temp_desc_links[i])

        except Exception as e:
            # In case of exception, show error in console
            print(f"Error while getting FullStack Labs listings: {e}")


    # Get position detailed description from URL scraped before
    def getDetailedDescriptions(self):
        try:
            # Loop through each link saved in previous step
            for i in range(0, len(self.descriptions_links_list)):
                print(f"- Getting job detailed description ({i+1}/{len(self.descriptions_links_list)}).")

                # Get link and navigate to URL
                desc_link = self.descriptions_links_list[i]
                self.driver.get(desc_link)
                
                sleep(2)

                try:
                    # Get the full description for the role
                    full_description = self.driver.find_element(By.XPATH, self.JOB_FULL_DESCRIPTION_ELEMENT_XPATH).text
                except Exception as e:
                    # In case of exception, show error in console and add the value "Unknown" to the list as placeholder
                    print(f"Error while getting full description: {desc_link} - Exception: {e}")
                    full_description = "Unknown."

                # Parse description to replace specific strings
                for word, replacement in self.replace_list.items():
                    full_description = full_description.replace(word, replacement).strip()

                # Append final full description to list
                self.full_descriptions_list.append(full_description)

                sleep(3)

        except Exception as e:
            # Throw error in case of general error
            print(f"Error while getting jobs detailed description: {e}")

    def getData(self):
        data = {
            "company": self.COMPANY_NAME,
            "job_list": self.jobs_list,
            "location_list": self.locations_list,
            "link_list": self.descriptions_links_list,
            "full_descriptions": self.full_descriptions_list
        }

        return data

scraper = FullStackLabs()
scraper.getListings()
scraper.getDetailedDescriptions()
scraper.generateOffers()