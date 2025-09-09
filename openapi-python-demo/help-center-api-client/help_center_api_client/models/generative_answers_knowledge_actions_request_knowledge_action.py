from enum import Enum


class GenerativeAnswersKnowledgeActionsRequestKnowledgeAction(str, Enum):
    COPIED_TO_CONVERSATION = "COPIED_TO_CONVERSATION"

    def __str__(self) -> str:
        return str(self.value)
