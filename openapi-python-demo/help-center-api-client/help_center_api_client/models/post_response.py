from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_object import PostObject


T = TypeVar("T", bound="PostResponse")


@_attrs_define
class PostResponse:
    """
    Attributes:
        post (Union[Unset, PostObject]):  Example: {'author_id': 3465, 'featured': True, 'id': 1635, 'title': 'The
            post'}.
    """

    post: Union[Unset, "PostObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        post: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.post, Unset):
            post = self.post.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if post is not UNSET:
            field_dict["post"] = post

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_object import PostObject

        d = dict(src_dict)
        _post = d.pop("post", UNSET)
        post: Union[Unset, PostObject]
        if isinstance(_post, Unset):
            post = UNSET
        else:
            post = PostObject.from_dict(_post)

        post_response = cls(
            post=post,
        )

        post_response.additional_properties = d
        return post_response

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
