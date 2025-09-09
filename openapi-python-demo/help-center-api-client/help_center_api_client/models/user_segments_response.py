from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_segment_object import UserSegmentObject


T = TypeVar("T", bound="UserSegmentsResponse")


@_attrs_define
class UserSegmentsResponse:
    """
    Attributes:
        user_segments (Union[Unset, list['UserSegmentObject']]):
    """

    user_segments: Union[Unset, list["UserSegmentObject"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_segments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_segments, Unset):
            user_segments = []
            for user_segments_item_data in self.user_segments:
                user_segments_item = user_segments_item_data.to_dict()
                user_segments.append(user_segments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_segments is not UNSET:
            field_dict["user_segments"] = user_segments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_segment_object import UserSegmentObject

        d = dict(src_dict)
        user_segments = []
        _user_segments = d.pop("user_segments", UNSET)
        for user_segments_item_data in _user_segments or []:
            user_segments_item = UserSegmentObject.from_dict(user_segments_item_data)

            user_segments.append(user_segments_item)

        user_segments_response = cls(
            user_segments=user_segments,
        )

        user_segments_response.additional_properties = d
        return user_segments_response

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
