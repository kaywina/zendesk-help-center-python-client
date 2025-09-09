from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.generative_answers_knowledge_actions_request_knowledge_action import (
    GenerativeAnswersKnowledgeActionsRequestKnowledgeAction,
)

T = TypeVar("T", bound="GenerativeAnswersKnowledgeActionsRequest")


@_attrs_define
class GenerativeAnswersKnowledgeActionsRequest:
    """
    Attributes:
        knowledge_action (GenerativeAnswersKnowledgeActionsRequestKnowledgeAction): The action performed on the
            generated answer.
        search_id (str): The ID of the search query that was used to generate the answer.
        ticket_nice_id (str): The ID of the ticket associated with the query.
    """

    knowledge_action: GenerativeAnswersKnowledgeActionsRequestKnowledgeAction
    search_id: str
    ticket_nice_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_action = self.knowledge_action.value

        search_id = self.search_id

        ticket_nice_id = self.ticket_nice_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_action": knowledge_action,
                "search_id": search_id,
                "ticket_nice_id": ticket_nice_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        knowledge_action = GenerativeAnswersKnowledgeActionsRequestKnowledgeAction(d.pop("knowledge_action"))

        search_id = d.pop("search_id")

        ticket_nice_id = d.pop("ticket_nice_id")

        generative_answers_knowledge_actions_request = cls(
            knowledge_action=knowledge_action,
            search_id=search_id,
            ticket_nice_id=ticket_nice_id,
        )

        generative_answers_knowledge_actions_request.additional_properties = d
        return generative_answers_knowledge_actions_request

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
