"""
Get the course data from a given department catalog page. The data is returned as a list of CourseInfo objects.
"""

from models.CourseInfo import CourseInfo, CourseTitle, CourseDescription
from lxml import html
import requests
import json

class CourseScraper:

    def __init__(self):
        # We'll use the data in this json file as a map between the (<= 3-character) course types
        # to their corresponding real names.
        with open("course_types.json") as f:
            self.course_types = json.load(f)

    """
    Get a list of CourseInfo objects from a given department catalog page.
    """
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

        courses = []

        for course in course_elements:
            name_info: CourseTitle = self.__get_course_name(course)
            course_description = self.__get_course_description(course)

            info = CourseInfo(
                name_info.dpt_code,
                name_info.course_num,
                name_info.course_type,
                name_info.course_name,
                course_description.course_description,
                course_description.credits,
                course_description.grading,
                course_description.typically_offered,
                course_description.requisites
            )

            courses.append(info)

        return courses
            
            

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

    """
    Private method that returns a CourseDescription object given an lxml.html.HtmlElement representing all the information of a course.
    """
    def __get_course_description(self, course: html.HtmlElement):
        # First, grab the course description element.
        course_description_element = course.xpath('div[@class="accordion-content"]')[0]

        # The actual description is in the first paragraph element inside this element.
        # We use the text_content() method to get the text of the description without any markup to
        # account for the cases where the description contains HTML tags.
        course_description = course_description_element.xpath('p[@class="course-description"]')[0].text_content()

        # The credits, grading, typically offered, and requisites information is in the inner HTML of
        # the only div following the course description paragraph.
        # So the value below is just a string containing all of this information.
        course_props = course_description_element.xpath('div')[0].text_content()

        # Since all of this information is in one string, we'll have to parse it to get the individual
        # pieces of information. 
        # We'll find the indices of the following substrings and then do math to get to the 
        # relevant data they address:
        #     "Credits:"
        #     "Grading:"
        #     "Typically Offered:"
        #     "Requisites:"
        # The final substring "Requisites:" is optional, so we'll have to check if it exists.
        # If it doesn't, then we'll just use the length of the string as the index of the end of the
        # requisites information.

        # First, we'll find the indices of the substrings.
        credits_index = course_props.find("Credits:")
        grading_index = course_props.find("Grading:")
        typically_offered_index = course_props.find("Typically Offered:")
        requisites_index = course_props.find("Requisites:")

        # Now we'll do some math to get the relevant information.

        # Afterwards we'll strip the whitespace from the beginning and end of the string.

        # The credits information is between the "Credits:" substring and the "Grading:" substring.
        credits = course_props[credits_index + len("Credits:"):grading_index].strip()

        # The grading information is between the "Grading:" substring and the "Typically Offered:" 
        # substring.
        grading = course_props[grading_index + len("Grading:"):typically_offered_index].strip()

        # The typically offered information is between the "Typically Offered:" substring and the 
        # "Requisites:" substring.
        #
        # If the "Requisites:" substring doesn't exist, then we'll just use the length of the 
        # string as the index.

        if requisites_index == -1:
            typically_offered = course_props[typically_offered_index + len("Typically Offered:"):].strip()
        else:
            typically_offered = course_props[typically_offered_index + len("Typically Offered:"):requisites_index].strip()

        # Convert the typically offered string to a list of strings without spaces
        typically_offered = typically_offered.split(', ')

        # The requisites information is between the "Requisites:" substring and the end of the string.
        #
        # If the "Requisites:" substring doesn't exist, then we'll just use an empty string as the
        # requisites information.
        if requisites_index == -1:
            requisites = ""
        else:
            requisites = course_props[requisites_index + len("Requisites:"):].strip()

        return CourseDescription(
            course_description, 
            credits, 
            grading, 
            typically_offered, 
            requisites
        )