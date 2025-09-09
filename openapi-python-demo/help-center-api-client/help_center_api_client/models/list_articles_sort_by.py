from enum import Enum


class ListArticlesSortBy(str, Enum):
    CREATED_AT = "created_at"
    POSITION = "position"
    TITLE = "title"
    UPDATED_AT = "updated_at"

    def __str__(self) -> str:
        return str(self.value)
