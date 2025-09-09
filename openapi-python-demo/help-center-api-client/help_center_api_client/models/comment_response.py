from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_object import CommentObject


T = TypeVar("T", bound="CommentResponse")


@_attrs_define
class CommentResponse:
    """
    Attributes:
        comment (Union[Unset, CommentObject]):  Example: {'author_id': 3465, 'body': 'Thanks for your help!',
            'created_at': '2012-04-04T09:14:57Z', 'id': 1635, 'locale': 'en-us', 'source_id': 65466, 'source_type':
            'Article'}.
    """

    comment: Union[Unset, "CommentObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment_object import CommentObject

        d = dict(src_dict)
        _comment = d.pop("comment", UNSET)
        comment: Union[Unset, CommentObject]
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = CommentObject.from_dict(_comment)

        comment_response = cls(
            comment=comment,
        )

        comment_response.additional_properties = d
        return comment_response

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
