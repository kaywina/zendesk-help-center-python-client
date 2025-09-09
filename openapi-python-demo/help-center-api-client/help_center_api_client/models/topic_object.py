from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.topic_object_manageable_by import TopicObjectManageableBy
from ..types import UNSET, Unset

T = TypeVar("T", bound="TopicObject")


@_attrs_define
class TopicObject:
    """The `manageable_by` attribute takes one of the following values:

    | Value     | Users                       |
    |-----------|---------------------------- |
    | staff     | agents and managers         |
    | managers  | only Help Center managers   |

    Note that `manageable_by` is only displayed to users who can manage the topic.

        Example:
            {'created_at': '2012-04-04T09:14:57Z', 'description': 'Security Best Practices', 'follower_count': 332, 'id':
                1635, 'manageable_by': 'staff', 'name': 'Security'}

        Attributes:
            name (str): The name of the topic
            created_at (Union[Unset, str]): When the topic was created
            description (Union[None, Unset, str]): The description of the topic. By default an empty string
            follower_count (Union[Unset, int]): The number of users following the topic
            html_url (Union[Unset, str]): The community url of the topic
            id (Union[Unset, int]): Automatically assigned when the topic is created
            manageable_by (Union[Unset, TopicObjectManageableBy]): The set of users who can manage this topic.
            position (Union[Unset, int]): The position of the topic relative to other topics in the community
            updated_at (Union[Unset, str]): When the topic was last updated
            url (Union[Unset, str]): The API url of the topic
            user_segment_id (Union[None, Unset, int]): The id of the user segment to which this topic belongs
    """

    name: str
    created_at: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    follower_count: Union[Unset, int] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    manageable_by: Union[Unset, TopicObjectManageableBy] = UNSET
    position: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    user_segment_id: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        created_at = self.created_at

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        follower_count = self.follower_count

        html_url = self.html_url

        id = self.id

        manageable_by: Union[Unset, str] = UNSET
        if not isinstance(self.manageable_by, Unset):
            manageable_by = self.manageable_by.value

        position = self.position

        updated_at = self.updated_at

        url = self.url

        user_segment_id: Union[None, Unset, int]
        if isinstance(self.user_segment_id, Unset):
            user_segment_id = UNSET
        else:
            user_segment_id = self.user_segment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if manageable_by is not UNSET:
            field_dict["manageable_by"] = manageable_by
        if position is not UNSET:
            field_dict["position"] = position
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if user_segment_id is not UNSET:
            field_dict["user_segment_id"] = user_segment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        created_at = d.pop("created_at", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        follower_count = d.pop("follower_count", UNSET)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        _manageable_by = d.pop("manageable_by", UNSET)
        manageable_by: Union[Unset, TopicObjectManageableBy]
        if isinstance(_manageable_by, Unset):
            manageable_by = UNSET
        else:
            manageable_by = TopicObjectManageableBy(_manageable_by)

        position = d.pop("position", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        def _parse_user_segment_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        user_segment_id = _parse_user_segment_id(d.pop("user_segment_id", UNSET))

        topic_object = cls(
            name=name,
            created_at=created_at,
            description=description,
            follower_count=follower_count,
            html_url=html_url,
            id=id,
            manageable_by=manageable_by,
            position=position,
            updated_at=updated_at,
            url=url,
            user_segment_id=user_segment_id,
        )

        topic_object.additional_properties = d
        return topic_object

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
