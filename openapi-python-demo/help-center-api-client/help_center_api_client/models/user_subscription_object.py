from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserSubscriptionObject")


@_attrs_define
class UserSubscriptionObject:
    """
    Example:
        {'followed_id': 65466, 'follower_id': 98354, 'id': 1635}

    Attributes:
        followed_id (int): The id of the user being followed
        follower_id (int): The id of the user doing the following
        id (int): Automatically assigned when the subscription is created
    """

    followed_id: int
    follower_id: int
    id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        followed_id = self.followed_id

        follower_id = self.follower_id

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "followed_id": followed_id,
                "follower_id": follower_id,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        followed_id = d.pop("followed_id")

        follower_id = d.pop("follower_id")

        id = d.pop("id")

        user_subscription_object = cls(
            followed_id=followed_id,
            follower_id=follower_id,
            id=id,
        )

        user_subscription_object.additional_properties = d
        return user_subscription_object

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
