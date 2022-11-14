from dataclasses import dataclass

@dataclass
class CourseInfo:
    dpt_code: str
    course_num: str
    course_name: str
    course_type_abbr: str
    course_type: str
    course_description: str
    credits: str
    grading: str
    typically_offered: list[str]
    requisites: str = None

    """
    Create a dictionary from the CourseInfo object.
    """
    def to_dict(self):
        return {
            "dpt_code": self.dpt_code,
            "course_num": self.course_num,
            "course_name": self.course_name,
            "course_type_abbr": self.course_type_abbr,
            "course_type": self.course_type,
            "course_description": self.course_description,
            "credits": self.credits,
            "grading": self.grading,
            "typically_offered": self.typically_offered,
            "requisites": self.requisites,
        }

@dataclass
class CourseTitle:
    dpt_code: str
    course_num: str
    course_name: str
    course_type_abbr: str

@dataclass
class CourseDescription:
    course_type: str
    course_description: str
    credits: str
    grading: str
    typically_offered: list[str]
    requisites: str = None