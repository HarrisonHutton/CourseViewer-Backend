"""
Scrape the entire UB catalog using the catalog scraper and course scraper objects
and insert every course as a dictionary into the database using the CoursesDB object.
"""
from database.CoursesDB import CoursesDB
from database.DatabaseEnum import DatabaseEnum
from web_scraper.models.CourseInfo import CourseInfo
from web_scraper.CatalogScraper import CatalogScraper
from web_scraper.CourseScraper import CourseScraper

def test_full_catalog_insert():
    # Create a CoursesDB object to insert the courses into the database.
    courses_db = CoursesDB(DatabaseEnum.DEV)

    # Create a CatalogScraper object to scrape UB's department list.
    catalog_scraper = CatalogScraper()

    # Create a CourseScraper object to scrape each course's information from each department's
    # course catalog.
    course_scraper = CourseScraper()

    # Get a list of all the department catalog URLs.
    catalog_urls = catalog_scraper.get_catalog_urls()

    # For each catalog URL, scrape the course data and insert it into the database.
    for url in catalog_urls:
        courses: list[CourseInfo] = course_scraper.get_course_data(url.catalog_url)
        # Insert the courses into the database.
        courses_db.insert_courses(courses)

if __name__ == "__main__":
    test_full_catalog_insert()