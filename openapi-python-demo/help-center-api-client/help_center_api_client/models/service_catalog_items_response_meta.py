from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCatalogItemsResponseMeta")


@_attrs_define
class ServiceCatalogItemsResponseMeta:
    """Metadata about the service catalog items

    Attributes:
        after_cursor (Union[None, Unset, str]): The cursor to use for the next page of results
        before_cursor (Union[None, Unset, str]): The cursor to use for the previous page of results
        has_more (Union[Unset, bool]): Indicates if there are more items available in the next page
    """

    after_cursor: Union[None, Unset, str] = UNSET
    before_cursor: Union[None, Unset, str] = UNSET
    has_more: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after_cursor: Union[None, Unset, str]
        if isinstance(self.after_cursor, Unset):
            after_cursor = UNSET
        else:
            after_cursor = self.after_cursor

        before_cursor: Union[None, Unset, str]
        if isinstance(self.before_cursor, Unset):
            before_cursor = UNSET
        else:
            before_cursor = self.before_cursor

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after_cursor is not UNSET:
            field_dict["after_cursor"] = after_cursor
        if before_cursor is not UNSET:
            field_dict["before_cursor"] = before_cursor
        if has_more is not UNSET:
            field_dict["has_more"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_after_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        after_cursor = _parse_after_cursor(d.pop("after_cursor", UNSET))

        def _parse_before_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        before_cursor = _parse_before_cursor(d.pop("before_cursor", UNSET))

        has_more = d.pop("has_more", UNSET)

        service_catalog_items_response_meta = cls(
            after_cursor=after_cursor,
            before_cursor=before_cursor,
            has_more=has_more,
        )

        service_catalog_items_response_meta.additional_properties = d
        return service_catalog_items_response_meta

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
