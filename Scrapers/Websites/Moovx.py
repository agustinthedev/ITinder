from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Moovx:

    SITE_URL = "https://moovx.mobi/careers/" # Job listing website 
    JOBS_TITLES_ELEMENT_XPATH = "//div[@id='jobs']//div[@onmouseout=\"this.style.background='#FFFFFF'\"]//div[@class=\"col-5\"]//p" # XPATH for the position title element
    JOBS_LOCATION_ELEMENT_XPATH = "//div[@id='jobs']//div[@onmouseout=\"this.style.background='#FFFFFF'\"]//div[@class=\"col-4\"]//p" # XPATH for the position location element
    JOBS_FULL_DESC_BUTTON_ELEMENT_XPATH = "//div[@id='jobs']//div[@onmouseout=\"this.style.background='#FFFFFF'\"]//div[@class=\"col-3\"]//a" # XPATH for the position full description link
    JOB_FULL_DESCRIPTION_ELEMENT_XPATH = "//div[@id=\"job-details\"] | //div[@id=\"content\"]" # XPATH for full position description

    driver = ""
    jobs_list = []
    locations_list = []
    descriptions_links_list = []
    full_descriptions_list = []

    replace_list = {"👨‍💻 Apply and start now!": "\n👨‍💻 Apply and start now!",
                    "Who we are": "\nWho we are:\n",
                    "What are you going to do?": "\nWhat are you going to do?\n",
                    "At Moovx we have always believed People are our top priority. ": "\nAt Moovx we have always believed People are our top priority. \n",
                    "Fair decisions, free of bias:": "\nFair decisions, free of bias:\n",
                    "What we offer": "\nWhat we offer:\n",
                    "Qualifications": "\nQualifications:\n",
                    "Responsibilities": "\nResponsibilities:\n",
                    "We expect you to bring your experience working with": "\nWe expect you to bring your experience working with:\n",
                    "About the project": "\nAbout the project:\n",
                    "Required qualifications": "\nRequired qualifications\n",
                    "Even better if you have": "\nEven better if you have:\n",
                    "Your skills and experience should be": "\nYour skills and experience should be:\n",
                    "About the position": "\nAbout the position:\n",
                    "ESSENTIAL FUNCTIONS AND RESPONSIBILITIES": "\nESSENTIAL FUNCTIONS AND RESPONSIBILITIES:\n",
                    "QUALIFICATIONS": "\n\nQUALIFICATIONS:\n",
                    "Must Have": "\nMust Have:\n",
                    "Nice to have": "\nNice to have:\n",
                    "Extra project info": "\nExtra project info:\n",
                    "Requirements": "\nRequirements:\n",
                    "About the role": "\nAbout the role:\n",
                    "What are we looking for?": "\nWhat are we looking for?\n",
                    "That's why we work every day on developing a company culture which reflects how we value our people:": "That's why we work every day on developing a company culture which reflects how we value our people:\n"}

    def __init__(self):
        pass

    def getListings(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.SITE_URL)

        sleep(3)

        try:
            jobs = self.driver.find_elements(By.XPATH, self.JOBS_TITLES_ELEMENT_XPATH)
            locations = self.driver.find_elements(By.XPATH, self.JOBS_LOCATION_ELEMENT_XPATH)
            descriptions_links = self.driver.find_elements(By.XPATH, self.JOBS_FULL_DESC_BUTTON_ELEMENT_XPATH)

            for i in range(0, len(jobs)):
                print(f"- Getting job title ({i+1}/{len(jobs)}).")
                job = jobs[i]

                try:
                    self.jobs_list.append(job.text)
                except Exception as e:
                    print(f"Error while appending job title: {job} - Exception: {e}")
                    self.jobs_list.append("Unknown.")

            for i in range(0, len(locations)):
                print(f"- Getting job location ({i+1}/{len(locations)}).")
                location = locations[i]

                try:
                    self.locations_list.append(location.text)
                except Exception as e:
                    print(f"Error while appending location: {location} - Exception: {e}")

            for i in range(0, len(descriptions_links)):
                print(f"- Getting job description link: ({i+1}/{len(descriptions_links)}).")
                description_link = descriptions_links[i]

                try:
                    self.descriptions_links_list.append(description_link.get_attribute('href').replace(";", ""))
                except Exception as e:
                    print(f"Error while appending listing url: {description_link} - Exception {e}")

        except Exception as e:
            print(f"Error while getting jobs listing: {e}")
        
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

                #full_description_parsed = self.parseDescription(full_description) # Parse description to replace specific strings
                for word, replacement in self.replace_list.items():
                    full_description = full_description.replace(word, replacement)

                self.full_descriptions_list.append(full_description)

                with open(f"{i+1}.txt", "a", encoding="utf-8") as file:
                    file.write(full_description)

                sleep(3)
        except Exception as e:
            pass

    def printListings(self):
        for i in range(0, len(self.jobs_list)):
            print(f"{self.jobs_list[i]} // {self.locations_list[i]} // {self.descriptions_links_list[i]}")
    

scraper = Moovx()
scraper.getListings()
scraper.printListings()
scraper.getDetailedDescriptions()
