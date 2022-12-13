from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
from bson import json_util
from urllib.parse import quote_plus
from web_scraper.models.CourseInfo import CourseInfo
# Import the DatabaseEnum class from this same folder
from .DatabaseEnum import DatabaseEnum
import os


load_dotenv(find_dotenv())

# Get the username and password from the .env file and quote them for use in a URL
username = quote_plus(os.environ.get("MONGODB_USER"))
password = quote_plus(os.environ.get("CLUSTER_PWD"))

connection_string = f"mongodb+srv://{username}:{password}@course-viewer-data.fs1azkk.mongodb.net/?retryWrites=true&w=majority"

# Currently allowing invalid certificates to speed up development.
client = MongoClient(connection_string, tls=True, tlsAllowInvalidCertificates=True)

class CoursesDB:
    def __init__(self, db_name: DatabaseEnum):
        # Make sure sure that the database name is valid
        assert db_name in DatabaseEnum, "Invalid database name. Please use the DatabaseEnum class to select a database."
        # This will be the name of the database in our MongoDB cluster
        self.db = client[db_name.value]
        # This will be the name of the collection in our MongoDB database
        self.courses_collection = self.db.course_collection

    def __insert_course(self, course: CourseInfo):
        self.courses_collection.insert_one(course.to_dict())

    def insert_courses(self, courses: list[CourseInfo]):
        for course in courses:
            self.__insert_course(course)

    def get_all_courses(self):
        try:
            courses = self.courses_collection.find()
            courses = json_util.dumps(courses)
            return courses
        except:
            print("Error: Could not find any courses")
            return None

    def get_dept_courses(self, dpt_code: str):
        try:
            courses = self.courses_collection.find({"dpt_code": dpt_code})
            courses = json_util.dumps(courses)
            return courses
        except:
            print(f"Error: Could not find courses for department code: {dpt_code}")
            return None