from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUserImageResponseUserImage")


@_attrs_define
class CreateUserImageResponseUserImage:
    """
    Attributes:
        content_type (Union[Unset, str]):
        path (Union[Unset, str]):
        size (Union[Unset, float]):
    """

    content_type: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    size: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        path = self.path

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if path is not UNSET:
            field_dict["path"] = path
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("content_type", UNSET)

        path = d.pop("path", UNSET)

        size = d.pop("size", UNSET)

        create_user_image_response_user_image = cls(
            content_type=content_type,
            path=path,
            size=size,
        )

        create_user_image_response_user_image.additional_properties = d
        return create_user_image_response_user_image

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
