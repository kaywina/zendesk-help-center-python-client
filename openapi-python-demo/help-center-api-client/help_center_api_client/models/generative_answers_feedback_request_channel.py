from enum import Enum


class GenerativeAnswersFeedbackRequestChannel(str, Enum):
    AGENT_WORKSPACE = "AGENT_WORKSPACE"
    HELP_CENTER = "HELP_CENTER"
    VOICE_COPILOT = "VOICE_COPILOT"

    def __str__(self) -> str:
        return str(self.value)
