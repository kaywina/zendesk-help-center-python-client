from enum import Enum


class UnifiedSearchResultType(str, Enum):
    ARTICLE = "ARTICLE"
    EXTERNAL_RECORD = "EXTERNAL_RECORD"
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
