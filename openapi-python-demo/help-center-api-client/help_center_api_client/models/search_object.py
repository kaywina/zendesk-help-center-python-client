from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.article_object import ArticleObject
    from ..models.post_comment_object import PostCommentObject


T = TypeVar("T", bound="SearchObject")


@_attrs_define
class SearchObject:
    """
    Attributes:
        results (list[Union['ArticleObject', 'PostCommentObject']]): An array with the base articles or community posts
    """

    results: list[Union["ArticleObject", "PostCommentObject"]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.article_object import ArticleObject

        results = []
        for results_item_data in self.results:
            results_item: dict[str, Any]
            if isinstance(results_item_data, ArticleObject):
                results_item = results_item_data.to_dict()
            else:
                results_item = results_item_data.to_dict()

            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.article_object import ArticleObject
        from ..models.post_comment_object import PostCommentObject

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:

            def _parse_results_item(data: object) -> Union["ArticleObject", "PostCommentObject"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    results_item_type_0 = ArticleObject.from_dict(data)

                    return results_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                results_item_type_1 = PostCommentObject.from_dict(data)

                return results_item_type_1

            results_item = _parse_results_item(results_item_data)

            results.append(results_item)

        search_object = cls(
            results=results,
        )

        search_object.additional_properties = d
        return search_object

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
