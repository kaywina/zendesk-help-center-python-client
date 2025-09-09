from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.generative_answers_feedback_request_channel import GenerativeAnswersFeedbackRequestChannel
from ..models.generative_answers_feedback_request_feedback_category import (
    GenerativeAnswersFeedbackRequestFeedbackCategory,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerativeAnswersFeedbackRequest")


@_attrs_define
class GenerativeAnswersFeedbackRequest:
    """
    Attributes:
        channel (GenerativeAnswersFeedbackRequestChannel): The channel where the answer was generated.
        is_helpful (bool): Indicates if the generated answer was helpful.
        search_id (str): The ID of the search query that was used to generate the answer.
        feedback_category (Union[Unset, GenerativeAnswersFeedbackRequestFeedbackCategory]): Category of the feedback.
        text_feedback (Union[Unset, str]): Additional text feedback provided by the user.
    """

    channel: GenerativeAnswersFeedbackRequestChannel
    is_helpful: bool
    search_id: str
    feedback_category: Union[Unset, GenerativeAnswersFeedbackRequestFeedbackCategory] = UNSET
    text_feedback: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel.value

        is_helpful = self.is_helpful

        search_id = self.search_id

        feedback_category: Union[Unset, str] = UNSET
        if not isinstance(self.feedback_category, Unset):
            feedback_category = self.feedback_category.value

        text_feedback = self.text_feedback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel": channel,
                "is_helpful": is_helpful,
                "search_id": search_id,
            }
        )
        if feedback_category is not UNSET:
            field_dict["feedback_category"] = feedback_category
        if text_feedback is not UNSET:
            field_dict["text_feedback"] = text_feedback

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = GenerativeAnswersFeedbackRequestChannel(d.pop("channel"))

        is_helpful = d.pop("is_helpful")

        search_id = d.pop("search_id")

        _feedback_category = d.pop("feedback_category", UNSET)
        feedback_category: Union[Unset, GenerativeAnswersFeedbackRequestFeedbackCategory]
        if isinstance(_feedback_category, Unset):
            feedback_category = UNSET
        else:
            feedback_category = GenerativeAnswersFeedbackRequestFeedbackCategory(_feedback_category)

        text_feedback = d.pop("text_feedback", UNSET)

        generative_answers_feedback_request = cls(
            channel=channel,
            is_helpful=is_helpful,
            search_id=search_id,
            feedback_category=feedback_category,
            text_feedback=text_feedback,
        )

        generative_answers_feedback_request.additional_properties = d
        return generative_answers_feedback_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
