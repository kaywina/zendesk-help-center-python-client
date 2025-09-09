from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.article_attachment_object import ArticleAttachmentObject


T = TypeVar("T", bound="ArticleAttachmentResponse")


@_attrs_define
class ArticleAttachmentResponse:
    """
    Attributes:
        article_attachment (Union[Unset, ArticleAttachmentObject]):  Example: {'article_id': 23, 'content_type':
            'application/pdf', 'content_url': 'https://company.zendesk.com/hc/article_attachments/200109629', 'created_at':
            '2012-04-04T09:14:57Z', 'file_name': 'party_invitation.pdf', 'id': 1428, 'inline': False, 'locale': 'en_us',
            'size': 58298}.
    """

    article_attachment: Union[Unset, "ArticleAttachmentObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        article_attachment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.article_attachment, Unset):
            article_attachment = self.article_attachment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if article_attachment is not UNSET:
            field_dict["article_attachment"] = article_attachment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.article_attachment_object import ArticleAttachmentObject

        d = dict(src_dict)
        _article_attachment = d.pop("article_attachment", UNSET)
        article_attachment: Union[Unset, ArticleAttachmentObject]
        if isinstance(_article_attachment, Unset):
            article_attachment = UNSET
        else:
            article_attachment = ArticleAttachmentObject.from_dict(_article_attachment)

        article_attachment_response = cls(
            article_attachment=article_attachment,
        )

        article_attachment_response.additional_properties = d
        return article_attachment_response

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
