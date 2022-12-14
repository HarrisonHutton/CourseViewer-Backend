"""
Scrape the catalog page for each department and get the department name and code.
"""

from web_scraper.models.DepartmentInfo import DepartmentInfo
from lxml import html
import requests

class DepartmentScraper:

    def get_department(self, url):
        # Get the html data from the department's catalog page.
        page = requests.get(url)
        tree = html.fromstring(page.content)

        # Get the department name and code from the html data.
        dpt_title = tree.xpath("//h1/text()")[0]

        dpt_name = dpt_title.split(" (")[0]
        dpt_code = dpt_title.split(" (")[1].split(")")[0]

        dpt_info = DepartmentInfo(dpt_name, dpt_code)

        return dpt_info
