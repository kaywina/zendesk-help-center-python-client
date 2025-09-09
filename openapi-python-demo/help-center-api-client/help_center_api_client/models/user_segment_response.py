from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_segment_object import UserSegmentObject


T = TypeVar("T", bound="UserSegmentResponse")


@_attrs_define
class UserSegmentResponse:
    """
    Attributes:
        user_segment (Union[Unset, UserSegmentObject]): The `user_type` attribute takes one of the following values:

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
             Example: {'built_in': False, 'created_at': '2017-07-20T22:55:29Z', 'group_ids': [12], 'name': 'VIP agents',
            'organization_ids': [42], 'tags': ['vip'], 'updated_at': '2017-07-23T21:43:28Z', 'user_type': 'staff'}.
    """

    user_segment: Union[Unset, "UserSegmentObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_segment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user_segment, Unset):
            user_segment = self.user_segment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_segment is not UNSET:
            field_dict["user_segment"] = user_segment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_segment_object import UserSegmentObject

        d = dict(src_dict)
        _user_segment = d.pop("user_segment", UNSET)
        user_segment: Union[Unset, UserSegmentObject]
        if isinstance(_user_segment, Unset):
            user_segment = UNSET
        else:
            user_segment = UserSegmentObject.from_dict(_user_segment)

        user_segment_response = cls(
            user_segment=user_segment,
        )

        user_segment_response.additional_properties = d
        return user_segment_response

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
