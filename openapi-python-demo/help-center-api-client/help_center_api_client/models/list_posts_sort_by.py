from enum import Enum


class ListPostsSortBy(str, Enum):
    COMMENTS = "comments"
    CREATED_AT = "created_at"
    EDITED_AT = "edited_at"
    RECENT_ACTIVITY = "recent_activity"
    UPDATED_AT = "updated_at"
    VOTES = "votes"

    def __str__(self) -> str:
        return str(self.value)
