from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoteObject")


@_attrs_define
class VoteObject:
    """
    Example:
        {'created_at': '2012-04-04T09:14:57Z', 'id': 1635, 'item_id': 65466, 'item_type': 'Article', 'user_id': 3465,
            'value': 1}

    Attributes:
        value (int): The value of the vote
        created_at (Union[Unset, str]): The time at which the vote was created
        id (Union[Unset, int]): Automatically assigned when the vote is created
        item_id (Union[Unset, int]): The id of the item for which this vote was cast
        item_type (Union[Unset, str]): The type of the item. Can be "Article", "Comment", "Post" or "PostComment"
        updated_at (Union[Unset, str]): The time at which the vote was last updated
        url (Union[Unset, str]): The API url of this vote
        user_id (Union[Unset, int]): The id of the user who cast this vote
    """

    value: int
    created_at: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    item_id: Union[Unset, int] = UNSET
    item_type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        created_at = self.created_at

        id = self.id

        item_id = self.item_id

        item_type = self.item_type

        updated_at = self.updated_at

        url = self.url

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if item_id is not UNSET:
            field_dict["item_id"] = item_id
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        item_id = d.pop("item_id", UNSET)

        item_type = d.pop("item_type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        user_id = d.pop("user_id", UNSET)

        vote_object = cls(
            value=value,
            created_at=created_at,
            id=id,
            item_id=item_id,
            item_type=item_type,
            updated_at=updated_at,
            url=url,
            user_id=user_id,
        )

        vote_object.additional_properties = d
        return vote_object

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
