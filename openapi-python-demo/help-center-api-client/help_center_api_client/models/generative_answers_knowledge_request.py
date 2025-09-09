from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.generative_answers_knowledge_request_contents_item import (
        GenerativeAnswersKnowledgeRequestContentsItem,
    )


T = TypeVar("T", bound="GenerativeAnswersKnowledgeRequest")


@_attrs_define
class GenerativeAnswersKnowledgeRequest:
    """
    Attributes:
        contents (list['GenerativeAnswersKnowledgeRequestContentsItem']):
        query (str): The query for which the answer is to be generated.
        ticket_id (int): The ID of the ticket associated with the query.
    """

    contents: list["GenerativeAnswersKnowledgeRequestContentsItem"]
    query: str
    ticket_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contents = []
        for contents_item_data in self.contents:
            contents_item = contents_item_data.to_dict()
            contents.append(contents_item)

        query = self.query

        ticket_id = self.ticket_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contents": contents,
                "query": query,
                "ticket_id": ticket_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generative_answers_knowledge_request_contents_item import (
            GenerativeAnswersKnowledgeRequestContentsItem,
        )

        d = dict(src_dict)
        contents = []
        _contents = d.pop("contents")
        for contents_item_data in _contents:
            contents_item = GenerativeAnswersKnowledgeRequestContentsItem.from_dict(contents_item_data)

            contents.append(contents_item)

        query = d.pop("query")

        ticket_id = d.pop("ticket_id")

        generative_answers_knowledge_request = cls(
            contents=contents,
            query=query,
            ticket_id=ticket_id,
        )

        generative_answers_knowledge_request.additional_properties = d
        return generative_answers_knowledge_request

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
