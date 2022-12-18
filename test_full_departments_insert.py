"""
Scrape the entire UB catalog using the catalog scraper and department scraper objects
and insert every department as a dictionary into the database using the CoursesDB object.
"""
from database.CoursesDB import CoursesDB
from database.DatabaseEnum import DatabaseEnum
from web_scraper.DepartmentScraper import DepartmentScraper
from web_scraper.CatalogScraper import CatalogScraper
from web_scraper.models.DepartmentInfo import DepartmentInfo

def test_full_departments_insert():
    # Create a CoursesDB object to insert the courses into the database.
    courses_db = CoursesDB(DatabaseEnum.DEV)

    # Create a CatalogScraper object to scrape UB's department list.
    catalog_scraper = CatalogScraper()

    # Create a DepartmentScraper object to scrape each department's information from the catalog.
    department_scraper = DepartmentScraper()

    # Get a list of all the department catalog URLs.
    catalog_urls = catalog_scraper.get_catalog_urls()

    dpts: list[DepartmentInfo] = []

    # For each catalog URL, scrape the course data and insert it into the database.
    for url in catalog_urls:
        dpt: DepartmentInfo = department_scraper.get_department(url.catalog_url)
        dpts.append(dpt)

    courses_db.insert_departments(dpts)

if __name__ == "__main__":
    test_full_departments_insert()