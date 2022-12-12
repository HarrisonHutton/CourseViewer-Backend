from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
from urllib.parse import quote_plus
import os

load_dotenv(find_dotenv())

# Get the username and password from the .env file and quote them for use in a URL
username = quote_plus(os.environ.get("MONGODB_USER"))
password = quote_plus(os.environ.get("CLUSTER_PWD"))

connection_string = f"mongodb+srv://{username}:{password}@course-viewer-data.fs1azkk.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string, tls=True, tlsAllowInvalidCertificates=True)

db = client["dev"]

courses_collection = db.course_collection

courses = courses_collection.find()

print(list(courses))