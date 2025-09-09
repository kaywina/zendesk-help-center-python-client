from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.section_object import SectionObject


T = TypeVar("T", bound="SectionsResponse")


@_attrs_define
class SectionsResponse:
    """
    Attributes:
        sections (Union[Unset, list['SectionObject']]):
    """

    sections: Union[Unset, list["SectionObject"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sections, Unset):
            sections = []
            for sections_item_data in self.sections:
                sections_item = sections_item_data.to_dict()
                sections.append(sections_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sections is not UNSET:
            field_dict["sections"] = sections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.section_object import SectionObject

        d = dict(src_dict)
        sections = []
        _sections = d.pop("sections", UNSET)
        for sections_item_data in _sections or []:
            sections_item = SectionObject.from_dict(sections_item_data)

            sections.append(sections_item)

        sections_response = cls(
            sections=sections,
        )

        sections_response.additional_properties = d
        return sections_response

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
