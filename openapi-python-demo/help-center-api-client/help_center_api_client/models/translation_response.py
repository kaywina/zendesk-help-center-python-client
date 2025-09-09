from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.translation_object import TranslationObject


T = TypeVar("T", bound="TranslationResponse")


@_attrs_define
class TranslationResponse:
    """
    Attributes:
        translation (Union[Unset, TranslationObject]):  Example: {'id': 3243452, 'locale': 'en', 'source_id': 768934,
            'source_type': 'Article', 'title': 'Hello translation'}.
    """

    translation: Union[Unset, "TranslationObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        translation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.translation, Unset):
            translation = self.translation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if translation is not UNSET:
            field_dict["translation"] = translation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.translation_object import TranslationObject

        d = dict(src_dict)
        _translation = d.pop("translation", UNSET)
        translation: Union[Unset, TranslationObject]
        if isinstance(_translation, Unset):
            translation = UNSET
        else:
            translation = TranslationObject.from_dict(_translation)

        translation_response = cls(
            translation=translation,
        )

        translation_response.additional_properties = d
        return translation_response

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
