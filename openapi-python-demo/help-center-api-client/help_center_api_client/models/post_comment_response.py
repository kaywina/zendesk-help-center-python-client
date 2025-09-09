from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_comment_object import PostCommentObject


T = TypeVar("T", bound="PostCommentResponse")


@_attrs_define
class PostCommentResponse:
    """
    Attributes:
        comment (Union[Unset, PostCommentObject]):  Example: {'author_id': 89567, 'body': 'My printer is on fire!',
            'id': 35467, 'official': False, 'vote_count': 15, 'vote_sum': 10}.
    """

    comment: Union[Unset, "PostCommentObject"] = UNSET
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
        from ..models.post_comment_object import PostCommentObject

        d = dict(src_dict)
        _comment = d.pop("comment", UNSET)
        comment: Union[Unset, PostCommentObject]
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = PostCommentObject.from_dict(_comment)

        post_comment_response = cls(
            comment=comment,
        )

        post_comment_response.additional_properties = d
        return post_comment_response

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
