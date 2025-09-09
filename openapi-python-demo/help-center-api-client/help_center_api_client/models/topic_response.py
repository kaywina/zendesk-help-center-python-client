from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topic_object import TopicObject


T = TypeVar("T", bound="TopicResponse")


@_attrs_define
class TopicResponse:
    """
    Attributes:
        topic (Union[Unset, TopicObject]): The `manageable_by` attribute takes one of the following values:

            | Value     | Users                       |
            |-----------|---------------------------- |
            | staff     | agents and managers         |
            | managers  | only Help Center managers   |

            Note that `manageable_by` is only displayed to users who can manage the topic.
             Example: {'created_at': '2012-04-04T09:14:57Z', 'description': 'Security Best Practices', 'follower_count':
            332, 'id': 1635, 'manageable_by': 'staff', 'name': 'Security'}.
    """

    topic: Union[Unset, "TopicObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        topic: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.topic, Unset):
            topic = self.topic.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if topic is not UNSET:
            field_dict["topic"] = topic

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.topic_object import TopicObject

        d = dict(src_dict)
        _topic = d.pop("topic", UNSET)
        topic: Union[Unset, TopicObject]
        if isinstance(_topic, Unset):
            topic = UNSET
        else:
            topic = TopicObject.from_dict(_topic)

        topic_response = cls(
            topic=topic,
        )

        topic_response.additional_properties = d
        return topic_response

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
