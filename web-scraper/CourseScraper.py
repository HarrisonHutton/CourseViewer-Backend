"""
Get the course data from a given department catalog page. The data is returned as a list of CourseInfo objects.
"""

from models.CourseInfo import CourseInfo, CourseTitle
from lxml import html
import requests
import json

class CourseScraper:

    def __init__(self):
        # We'll use the data in this json file as a map between the (<= 3-character) course types
        # to their corresponding real names.
        with open("course_types.json") as f:
            self.course_types = json.load(f)

    def get_course_data(self, url):
        # Get the HTML from the page
        page = requests.get(url)
        tree = html.fromstring(page.content)

        # UB's course catalogs are set up with two accordions.
        # The first accordion contains "The Learning Environment".
        # The second accordion contains the actual courses and their information.
        accordions = tree.xpath('//ul[@class="accordion"]')

        # Since we only want the courses, we'll get the second accordion.
        course_elements = accordions[1].xpath('.//li')

        for course in course_elements:
            name_info: CourseTitle = self.__get_course_name(course)
            print(name_info)
            
            

    """
    Private method that returns a CourseTitle object given an lxml.html.HtmlElement representing
    all the information of a course.
    """
    def __get_course_name(self, course: html.HtmlElement):
        # The return value of the xpath call is a list with one element, so we'll just 
        # grab the first element immediately.
        full_course_name = course.xpath('a/text()')[0]

        # The course name is formatted as:
        # "<department code> <course number><course type> <course name>"
        #
        # The department code is a variable number of characters.
        # The course number is exactly 3 digits long.
        # The course type is a variable number of characters.
        # The course name is a variable number of characters.
        #
        # For example:
        # "CSE 250LR Data Structures"

        # First, we'll split the course name by spaces.
        course_name_parts = full_course_name.split()

        # Now extract the relevant information from the course_name_parts list.

        # The department code is simply the first element in the list.
        dpt_code = course_name_parts[0]

        # The course number is the first 3 characters of the second element in the list
        course_num = course_name_parts[1][:3]

        # The course type is the everything following the first 3 characters of the second element
        # in the list.
        course_type = self.course_types[course_name_parts[1][3:]]

        # Now, since we split by spaces earlier, we have to join the course name back together to 
        # account for spaces in the name.
        course_name = ' '.join(course_name_parts[2:])

        # Finally, return a CourseTitle object containing the relevant information.
        return CourseTitle(dpt_code, course_num, course_type, course_name)

    