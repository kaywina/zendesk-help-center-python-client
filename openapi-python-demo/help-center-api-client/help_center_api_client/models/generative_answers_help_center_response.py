from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.generative_answers_help_center_response_llm_confidence_level import (
    GenerativeAnswersHelpCenterResponseLlmConfidenceLevel,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generative_answers_help_center_response_source_contents_item import (
        GenerativeAnswersHelpCenterResponseSourceContentsItem,
    )


T = TypeVar("T", bound="GenerativeAnswersHelpCenterResponse")


@_attrs_define
class GenerativeAnswersHelpCenterResponse:
    """
    Attributes:
        answer_found (Union[Unset, bool]): Indicates if the query was solved.
        generated_answer (Union[Unset, str]): The generated answer for the query.
        generated_answer_formatted (Union[Unset, str]): The generated answer formatted for display in markdown.
        llm_confidence_level (Union[Unset, GenerativeAnswersHelpCenterResponseLlmConfidenceLevel]): Confidence level of
            the LLM in the generated answer.
        search_id (Union[Unset, str]): Id of the search query that used to get source contents.
        source_contents (Union[Unset, list['GenerativeAnswersHelpCenterResponseSourceContentsItem']]):
    """

    answer_found: Union[Unset, bool] = UNSET
    generated_answer: Union[Unset, str] = UNSET
    generated_answer_formatted: Union[Unset, str] = UNSET
    llm_confidence_level: Union[Unset, GenerativeAnswersHelpCenterResponseLlmConfidenceLevel] = UNSET
    search_id: Union[Unset, str] = UNSET
    source_contents: Union[Unset, list["GenerativeAnswersHelpCenterResponseSourceContentsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        answer_found = self.answer_found

        generated_answer = self.generated_answer

        generated_answer_formatted = self.generated_answer_formatted

        llm_confidence_level: Union[Unset, str] = UNSET
        if not isinstance(self.llm_confidence_level, Unset):
            llm_confidence_level = self.llm_confidence_level.value

        search_id = self.search_id

        source_contents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.source_contents, Unset):
            source_contents = []
            for source_contents_item_data in self.source_contents:
                source_contents_item = source_contents_item_data.to_dict()
                source_contents.append(source_contents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if answer_found is not UNSET:
            field_dict["answer_found"] = answer_found
        if generated_answer is not UNSET:
            field_dict["generated_answer"] = generated_answer
        if generated_answer_formatted is not UNSET:
            field_dict["generated_answer_formatted"] = generated_answer_formatted
        if llm_confidence_level is not UNSET:
            field_dict["llm_confidence_level"] = llm_confidence_level
        if search_id is not UNSET:
            field_dict["search_id"] = search_id
        if source_contents is not UNSET:
            field_dict["source_contents"] = source_contents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generative_answers_help_center_response_source_contents_item import (
            GenerativeAnswersHelpCenterResponseSourceContentsItem,
        )

        d = dict(src_dict)
        answer_found = d.pop("answer_found", UNSET)

        generated_answer = d.pop("generated_answer", UNSET)

        generated_answer_formatted = d.pop("generated_answer_formatted", UNSET)

        _llm_confidence_level = d.pop("llm_confidence_level", UNSET)
        llm_confidence_level: Union[Unset, GenerativeAnswersHelpCenterResponseLlmConfidenceLevel]
        if isinstance(_llm_confidence_level, Unset):
            llm_confidence_level = UNSET
        else:
            llm_confidence_level = GenerativeAnswersHelpCenterResponseLlmConfidenceLevel(_llm_confidence_level)

        search_id = d.pop("search_id", UNSET)

        source_contents = []
        _source_contents = d.pop("source_contents", UNSET)
        for source_contents_item_data in _source_contents or []:
            source_contents_item = GenerativeAnswersHelpCenterResponseSourceContentsItem.from_dict(
                source_contents_item_data
            )

            source_contents.append(source_contents_item)

        generative_answers_help_center_response = cls(
            answer_found=answer_found,
            generated_answer=generated_answer,
            generated_answer_formatted=generated_answer_formatted,
            llm_confidence_level=llm_confidence_level,
            search_id=search_id,
            source_contents=source_contents,
        )

        generative_answers_help_center_response.additional_properties = d
        return generative_answers_help_center_response

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
