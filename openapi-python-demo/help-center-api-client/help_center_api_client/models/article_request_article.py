from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArticleRequestArticle")


@_attrs_define
class ArticleRequestArticle:
    """
    Attributes:
        locale (str):  Example: en-us.
        permission_group_id (int):  Default: 0. Example: 56.
        title (str):  Example: Taking photos in low light.
        user_segment_id (int):  Example: 123.
        body (Union[Unset, str]):  Example: Use a tripod.
    """

    locale: str
    title: str
    user_segment_id: int
    permission_group_id: int = 0
    body: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        permission_group_id = self.permission_group_id

        title = self.title

        user_segment_id = self.user_segment_id

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locale": locale,
                "permission_group_id": permission_group_id,
                "title": title,
                "user_segment_id": user_segment_id,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        locale = d.pop("locale")

        permission_group_id = d.pop("permission_group_id")

        title = d.pop("title")

        user_segment_id = d.pop("user_segment_id")

        body = d.pop("body", UNSET)

        article_request_article = cls(
            locale=locale,
            permission_group_id=permission_group_id,
            title=title,
            user_segment_id=user_segment_id,
            body=body,
        )

        article_request_article.additional_properties = d
        return article_request_article

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
