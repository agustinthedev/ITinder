from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Offers import Offer

class Switch:

    COMPANY_NAME = "Switch Software Solutions"
    SITE_URL = "https://switch.hiringroom.com/jobs"
    JOBS_TITLES_ELEMENT_XPATH = ""
    JOBS_LOCATION_ELEMENT_XPATH = ""
    JOBS_FULL_DESCRIPTION_LINK_XPATH = ""
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
        pass

    def getDetailedDescriptions(self):
        pass

    def generateOffers(self):
        pass

    def start(self):
        self.getListings()
        self.getDetailedDescriptions()
        self.generateOffers