from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Util import Offers

class FullStackLabs:

    COMPANY_NAME = "FullStackLabs"
    SITE_URL = "https://jobs.lever.co/fullstacklabs/?workplaceType=remote"
    JOBS_TITLES_ELEMENT_XPATH = ""
    JOBS_LOCATION_ELEMENT_XPATH = ""
    JOBS_FULL_DESC_BUTTON_ELEMENT_XPATH = ""
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
        pass