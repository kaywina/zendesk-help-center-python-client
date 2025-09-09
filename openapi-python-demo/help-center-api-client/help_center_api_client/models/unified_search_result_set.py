from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unified_search_result import UnifiedSearchResult
    from ..models.unified_search_result_set_meta import UnifiedSearchResultSetMeta


T = TypeVar("T", bound="UnifiedSearchResultSet")


@_attrs_define
class UnifiedSearchResultSet:
    """
    Attributes:
        meta (Union[Unset, UnifiedSearchResultSetMeta]):
        results (Union[Unset, list['UnifiedSearchResult']]):
    """

    meta: Union[Unset, "UnifiedSearchResultSetMeta"] = UNSET
    results: Union[Unset, list["UnifiedSearchResult"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unified_search_result import UnifiedSearchResult
        from ..models.unified_search_result_set_meta import UnifiedSearchResultSetMeta

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, UnifiedSearchResultSetMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = UnifiedSearchResultSetMeta.from_dict(_meta)

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = UnifiedSearchResult.from_dict(results_item_data)

            results.append(results_item)

        unified_search_result_set = cls(
            meta=meta,
            results=results,
        )

        unified_search_result_set.additional_properties = d
        return unified_search_result_set

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
