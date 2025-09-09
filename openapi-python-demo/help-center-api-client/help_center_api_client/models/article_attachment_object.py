from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.article_attachment_object_file import ArticleAttachmentObjectFile


T = TypeVar("T", bound="ArticleAttachmentObject")


@_attrs_define
class ArticleAttachmentObject:
    """
    Example:
        {'article_id': 23, 'content_type': 'application/pdf', 'content_url':
            'https://company.zendesk.com/hc/article_attachments/200109629', 'created_at': '2012-04-04T09:14:57Z',
            'file_name': 'party_invitation.pdf', 'id': 1428, 'inline': False, 'locale': 'en_us', 'size': 58298}

    Attributes:
        article_id (Union[Unset, int]): The associated article, if present
        content_type (Union[Unset, str]): The file type. Example: image/png
        content_url (Union[Unset, str]): URL where the attachment file can be downloaded
        created_at (Union[Unset, str]): The time the article attachment was created
        file (Union[Unset, ArticleAttachmentObjectFile]): File to upload, applicable only during creation.
        file_name (Union[Unset, str]): The file name
        guide_media_id (Union[Unset, str]): Unique identifier for the guide-media to associate with this attachment,
            applicable only during creation.
        id (Union[Unset, int]): Assigned ID when the article attachment is created
        inline (Union[Unset, bool]): The attached file is shown in the admin interface for inline attachments. Its URL
            can be referenced in the article's HTML body. Inline attachments are image files directly embedded in the
            article body. If false, the attachment is listed in the list of attachments. The default value is false
        locale (Union[Unset, str]): The locale of translation that the attachment will be attached to and can only be
            set on inline attachments
        size (Union[Unset, int]): The attachment file size in bytes
        updated_at (Union[Unset, str]): The time the article attachment was last updated
        url (Union[Unset, str]): The URL of the article attachment
    """

    article_id: Union[Unset, int] = UNSET
    content_type: Union[Unset, str] = UNSET
    content_url: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    file: Union[Unset, "ArticleAttachmentObjectFile"] = UNSET
    file_name: Union[Unset, str] = UNSET
    guide_media_id: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    inline: Union[Unset, bool] = UNSET
    locale: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        article_id = self.article_id

        content_type = self.content_type

        content_url = self.content_url

        created_at = self.created_at

        file: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        file_name = self.file_name

        guide_media_id = self.guide_media_id

        id = self.id

        inline = self.inline

        locale = self.locale

        size = self.size

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if article_id is not UNSET:
            field_dict["article_id"] = article_id
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if content_url is not UNSET:
            field_dict["content_url"] = content_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if file is not UNSET:
            field_dict["file"] = file
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if guide_media_id is not UNSET:
            field_dict["guide_media_id"] = guide_media_id
        if id is not UNSET:
            field_dict["id"] = id
        if inline is not UNSET:
            field_dict["inline"] = inline
        if locale is not UNSET:
            field_dict["locale"] = locale
        if size is not UNSET:
            field_dict["size"] = size
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.article_attachment_object_file import ArticleAttachmentObjectFile

        d = dict(src_dict)
        article_id = d.pop("article_id", UNSET)

        content_type = d.pop("content_type", UNSET)

        content_url = d.pop("content_url", UNSET)

        created_at = d.pop("created_at", UNSET)

        _file = d.pop("file", UNSET)
        file: Union[Unset, ArticleAttachmentObjectFile]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = ArticleAttachmentObjectFile.from_dict(_file)

        file_name = d.pop("file_name", UNSET)

        guide_media_id = d.pop("guide_media_id", UNSET)

        id = d.pop("id", UNSET)

        inline = d.pop("inline", UNSET)

        locale = d.pop("locale", UNSET)

        size = d.pop("size", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        article_attachment_object = cls(
            article_id=article_id,
            content_type=content_type,
            content_url=content_url,
            created_at=created_at,
            file=file,
            file_name=file_name,
            guide_media_id=guide_media_id,
            id=id,
            inline=inline,
            locale=locale,
            size=size,
            updated_at=updated_at,
            url=url,
        )

        article_attachment_object.additional_properties = d
        return article_attachment_object

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
