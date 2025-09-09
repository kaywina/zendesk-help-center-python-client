from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_object import LabelObject


T = TypeVar("T", bound="LabelResponse")


@_attrs_define
class LabelResponse:
    """
    Attributes:
        label (Union[Unset, LabelObject]):  Example: {'created_at': '2012-04-04T09:14:57Z', 'id': 2003, 'name':
            'instructions'}.
    """

    label: Union[Unset, "LabelObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_object import LabelObject

        d = dict(src_dict)
        _label = d.pop("label", UNSET)
        label: Union[Unset, LabelObject]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = LabelObject.from_dict(_label)

        label_response = cls(
            label=label,
        )

        label_response.additional_properties = d
        return label_response

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
