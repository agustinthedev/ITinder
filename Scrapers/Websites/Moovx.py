from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def parse_description(text):
    text.replace("Who we are", "\n\nWho we are\n\n")
    text.replace("What are you going to do?", "\n\nWhat are you going to do?\n\n")
    text.replace("We expect you to bring", "\n\nWe expect you to bring\n\n")
    text.replace("At Moovx we have always believed People are our top priority. ", "\n\nAt Moovx we have always believed People are our top priority. \n\n")
    text.replace("Fair decisions, free of bias:", "\n\nFair decisions, free of bias:\n\n")
    text.replace("What we offer", "\n\nWhat we offer\n\n")
    text.replace("Qualifications", "\n\nQualifications\n\n")
    text.replace("Responsibilities", "\n\nResponsibilities\n\n")
    text.replace("We expect you to bring your experience working with", "\n\nWe expect you to bring your experience working with\n\n")
    text.replace("About the project", "\n\nAbout the project\n\n")
    text.replace("Required qualifications", "\n\nRequired qualifications\n\n")
    text.replace("Even better if you have", "\n\nEven better if you have\n\n")
    text.replace("Your skills and experience should be", "\n\nYour skills and experience should be\n\n")
    text.replace("About the position", "\n\nAbout the position\n\n")
    text.replace("ESSENTIAL FUNCTIONS AND RESPONSIBILITIES", "\n\nESSENTIAL FUNCTIONS AND RESPONSIBILITIES\n\n")
    text.replace("QUALIFICATIONS", "\n\nQUALIFICATIONS\n\n")
    text.replace("Must Have", "\n\nMust Have\n\n")
    text.replace("Nice to have", "\n\nNice to have\n\n")
    text.replace("Extra project info", "\n\nExtra project info\n\n")
    text.replace("Requirements", "\n\nRequirements\n\n")
    text.replace("About the role", "\n\nAbout the role\n\n")
    text.replace("What are we looking for?", "\n\nWhat are we looking for?\n\n")

SITE_URL = "https://moovx.mobi/careers/"
JOBS_TITLES_ELEMENT_XPATH = "//div[@id='jobs']//div[@onmouseout=\"this.style.background='#FFFFFF'\"]//div[@class=\"col-5\"]//p"
JOBS_LOCATION_ELEMENT_XPATH = "//div[@id='jobs']//div[@onmouseout=\"this.style.background='#FFFFFF'\"]//div[@class=\"col-4\"]//p"
JOBS_FULL_DESC_BUTTON_ELEMENT_XPATH = "//div[@id='jobs']//div[@onmouseout=\"this.style.background='#FFFFFF'\"]//div[@class=\"col-3\"]//a"
JOB_FULL_DESCRIPTION_ELEMENT_XPATH = "//div[@id=\"job-details\"] | //div[@id=\"content\"]"

driver = webdriver.Chrome()
driver.get(SITE_URL)

jobs_list = []
locations_list = []
descriptions_links_list = []
full_descriptions_list = []

jobs = driver.find_elements(By.XPATH, JOBS_TITLES_ELEMENT_XPATH)
locations = driver.find_elements(By.XPATH, JOBS_LOCATION_ELEMENT_XPATH)
descriptions_links = driver.find_elements(By.XPATH, JOBS_FULL_DESC_BUTTON_ELEMENT_XPATH)

for job in jobs: jobs_list.append(job.text)
for location in locations: locations_list.append(location.text)
for description_link in descriptions_links: descriptions_links_list.append(description_link.get_attribute('href').replace(";", ""))

for i in range(0, len(descriptions_links_list)):
    desc_link = descriptions_links_list[i]
    driver.get(desc_link)

    print(f"Scraping URL: {desc_link}")
    sleep(2)

    full_description = driver.find_element(By.XPATH, JOB_FULL_DESCRIPTION_ELEMENT_XPATH).text
    full_descriptions_list.append(full_description)

    with open(f"{i}", "a", encoding="utf-8") as file:
        file.write(full_description)

    sleep(3)

for i in range(0, len(jobs)): print(f"{jobs_list[i]} - {locations_list[i]} - {descriptions_links_list[i]}")
