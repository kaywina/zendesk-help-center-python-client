from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topic_object import TopicObject


T = TypeVar("T", bound="TopicsResponse")


@_attrs_define
class TopicsResponse:
    """
    Attributes:
        topics (Union[Unset, list['TopicObject']]):
    """

    topics: Union[Unset, list["TopicObject"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        topics: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.topics, Unset):
            topics = []
            for topics_item_data in self.topics:
                topics_item = topics_item_data.to_dict()
                topics.append(topics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if topics is not UNSET:
            field_dict["topics"] = topics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.topic_object import TopicObject

        d = dict(src_dict)
        topics = []
        _topics = d.pop("topics", UNSET)
        for topics_item_data in _topics or []:
            topics_item = TopicObject.from_dict(topics_item_data)

            topics.append(topics_item)

        topics_response = cls(
            topics=topics,
        )

        topics_response.additional_properties = d
        return topics_response

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
