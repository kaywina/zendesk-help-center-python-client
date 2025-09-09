from enum import Enum


class ListUserSubscriptionsByUserIdType(str, Enum):
    FOLLOWERS = "followers"
    FOLLOWINGS = "followings"

    def __str__(self) -> str:
        return str(self.value)
