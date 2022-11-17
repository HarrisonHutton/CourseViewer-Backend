from database.CoursesDB import CoursesDB
from database.DatabaseEnum import DatabaseEnum
from web_scraper.models.CourseInfo import CourseInfo

courses_db = CoursesDB(DatabaseEnum.DEV)

# Create 5 different courses in the format of a CourseInfo object
courses = [
    CourseInfo("CSE", "101", "Introduction to Computer Science", "LEC", "Lecture", "This is a course about computers.", "3", "Letter", ["Fall", "Spring"]),
    CourseInfo("CSE", "102", "Introduction to Computer Science II", "LEC", "Lecture", "This is a course about computers.", "3", "Letter", ["Fall", "Spring"]),
    CourseInfo("CSE", "103", "Introduction to Computer Science III", "LEC", "Lecture", "This is a course about computers.", "3", "Letter", ["Fall", "Spring"]),
    CourseInfo("CSE", "104", "Introduction to Computer Science IV", "LEC", "Lecture", "This is a course about computers.", "3", "Letter", ["Fall", "Spring"]),
    CourseInfo("CSE", "105", "Introduction to Computer Science V", "LEC", "Lecture", "This is a course about computers.", "3", "Letter", ["Fall", "Spring"]),
]

# Insert the courses into the database
courses_db.insert_courses(courses)
