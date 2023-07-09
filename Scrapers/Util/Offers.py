from .DB import Database

class Offer:
    OFFER_COMPANY = ""
    OFFER_TITLE = ""
    OFFER_LOCATION = "Unknown" # Default position location is Unknown
    OFFER_LINK = ""
    OFFER_DESCRIPTION = ""

    def __init__(self, company, title, location, link, description):
        self.OFFER_COMPANY = company
        self.OFFER_TITLE = title
        self.OFFER_LOCATION = location
        self.OFFER_LINK = link
        self.OFFER_DESCRIPTION = description

    def loadOffer(self):
        database = Database()
        database.addListing(self.OFFER_COMPANY, self.OFFER_TITLE, self.OFFER_LOCATION, self.OFFER_LINK, self.OFFER_DESCRIPTION)