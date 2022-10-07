from dataclasses import dataclass

@dataclass
class CourseInfo:
    dpt_code: str
    course_num: str
    course_name: str
    course_type: str
    course_description: str
    credits: str
    grading: str
    typically_offered: str
    requisites: str