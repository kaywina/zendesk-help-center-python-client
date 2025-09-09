from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vote_object import VoteObject


T = TypeVar("T", bound="VoteResponse")


@_attrs_define
class VoteResponse:
    """
    Attributes:
        vote (Union[Unset, VoteObject]):  Example: {'created_at': '2012-04-04T09:14:57Z', 'id': 1635, 'item_id': 65466,
            'item_type': 'Article', 'user_id': 3465, 'value': 1}.
    """

    vote: Union[Unset, "VoteObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vote: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vote, Unset):
            vote = self.vote.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vote is not UNSET:
            field_dict["vote"] = vote

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vote_object import VoteObject

        d = dict(src_dict)
        _vote = d.pop("vote", UNSET)
        vote: Union[Unset, VoteObject]
        if isinstance(_vote, Unset):
            vote = UNSET
        else:
            vote = VoteObject.from_dict(_vote)

        vote_response = cls(
            vote=vote,
        )

        vote_response.additional_properties = d
        return vote_response

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
