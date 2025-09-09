from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vote_object import VoteObject


T = TypeVar("T", bound="VotesResponse")


@_attrs_define
class VotesResponse:
    """
    Attributes:
        votes (Union[Unset, list['VoteObject']]):
    """

    votes: Union[Unset, list["VoteObject"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        votes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.votes, Unset):
            votes = []
            for votes_item_data in self.votes:
                votes_item = votes_item_data.to_dict()
                votes.append(votes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if votes is not UNSET:
            field_dict["votes"] = votes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vote_object import VoteObject

        d = dict(src_dict)
        votes = []
        _votes = d.pop("votes", UNSET)
        for votes_item_data in _votes or []:
            votes_item = VoteObject.from_dict(votes_item_data)

            votes.append(votes_item)

        votes_response = cls(
            votes=votes,
        )

        votes_response.additional_properties = d
        return votes_response

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
