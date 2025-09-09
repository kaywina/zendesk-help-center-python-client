from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerativeAnswersKnowledgeResponseSourceContentsItem")


@_attrs_define
class GenerativeAnswersKnowledgeResponseSourceContentsItem:
    """
    Attributes:
        id (Union[Unset, str]): Unique identifier for the content.
        locale (Union[Unset, str]): Locale of the content.
        search_id (Union[Unset, str]): Search identifier for the content.
        title (Union[Unset, str]): Title of the content.
        type_ (Union[Unset, str]): Type of content (e.g., article).
        url (Union[Unset, str]): URL to access the content.
    """

    id: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    search_id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        locale = self.locale

        search_id = self.search_id

        title = self.title

        type_ = self.type_

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if locale is not UNSET:
            field_dict["locale"] = locale
        if search_id is not UNSET:
            field_dict["search_id"] = search_id
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        locale = d.pop("locale", UNSET)

        search_id = d.pop("search_id", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        generative_answers_knowledge_response_source_contents_item = cls(
            id=id,
            locale=locale,
            search_id=search_id,
            title=title,
            type_=type_,
            url=url,
        )

        generative_answers_knowledge_response_source_contents_item.additional_properties = d
        return generative_answers_knowledge_response_source_contents_item

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
