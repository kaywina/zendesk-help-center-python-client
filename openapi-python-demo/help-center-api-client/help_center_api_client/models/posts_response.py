from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_object import PostObject


T = TypeVar("T", bound="PostsResponse")


@_attrs_define
class PostsResponse:
    """
    Attributes:
        posts (Union[Unset, list['PostObject']]):
    """

    posts: Union[Unset, list["PostObject"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        posts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.posts, Unset):
            posts = []
            for posts_item_data in self.posts:
                posts_item = posts_item_data.to_dict()
                posts.append(posts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if posts is not UNSET:
            field_dict["posts"] = posts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_object import PostObject

        d = dict(src_dict)
        posts = []
        _posts = d.pop("posts", UNSET)
        for posts_item_data in _posts or []:
            posts_item = PostObject.from_dict(posts_item_data)

            posts.append(posts_item)

        posts_response = cls(
            posts=posts,
        )

        posts_response.additional_properties = d
        return posts_response

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
