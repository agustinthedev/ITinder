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

        query = "SELECT id FROM job_listings WHERE link=%s"

        self.cursor.execute(query, (link,))       
        row = self.cursor.fetchone()

        if row is None:
            print("Doesn't exist")

            insert_query = "INSERT INTO job_listings (id, company, title, location, link, description) VALUES (NULL, %s, %s, %s, %s, %s)"
            insert_values = (company, title, location, link, description)

            self.cursor.execute(insert_query, insert_values)
            self.db.commit()

            print("Inserted one unique value")
        else:
            print(f"{link} already exists in database ")

        #print("Inserted new job listing into 'job_listings' table.")

    def getListings(self):
        pass

    def removeListing(self, link):
        pass