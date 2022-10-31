from dataclasses import dataclass

@dataclass
class CourseInfo:
    dpt_code: str
    course_num: str
    course_type: str
    course_name: str
    course_description: str
    credits: str
    grading: str
    typically_offered: list[str]
    requisites: str = None

@dataclass
class CourseTitle:
    dpt_code: str
    course_num: str
    course_type: str
    course_name: str

@dataclass
class CourseDescription:
    course_description: str
    credits: str
    grading: str
    typically_offered: list[str]
    requisites: str = None