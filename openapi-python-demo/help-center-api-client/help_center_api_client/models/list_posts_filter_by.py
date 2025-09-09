from enum import Enum


class ListPostsFilterBy(str, Enum):
    ANSWERED = "answered"
    COMPLETED = "completed"
    NONE = "none"
    NOT_PLANNED = "not_planned"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
