from dotenv import load_dotenv, find_dotenv
import os
import mysql.connector

class Database:

    db = ""
    cursor = ""

    def __init__(self):
        load_dotenv(find_dotenv())
        self.db = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),
            user = os.getenv("DB_USER"),
            passwd = os.getenv("DB_PASSWD"),
            database = os.getenv("DB_DATABASE")
        )

        self.cursor = self.db.cursor()

    def addListing(self, company, title, location, link, description):
        #query = "INSERT INTO job_listings (id, company, title, location, link, description) VALUES (NULL, %s, %s, %s, %s, %s)"
        #values = (company, title, location, link, description)

        query = "SELECT id FROM job_listings WHERE link = 'https://jobs.lever.co/fullstacklabs/ac6e1b5f-2ad5-4564-baac-cf1489a1f23d'"

        self.cursor.execute(query)

        for x in self.cursor:
            print(x)
        #self.db.commit()

        #print("Inserted new job listing into 'job_listings' table.")

    def getListings(self):
        pass

    def removeListing(self, link):
        pass

db = Database()
db.addListing("Google", "QA", "Remote", "https://jobs.lever.co/fullstacklabs/ac6e1b5f-2ad5-4564-baac-cf1489a1f23d", "test")