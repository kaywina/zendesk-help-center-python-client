from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.section_put_request_section_sorting import SectionPutRequestSectionSorting
from ..types import UNSET, Unset

T = TypeVar("T", bound="SectionPutRequestSection")


@_attrs_define
class SectionPutRequestSection:
    """
    Attributes:
        category_id (Union[Unset, int]): The id of the category to which this section belongs
        description (Union[Unset, str]): The description of the section
        name (Union[Unset, str]): The name of the section
        parent_section_id (Union[Unset, int]): The id of the section to which this section belongs. Only writable for
            Guide Enterprise customers
        position (Union[Unset, int]): The position of this section in the section list. Used when sorting is set to
            ´manual´.
        sorting (Union[Unset, SectionPutRequestSectionSorting]): Defines the type of sorting used in this section
        theme_template (Union[Unset, str]): The theme template name used to display this section in Help Center.
            Example: section_template.
    """

    category_id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    parent_section_id: Union[Unset, int] = UNSET
    position: Union[Unset, int] = UNSET
    sorting: Union[Unset, SectionPutRequestSectionSorting] = UNSET
    theme_template: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        description = self.description

        name = self.name

        parent_section_id = self.parent_section_id

        position = self.position

        sorting: Union[Unset, str] = UNSET
        if not isinstance(self.sorting, Unset):
            sorting = self.sorting.value

        theme_template = self.theme_template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if parent_section_id is not UNSET:
            field_dict["parent_section_id"] = parent_section_id
        if position is not UNSET:
            field_dict["position"] = position
        if sorting is not UNSET:
            field_dict["sorting"] = sorting
        if theme_template is not UNSET:
            field_dict["theme_template"] = theme_template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category_id = d.pop("category_id", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        parent_section_id = d.pop("parent_section_id", UNSET)

        position = d.pop("position", UNSET)

        _sorting = d.pop("sorting", UNSET)
        sorting: Union[Unset, SectionPutRequestSectionSorting]
        if isinstance(_sorting, Unset):
            sorting = UNSET
        else:
            sorting = SectionPutRequestSectionSorting(_sorting)

        theme_template = d.pop("theme_template", UNSET)

        section_put_request_section = cls(
            category_id=category_id,
            description=description,
            name=name,
            parent_section_id=parent_section_id,
            position=position,
            sorting=sorting,
            theme_template=theme_template,
        )

        section_put_request_section.additional_properties = d
        return section_put_request_section

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
