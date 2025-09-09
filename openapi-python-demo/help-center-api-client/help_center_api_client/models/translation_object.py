from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranslationObject")


@_attrs_define
class TranslationObject:
    """
    Example:
        {'id': 3243452, 'locale': 'en', 'source_id': 768934, 'source_type': 'Article', 'title': 'Hello translation'}

    Attributes:
        locale (str): The locale of the translation
        title (str): The title of the translation
        body (Union[Unset, str]): HTML body of the translation. Empty by default
        created_at (Union[Unset, str]): The time at which the translation was created
        created_by_id (Union[Unset, int]): The id of the user who created the translation
        draft (Union[Unset, bool]): True if the translation is a draft; false otherwise. False by default
        html_url (Union[Unset, str]): The url of the translation in Help Center
        id (Union[Unset, int]): Automatically assigned when a translation is created
        outdated (Union[Unset, bool]): True if the translation is outdated; false otherwise. False by default
        source_id (Union[Unset, int]): The id of the item that has this translation
        source_type (Union[Unset, str]): The type of the item that has this translation. Can be "article", "section", or
            "category".
        updated_at (Union[Unset, str]): The time at which the translation was last updated
        updated_by_id (Union[None, Unset, int]): The id of the user who last updated the translation
        url (Union[Unset, str]): The API url of the translation
    """

    locale: str
    title: str
    body: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, int] = UNSET
    draft: Union[Unset, bool] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    outdated: Union[Unset, bool] = UNSET
    source_id: Union[Unset, int] = UNSET
    source_type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    updated_by_id: Union[None, Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        title = self.title

        body = self.body

        created_at = self.created_at

        created_by_id = self.created_by_id

        draft = self.draft

        html_url = self.html_url

        id = self.id

        outdated = self.outdated

        source_id = self.source_id

        source_type = self.source_type

        updated_at = self.updated_at

        updated_by_id: Union[None, Unset, int]
        if isinstance(self.updated_by_id, Unset):
            updated_by_id = UNSET
        else:
            updated_by_id = self.updated_by_id

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locale": locale,
                "title": title,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if draft is not UNSET:
            field_dict["draft"] = draft
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if outdated is not UNSET:
            field_dict["outdated"] = outdated
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by_id is not UNSET:
            field_dict["updated_by_id"] = updated_by_id
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        locale = d.pop("locale")

        title = d.pop("title")

        body = d.pop("body", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        draft = d.pop("draft", UNSET)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        outdated = d.pop("outdated", UNSET)

        source_id = d.pop("source_id", UNSET)

        source_type = d.pop("source_type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        def _parse_updated_by_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        updated_by_id = _parse_updated_by_id(d.pop("updated_by_id", UNSET))

        url = d.pop("url", UNSET)

        translation_object = cls(
            locale=locale,
            title=title,
            body=body,
            created_at=created_at,
            created_by_id=created_by_id,
            draft=draft,
            html_url=html_url,
            id=id,
            outdated=outdated,
            source_id=source_id,
            source_type=source_type,
            updated_at=updated_at,
            updated_by_id=updated_by_id,
            url=url,
        )

        translation_object.additional_properties = d
        return translation_object

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
