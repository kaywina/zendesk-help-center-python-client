from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_user_image_upload_response_upload import RequestUserImageUploadResponseUpload


T = TypeVar("T", bound="RequestUserImageUploadResponse")


@_attrs_define
class RequestUserImageUploadResponse:
    """
    Attributes:
        upload (Union[Unset, RequestUserImageUploadResponseUpload]):
    """

    upload: Union[Unset, "RequestUserImageUploadResponseUpload"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.upload, Unset):
            upload = self.upload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upload is not UNSET:
            field_dict["upload"] = upload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_user_image_upload_response_upload import RequestUserImageUploadResponseUpload

        d = dict(src_dict)
        _upload = d.pop("upload", UNSET)
        upload: Union[Unset, RequestUserImageUploadResponseUpload]
        if isinstance(_upload, Unset):
            upload = UNSET
        else:
            upload = RequestUserImageUploadResponseUpload.from_dict(_upload)

        request_user_image_upload_response = cls(
            upload=upload,
        )

        request_user_image_upload_response.additional_properties = d
        return request_user_image_upload_response

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
