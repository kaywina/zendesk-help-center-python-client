from enum import Enum


class GenerativeAnswersKnowledgeResponseLlmConfidenceLevel(str, Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    NORMAL = "NORMAL"
    VERY_HIGH = "VERY_HIGH"
    VERY_LOW = "VERY_LOW"

    def __str__(self) -> str:
        return str(self.value)
