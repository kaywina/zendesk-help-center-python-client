from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_user_image_upload_response_upload_headers import RequestUserImageUploadResponseUploadHeaders


T = TypeVar("T", bound="RequestUserImageUploadResponseUpload")


@_attrs_define
class RequestUserImageUploadResponseUpload:
    """
    Attributes:
        headers (Union[Unset, RequestUserImageUploadResponseUploadHeaders]):
        token (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    headers: Union[Unset, "RequestUserImageUploadResponseUploadHeaders"] = UNSET
    token: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        token = self.token

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers
        if token is not UNSET:
            field_dict["token"] = token
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_user_image_upload_response_upload_headers import (
            RequestUserImageUploadResponseUploadHeaders,
        )

        d = dict(src_dict)
        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, RequestUserImageUploadResponseUploadHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = RequestUserImageUploadResponseUploadHeaders.from_dict(_headers)

        token = d.pop("token", UNSET)

        url = d.pop("url", UNSET)

        request_user_image_upload_response_upload = cls(
            headers=headers,
            token=token,
            url=url,
        )

        request_user_image_upload_response_upload.additional_properties = d
        return request_user_image_upload_response_upload

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
