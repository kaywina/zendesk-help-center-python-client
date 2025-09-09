import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CategoryObject")


@_attrs_define
class CategoryObject:
    """
    Example:
        {'description': '', 'html_url': 'https://company.zendesk.com/hc/en-us/categories/354362577', 'id': 1635,
            'locale': 'en-us', 'name': 'Self Help Articles', 'source_locale': 'en-us', 'url':
            'https://company.zendesk.com/api/v2/help_center/categories/354362577'}

    Attributes:
        id (int): Automatically assigned when creating categories
        locale (str): The locale where the category is displayed
        name (str): The name of the category
        created_at (Union[Unset, datetime.datetime]): The time at which the category was created
        description (Union[Unset, str]): The description of the category
        html_url (Union[Unset, str]): The url of this category in Help Center
        outdated (Union[Unset, bool]): Whether the category is out of date
        position (Union[Unset, int]): The position of this category relative to other categories
        source_locale (Union[Unset, str]): The source (default) locale of the category
        updated_at (Union[Unset, datetime.datetime]): The time at which the category was last updated
        url (Union[Unset, str]): The API url of this category
    """

    id: int
    locale: str
    name: str
    created_at: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    outdated: Union[Unset, bool] = UNSET
    position: Union[Unset, int] = UNSET
    source_locale: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        locale = self.locale

        name = self.name

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description = self.description

        html_url = self.html_url

        outdated = self.outdated

        position = self.position

        source_locale = self.source_locale

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "locale": locale,
                "name": name,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if outdated is not UNSET:
            field_dict["outdated"] = outdated
        if position is not UNSET:
            field_dict["position"] = position
        if source_locale is not UNSET:
            field_dict["source_locale"] = source_locale
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        locale = d.pop("locale")

        name = d.pop("name")

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        description = d.pop("description", UNSET)

        html_url = d.pop("html_url", UNSET)

        outdated = d.pop("outdated", UNSET)

        position = d.pop("position", UNSET)

        source_locale = d.pop("source_locale", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        url = d.pop("url", UNSET)

        category_object = cls(
            id=id,
            locale=locale,
            name=name,
            created_at=created_at,
            description=description,
            html_url=html_url,
            outdated=outdated,
            position=position,
            source_locale=source_locale,
            updated_at=updated_at,
            url=url,
        )

        category_object.additional_properties = d
        return category_object

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
