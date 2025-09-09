from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.article_request_article import ArticleRequestArticle


T = TypeVar("T", bound="ArticleRequest")


@_attrs_define
class ArticleRequest:
    """
    Attributes:
        article (ArticleRequestArticle):
        notify_subscribers (Union[Unset, bool]):
    """

    article: "ArticleRequestArticle"
    notify_subscribers: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        article = self.article.to_dict()

        notify_subscribers = self.notify_subscribers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "article": article,
            }
        )
        if notify_subscribers is not UNSET:
            field_dict["notify_subscribers"] = notify_subscribers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.article_request_article import ArticleRequestArticle

        d = dict(src_dict)
        article = ArticleRequestArticle.from_dict(d.pop("article"))

        notify_subscribers = d.pop("notify_subscribers", UNSET)

        article_request = cls(
            article=article,
            notify_subscribers=notify_subscribers,
        )

        article_request.additional_properties = d
        return article_request

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
