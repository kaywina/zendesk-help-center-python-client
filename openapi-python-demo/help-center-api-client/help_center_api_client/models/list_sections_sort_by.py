from enum import Enum


class ListSectionsSortBy(str, Enum):
    CREATED_AT = "created_at"
    POSITION = "position"
    UPDATED_AT = "updated_at"

    def __str__(self) -> str:
        return str(self.value)
