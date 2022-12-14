# Import course_data.py and call get_course_data() with the URL of a department catalog page.

from web_scraper.CourseScraper import CourseScraper
from web_scraper.CatalogScraper import CatalogScraper   
from web_scraper.DepartmentScraper import DepartmentScraper

scraper = CourseScraper()

catalog_scraper = CatalogScraper()
catalog_urls = catalog_scraper.get_catalog_urls()

department_scraper = DepartmentScraper()

# Print ever single course that UB offers in the following format:
#
# <dpt_code> <course_num> <course_type> <course_name>

for url in catalog_urls:
    department_scraper.get_department(url.catalog_url)
    # courses = scraper.get_course_data(url.catalog_url)
    # for course in courses:
    #     print(course.dpt_code, course.course_num, course.course_type, course.course_name)