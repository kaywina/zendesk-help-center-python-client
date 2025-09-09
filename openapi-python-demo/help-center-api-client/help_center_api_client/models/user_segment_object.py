from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSegmentObject")


@_attrs_define
class UserSegmentObject:
    """The `user_type` attribute takes one of the following values:

    | Value               | Users                                |
    |---------------------|--------------------------------------|
    | signed_in_users     | only authenticated users             |
    | staff               | only agents and Help Center managers |


    For `group_ids`, `organization_ids`, `tags`, and `or_tags`,
    an empty array means that access is not restricted by the attribute. For example,
    if no group ids are specified, then users don't have to be in any specific group to
    have access.

    For `tags`, a user must have all the listed tags to have access. For `or_tags`, a
    user must have at least one of the listed tags to have access.

        Example:
            {'built_in': False, 'created_at': '2017-07-20T22:55:29Z', 'group_ids': [12], 'name': 'VIP agents',
                'organization_ids': [42], 'tags': ['vip'], 'updated_at': '2017-07-23T21:43:28Z', 'user_type': 'staff'}

        Attributes:
            user_type (str): The set of users who can view content
            added_user_ids (Union[Unset, list[int]]): The ids of users added specifically to this user segment, regardless
                of matching tags or other criteria
            built_in (Union[Unset, bool]): Whether the user segment is built-in. Built-in user segments cannot be modified
            created_at (Union[Unset, str]): When the user segment was created
            group_ids (Union[Unset, list[int]]): The ids of the groups that have access
            id (Union[Unset, int]): Automatically assigned when the user segment is created
            name (Union[Unset, str]): User segment name (localized to the locale of the current user for built-in user
                segments)
            or_tags (Union[Unset, list[str]]): A user must have at least one tag in the list to have access
            organization_ids (Union[Unset, list[int]]): The ids of the organizations that have access
            tags (Union[Unset, list[str]]): All the tags a user must have to have access
            updated_at (Union[Unset, str]): When the user segment was last updated
    """

    user_type: str
    added_user_ids: Union[Unset, list[int]] = UNSET
    built_in: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    group_ids: Union[Unset, list[int]] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    or_tags: Union[Unset, list[str]] = UNSET
    organization_ids: Union[Unset, list[int]] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_type = self.user_type

        added_user_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.added_user_ids, Unset):
            added_user_ids = self.added_user_ids

        built_in = self.built_in

        created_at = self.created_at

        group_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        id = self.id

        name = self.name

        or_tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.or_tags, Unset):
            or_tags = self.or_tags

        organization_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.organization_ids, Unset):
            organization_ids = self.organization_ids

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_type": user_type,
            }
        )
        if added_user_ids is not UNSET:
            field_dict["added_user_ids"] = added_user_ids
        if built_in is not UNSET:
            field_dict["built_in"] = built_in
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if or_tags is not UNSET:
            field_dict["or_tags"] = or_tags
        if organization_ids is not UNSET:
            field_dict["organization_ids"] = organization_ids
        if tags is not UNSET:
            field_dict["tags"] = tags
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_type = d.pop("user_type")

        added_user_ids = cast(list[int], d.pop("added_user_ids", UNSET))

        built_in = d.pop("built_in", UNSET)

        created_at = d.pop("created_at", UNSET)

        group_ids = cast(list[int], d.pop("group_ids", UNSET))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        or_tags = cast(list[str], d.pop("or_tags", UNSET))

        organization_ids = cast(list[int], d.pop("organization_ids", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        updated_at = d.pop("updated_at", UNSET)

        user_segment_object = cls(
            user_type=user_type,
            added_user_ids=added_user_ids,
            built_in=built_in,
            created_at=created_at,
            group_ids=group_ids,
            id=id,
            name=name,
            or_tags=or_tags,
            organization_ids=organization_ids,
            tags=tags,
            updated_at=updated_at,
        )

        user_segment_object.additional_properties = d
        return user_segment_object

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
