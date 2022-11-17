"""
Since UB's catalog page data is sourced from a public json file, we can use that to get the
catalog URLs for all the departments.

Source: https://catalog.buffalo.edu/courses/data/subjects.json
"""

from web_scraper.models.CatalogInfo import CatalogInfo
import requests
import json

class CatalogScraper:

    def get_catalog_urls(self):
        # Get the json data from the UB catalog page
        page = requests.get("https://catalog.buffalo.edu/courses/data/subjects.json")
        data = json.loads(page.content)

        # The json data is a list of dictionaries, where each dictionary contains the department
        # code, department name, and the URL of the department's catalog page in the following format:
        #
        # {"page": <dpt_name>, "url": <catalog_url>, "abbr": <dpt_code>}
        catalog_urls = []

        for dpt in data:
            url = "https://catalog.buffalo.edu/courses/" + dpt["url"]
            info = CatalogInfo(dpt["abbr"], dpt["page"], url)
            catalog_urls.append(info)

        return catalog_urls
