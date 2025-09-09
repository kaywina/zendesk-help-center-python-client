from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.article_attachment_object import ArticleAttachmentObject


T = TypeVar("T", bound="ArticleAttachmentsResponse")


@_attrs_define
class ArticleAttachmentsResponse:
    """
    Attributes:
        article_attachments (Union[Unset, list['ArticleAttachmentObject']]):
    """

    article_attachments: Union[Unset, list["ArticleAttachmentObject"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        article_attachments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.article_attachments, Unset):
            article_attachments = []
            for article_attachments_item_data in self.article_attachments:
                article_attachments_item = article_attachments_item_data.to_dict()
                article_attachments.append(article_attachments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if article_attachments is not UNSET:
            field_dict["article_attachments"] = article_attachments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.article_attachment_object import ArticleAttachmentObject

        d = dict(src_dict)
        article_attachments = []
        _article_attachments = d.pop("article_attachments", UNSET)
        for article_attachments_item_data in _article_attachments or []:
            article_attachments_item = ArticleAttachmentObject.from_dict(article_attachments_item_data)

            article_attachments.append(article_attachments_item)

        article_attachments_response = cls(
            article_attachments=article_attachments,
        )

        article_attachments_response.additional_properties = d
        return article_attachments_response

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
