from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_user_image_response_user_image import CreateUserImageResponseUserImage


T = TypeVar("T", bound="CreateUserImageResponse")


@_attrs_define
class CreateUserImageResponse:
    """
    Attributes:
        user_image (Union[Unset, CreateUserImageResponseUserImage]):
    """

    user_image: Union[Unset, "CreateUserImageResponseUserImage"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_image: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user_image, Unset):
            user_image = self.user_image.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_image is not UNSET:
            field_dict["user_image"] = user_image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_user_image_response_user_image import CreateUserImageResponseUserImage

        d = dict(src_dict)
        _user_image = d.pop("user_image", UNSET)
        user_image: Union[Unset, CreateUserImageResponseUserImage]
        if isinstance(_user_image, Unset):
            user_image = UNSET
        else:
            user_image = CreateUserImageResponseUserImage.from_dict(_user_image)

        create_user_image_response = cls(
            user_image=user_image,
        )

        create_user_image_response.additional_properties = d
        return create_user_image_response

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
