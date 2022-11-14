from enum import Enum

class DatabaseEnum(Enum):
    DEV = "dev"
    PROD = "prod"

    def get_members(self):
        return [member.value for member in self.__class__]