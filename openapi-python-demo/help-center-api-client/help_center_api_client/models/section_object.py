from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SectionObject")


@_attrs_define
class SectionObject:
    """
    Example:
        {'category_id': 3465, 'description': 'This section contains tricks for the airborne', 'id': 1635, 'locale': 'en-
            us', 'name': 'Avionics'}

    Attributes:
        locale (str): The locale in which the section is displayed
        name (str): The name of the section
        category_id (Union[Unset, int]): The id of the category to which this section belongs
        created_at (Union[Unset, str]): The time at which the section was created
        description (Union[Unset, str]): The description of the section
        html_url (Union[Unset, str]): The url of this section in HC
        id (Union[Unset, int]): Automatically assigned when creating subscriptions
        outdated (Union[Unset, bool]): Whether the section is out of date
        parent_section_id (Union[None, Unset, int]): The id of the section to which this section belongs. Only writable
            for Guide Enterprise customers
        position (Union[Unset, int]): The position of this section in the section list. Used when sorting is set to
            ´manual´. By default the section is added to the end of the list
        source_locale (Union[Unset, str]): The source (default) locale of the section
        theme_template (Union[Unset, str]): The theme template name used to display this section in Help Center.
            Example: section_template.
        updated_at (Union[Unset, str]): The time at which the section was last updated
        url (Union[Unset, str]): The API url of this section
    """

    locale: str
    name: str
    category_id: Union[Unset, int] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    outdated: Union[Unset, bool] = UNSET
    parent_section_id: Union[None, Unset, int] = UNSET
    position: Union[Unset, int] = UNSET
    source_locale: Union[Unset, str] = UNSET
    theme_template: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        name = self.name

        category_id = self.category_id

        created_at = self.created_at

        description = self.description

        html_url = self.html_url

        id = self.id

        outdated = self.outdated

        parent_section_id: Union[None, Unset, int]
        if isinstance(self.parent_section_id, Unset):
            parent_section_id = UNSET
        else:
            parent_section_id = self.parent_section_id

        position = self.position

        source_locale = self.source_locale

        theme_template = self.theme_template

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locale": locale,
                "name": name,
            }
        )
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if outdated is not UNSET:
            field_dict["outdated"] = outdated
        if parent_section_id is not UNSET:
            field_dict["parent_section_id"] = parent_section_id
        if position is not UNSET:
            field_dict["position"] = position
        if source_locale is not UNSET:
            field_dict["source_locale"] = source_locale
        if theme_template is not UNSET:
            field_dict["theme_template"] = theme_template
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        locale = d.pop("locale")

        name = d.pop("name")

        category_id = d.pop("category_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        outdated = d.pop("outdated", UNSET)

        def _parse_parent_section_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_section_id = _parse_parent_section_id(d.pop("parent_section_id", UNSET))

        position = d.pop("position", UNSET)

        source_locale = d.pop("source_locale", UNSET)

        theme_template = d.pop("theme_template", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        section_object = cls(
            locale=locale,
            name=name,
            category_id=category_id,
            created_at=created_at,
            description=description,
            html_url=html_url,
            id=id,
            outdated=outdated,
            parent_section_id=parent_section_id,
            position=position,
            source_locale=source_locale,
            theme_template=theme_template,
            updated_at=updated_at,
            url=url,
        )

        section_object.additional_properties = d
        return section_object

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
