from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.generative_answers_knowledge_response_llm_confidence_level import (
    GenerativeAnswersKnowledgeResponseLlmConfidenceLevel,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generative_answers_knowledge_response_source_contents_item import (
        GenerativeAnswersKnowledgeResponseSourceContentsItem,
    )


T = TypeVar("T", bound="GenerativeAnswersKnowledgeResponse")


@_attrs_define
class GenerativeAnswersKnowledgeResponse:
    """
    Attributes:
        answer (Union[Unset, str]): The generated answer for the query.
        llm_confidence_level (Union[Unset, GenerativeAnswersKnowledgeResponseLlmConfidenceLevel]): Confidence level of
            the LLM in the generated answer.
        solved (Union[Unset, bool]): Indicates if the query was solved.
        source_contents (Union[Unset, list['GenerativeAnswersKnowledgeResponseSourceContentsItem']]):
    """

    answer: Union[Unset, str] = UNSET
    llm_confidence_level: Union[Unset, GenerativeAnswersKnowledgeResponseLlmConfidenceLevel] = UNSET
    solved: Union[Unset, bool] = UNSET
    source_contents: Union[Unset, list["GenerativeAnswersKnowledgeResponseSourceContentsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        answer = self.answer

        llm_confidence_level: Union[Unset, str] = UNSET
        if not isinstance(self.llm_confidence_level, Unset):
            llm_confidence_level = self.llm_confidence_level.value

        solved = self.solved

        source_contents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.source_contents, Unset):
            source_contents = []
            for source_contents_item_data in self.source_contents:
                source_contents_item = source_contents_item_data.to_dict()
                source_contents.append(source_contents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if answer is not UNSET:
            field_dict["answer"] = answer
        if llm_confidence_level is not UNSET:
            field_dict["llm_confidence_level"] = llm_confidence_level
        if solved is not UNSET:
            field_dict["solved"] = solved
        if source_contents is not UNSET:
            field_dict["source_contents"] = source_contents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generative_answers_knowledge_response_source_contents_item import (
            GenerativeAnswersKnowledgeResponseSourceContentsItem,
        )

        d = dict(src_dict)
        answer = d.pop("answer", UNSET)

        _llm_confidence_level = d.pop("llm_confidence_level", UNSET)
        llm_confidence_level: Union[Unset, GenerativeAnswersKnowledgeResponseLlmConfidenceLevel]
        if isinstance(_llm_confidence_level, Unset):
            llm_confidence_level = UNSET
        else:
            llm_confidence_level = GenerativeAnswersKnowledgeResponseLlmConfidenceLevel(_llm_confidence_level)

        solved = d.pop("solved", UNSET)

        source_contents = []
        _source_contents = d.pop("source_contents", UNSET)
        for source_contents_item_data in _source_contents or []:
            source_contents_item = GenerativeAnswersKnowledgeResponseSourceContentsItem.from_dict(
                source_contents_item_data
            )

            source_contents.append(source_contents_item)

        generative_answers_knowledge_response = cls(
            answer=answer,
            llm_confidence_level=llm_confidence_level,
            solved=solved,
            source_contents=source_contents,
        )

        generative_answers_knowledge_response.additional_properties = d
        return generative_answers_knowledge_response

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
