from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.section_object import SectionObject


T = TypeVar("T", bound="SectionResponse")


@_attrs_define
class SectionResponse:
    """
    Attributes:
        section (Union[Unset, SectionObject]):  Example: {'category_id': 3465, 'description': 'This section contains
            tricks for the airborne', 'id': 1635, 'locale': 'en-us', 'name': 'Avionics'}.
    """

    section: Union[Unset, "SectionObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        section: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.section, Unset):
            section = self.section.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if section is not UNSET:
            field_dict["section"] = section

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.section_object import SectionObject

        d = dict(src_dict)
        _section = d.pop("section", UNSET)
        section: Union[Unset, SectionObject]
        if isinstance(_section, Unset):
            section = UNSET
        else:
            section = SectionObject.from_dict(_section)

        section_response = cls(
            section=section,
        )

        section_response.additional_properties = d
        return section_response

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
