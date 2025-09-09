from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.article_object import ArticleObject


T = TypeVar("T", bound="ArticleSearchResponse")


@_attrs_define
class ArticleSearchResponse:
    """
    Attributes:
        result_type (Union[Unset, str]): For articles, always the string `article` Default: 'article'.
        results (Union[Unset, list['ArticleObject']]):
        snippet (Union[Unset, str]): The portion of an article that is relevant to the search query, with matching words
            or phrases delimited by <em></em> tags. Example: a query for `carrot potato` might return the snippet `...don't
            confuse <em>carrots</em> with <em>potatoes</em>...`
    """

    result_type: Union[Unset, str] = "article"
    results: Union[Unset, list["ArticleObject"]] = UNSET
    snippet: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result_type = self.result_type

        results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        snippet = self.snippet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result_type is not UNSET:
            field_dict["result_type"] = result_type
        if results is not UNSET:
            field_dict["results"] = results
        if snippet is not UNSET:
            field_dict["snippet"] = snippet

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.article_object import ArticleObject

        d = dict(src_dict)
        result_type = d.pop("result_type", UNSET)

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = ArticleObject.from_dict(results_item_data)

            results.append(results_item)

        snippet = d.pop("snippet", UNSET)

        article_search_response = cls(
            result_type=result_type,
            results=results,
            snippet=snippet,
        )

        article_search_response.additional_properties = d
        return article_search_response

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
