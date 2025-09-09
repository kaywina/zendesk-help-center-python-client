from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.article_object import ArticleObject


T = TypeVar("T", bound="ArticleResponse")


@_attrs_define
class ArticleResponse:
    """
    Attributes:
        article (Union[Unset, ArticleObject]):  Example: {'author_id': 3465, 'comments_disabled': False, 'id': 1635,
            'locale': 'en', 'permission_group_id': 13, 'title': 'The article', 'user_segment_id': 12}.
    """

    article: Union[Unset, "ArticleObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        article: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.article, Unset):
            article = self.article.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if article is not UNSET:
            field_dict["article"] = article

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.article_object import ArticleObject

        d = dict(src_dict)
        _article = d.pop("article", UNSET)
        article: Union[Unset, ArticleObject]
        if isinstance(_article, Unset):
            article = UNSET
        else:
            article = ArticleObject.from_dict(_article)

        article_response = cls(
            article=article,
        )

        article_response.additional_properties = d
        return article_response

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
