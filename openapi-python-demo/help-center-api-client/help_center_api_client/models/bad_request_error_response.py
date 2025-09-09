from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bad_request_error_response_errors import BadRequestErrorResponseErrors


T = TypeVar("T", bound="BadRequestErrorResponse")


@_attrs_define
class BadRequestErrorResponse:
    """
    Example:
        {'errors': {'field_name_with_error': ['cannot process this field']}}

    Attributes:
        errors (Union[Unset, BadRequestErrorResponseErrors]):
    """

    errors: Union[Unset, "BadRequestErrorResponseErrors"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bad_request_error_response_errors import BadRequestErrorResponseErrors

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: Union[Unset, BadRequestErrorResponseErrors]
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = BadRequestErrorResponseErrors.from_dict(_errors)

        bad_request_error_response = cls(
            errors=errors,
        )

        bad_request_error_response.additional_properties = d
        return bad_request_error_response

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
