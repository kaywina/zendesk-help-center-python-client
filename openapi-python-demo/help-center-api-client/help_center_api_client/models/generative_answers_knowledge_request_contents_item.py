from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GenerativeAnswersKnowledgeRequestContentsItem")


@_attrs_define
class GenerativeAnswersKnowledgeRequestContentsItem:
    """
    Attributes:
        id (str): Unique identifier for the content.
        locale (str): Locale of the content.
        search_id (str): Search identifier for the content.
        type_ (str): Type of content (e.g., article).
        url (str): URL to access the content.
    """

    id: str
    locale: str
    search_id: str
    type_: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        locale = self.locale

        search_id = self.search_id

        type_ = self.type_

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "locale": locale,
                "search_id": search_id,
                "type": type_,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        locale = d.pop("locale")

        search_id = d.pop("search_id")

        type_ = d.pop("type")

        url = d.pop("url")

        generative_answers_knowledge_request_contents_item = cls(
            id=id,
            locale=locale,
            search_id=search_id,
            type_=type_,
            url=url,
        )

        generative_answers_knowledge_request_contents_item.additional_properties = d
        return generative_answers_knowledge_request_contents_item

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
