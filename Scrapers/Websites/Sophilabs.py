from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Sophilabs:

    COMPANY_NAME = "Sophilabs"
    SITE_URL = "https://sophilabs.com/careers" # Job listing website
    SHOW_ALL_POSITIONS_BUTTON_XPATH = "//span[text()='Show All Positions']" # 'Show all positions' button so page shows all available positions
    JOBS_TITLES_ELEMENT_XPATH = "//main//section//div//div//ul//li//a//h3" # XPATH for the position title element 
    JOBS_LOCATION_ELEMENT_XPATH = "//main//section//div//div//ul//li//a//h3//em" # XPATH for the position location element
    JOBS_FULL_DESCRIPTION_LINK_XPATH = "//main//section//div//div//ul//li//a" # XPATH for the position full description link
    JOB_FULL_DESCRIPTION_ELEMENT_XPATH = "//main//section//div//div[3]" # XPATH for full position description

    driver = "" # Chrome driver
    jobs_list = [] # List of titles for open positions
    locations_list = [] # List of locations available for the open positons (remote/on-site)
    descriptions_links_list = [] # Link to the full description of the position
    full_descriptions_list = [] # Full description of the positions

    # Dictionary to replace words/phrases in the full position description
    replace_list = {"If you share our commitment to delivering excellent client-focused service and putting customers first, enjoy working in teams, and are always looking to improve, join us!": "\nIf you share our commitment to delivering excellent client-focused service and putting customers first, enjoy working in teams, and are always looking to improve, join us!",
                    "A Typical Day": "\nA Typical Day:\n",
                    "Qualifications": "\nQualifications:\n",
                    "Preferred qualifications": "\nPreferred qualifications:\n",
                    "We offer": "\nWe offer:\n",
                    "Responsibilities for this position include, but are not limited to:": "\nResponsibilities for this position include, but are not limited to:\n",
                    "Responsibilities": "\nResponsibilities:\n",
                    "Preferred qualifications:\n:": "Preferred qualifications:\n", # In some cases the ":" is already present. This replacement is to avoid duplicating it.
                    "Qualifications:\n:": "Qualifications:\n", # In some cases the ":" is already present. This replacement is to avoid duplicating it.
                    "We offer:\n:": "We offer:\n"} # In some cases the ":" is already present. This replacement is to avoid duplicating it.

    def __init__(self):
        pass
    
    # Get listings from Sophilabs site
    def getListings(self):
        try:
            # Open browser
            self.driver = webdriver.Chrome()
            self.driver.get(self.SITE_URL)

            sleep(3)

            # Locate 'Show all positions' button and click it
            show_all = self.driver.find_element(By.XPATH, self.SHOW_ALL_POSITIONS_BUTTON_XPATH)
            show_all.click()

            sleep(2)

            # Locate elements for jobs, locations and description links using XPATH
            jobs = self.driver.find_elements(By.XPATH, self.JOBS_TITLES_ELEMENT_XPATH)
            locations = self.driver.find_elements(By.XPATH, self.JOBS_LOCATION_ELEMENT_XPATH)
            description_links = self.driver.find_elements(By.XPATH, self.JOBS_FULL_DESCRIPTION_LINK_XPATH)

            try:
                # Loop through all open positions found
                for i in range(0, len(jobs)):
                    print(f"- Getting job title ({i+1}/{len(jobs)}).")

                    full_job = jobs[i].text
                    title_and_location_list = full_job.split("\n") # full_job gets title AND location combined, splitting in order to get them separated

                    location = title_and_location_list[0].split(":")[0].title() # Job location (Remove countries)
                    title = title_and_location_list[1] # Job title
                    full_description_link = description_links[i].get_attribute("href") # Get position full description link

                    # Append data to lists 
                    self.jobs_list.append(title)
                    self.locations_list.append(location)
                    self.descriptions_links_list.append(full_description_link)

                    print(f"Title: {title} // Location: {location} // Link: {full_description_link}")
                    
                    
            except Exception as e:
                print(f"Error while trying to retrieve listings: {e}")
        except Exception as e:
            print(f"General error: {e}")

    
    def getDetailedDescriptions(self):
        try:
            # Loop through full descriptions links list
            for i in range(0, len(self.descriptions_links_list)):
                print(f"- Getting job detailed description ({i+1}/{len(self.descriptions_links_list)}).")

                # Get link and open it
                desc_link = self.descriptions_links_list[i]
                self.driver.get(desc_link)

                sleep(3)

                # Get job description by using XPATH. Log error and add "Unknown" placeholder to descriptions list in case it fails.
                try:
                    full_description = self.driver.find_element(By.XPATH, self.JOB_FULL_DESCRIPTION_ELEMENT_XPATH).text
                except Exception as e:
                    print(f"Error while getting full description: {desc_link} - Exception: {e}")
                    full_description = "Unknown."

                # Parse description to replace specific strings
                for word, replacement in self.replace_list.items():
                    full_description = full_description.replace(word, replacement)
                
                # Add description to list
                self.full_descriptions_list.append(full_description)

                '''

                TO DO: REMOVE THIS WRITE TO FILE, ONLY USED TO DEBUG.

                '''
                with open(f"{i+1}.txt", "a", encoding="utf-8") as file:
                        file.write(full_description)

                sleep(3)
        except Exception as e:
            print(f"Error while getting jobs detailed description: {e}")

    def generateOffers(self):
        '''
        
        TO DO: Once all position listings are scraped, generate Offers and upload to site.

        '''

    def start(self):
        self.getListings()
        self.getDetailedDescriptions()
        self.generateOffers()            


'''
scraper = Sophilabs()
scraper.getListings()
scraper.getDetailedDescriptions()
scraper.generateOffers()
scraper.start()
'''

scraper = Sophilabs()
scraper.start()