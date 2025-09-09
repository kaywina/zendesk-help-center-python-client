from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalesWithDefaultResponse")


@_attrs_define
class LocalesWithDefaultResponse:
    """
    Attributes:
        default_locale (Union[Unset, str]):
        locales (Union[Unset, list[str]]):
    """

    default_locale: Union[Unset, str] = UNSET
    locales: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_locale = self.default_locale

        locales: Union[Unset, list[str]] = UNSET
        if not isinstance(self.locales, Unset):
            locales = self.locales

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if locales is not UNSET:
            field_dict["locales"] = locales

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_locale = d.pop("default_locale", UNSET)

        locales = cast(list[str], d.pop("locales", UNSET))

        locales_with_default_response = cls(
            default_locale=default_locale,
            locales=locales,
        )

        locales_with_default_response.additional_properties = d
        return locales_with_default_response

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
