from enum import Enum


class SectionPutRequestSectionSorting(str, Enum):
    CREATION_ASC = "creation_asc"
    CREATION_DESC = "creation_desc"
    MANUAL = "manual"
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
