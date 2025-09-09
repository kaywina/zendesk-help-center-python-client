from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnifiedSearchResultSetMeta")


@_attrs_define
class UnifiedSearchResultSetMeta:
    """
    Attributes:
        after_cursor (Union[Unset, str]):
        before_cursor (Union[Unset, str]):
        has_more (Union[Unset, bool]):
    """

    after_cursor: Union[Unset, str] = UNSET
    before_cursor: Union[Unset, str] = UNSET
    has_more: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after_cursor = self.after_cursor

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
        after_cursor = d.pop("after_cursor", UNSET)

        before_cursor = d.pop("before_cursor", UNSET)

        has_more = d.pop("has_more", UNSET)

        unified_search_result_set_meta = cls(
            after_cursor=after_cursor,
            before_cursor=before_cursor,
            has_more=has_more,
        )

        unified_search_result_set_meta.additional_properties = d
        return unified_search_result_set_meta

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
