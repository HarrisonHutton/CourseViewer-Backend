from dataclasses import dataclass

@dataclass
class DepartmentInfo:
    dpt_name: str
    dpt_code: str

    """
    Create a dictionary from the DepartmentInfo object.
    """
    def to_dict(self):
        return {
            "dpt_name": self.dpt_name,
            "dpt_code": self.dpt_code,
        }