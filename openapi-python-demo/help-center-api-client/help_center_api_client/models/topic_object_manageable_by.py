from enum import Enum


class TopicObjectManageableBy(str, Enum):
    MANAGERS = "managers"
    STAFF = "staff"

    def __str__(self) -> str:
        return str(self.value)
