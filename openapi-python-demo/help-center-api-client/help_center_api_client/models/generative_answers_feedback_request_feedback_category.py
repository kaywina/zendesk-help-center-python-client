from enum import Enum


class GenerativeAnswersFeedbackRequestFeedbackCategory(str, Enum):
    BROKEN_LINKS = "BROKEN_LINKS"
    FALSE_INFORMATION = "FALSE_INFORMATION"
    INCOMPLETE = "INCOMPLETE"
    IRRELEVANT = "IRRELEVANT"
    OTHER = "OTHER"
    POOR_FORMATTING = "POOR_FORMATTING"
    UNKNOWN_FEEDBACK = "UNKNOWN_FEEDBACK"
    WRONG_LANGUAGE = "WRONG_LANGUAGE"

    def __str__(self) -> str:
        return str(self.value)
