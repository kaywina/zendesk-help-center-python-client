from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_object import CategoryObject


T = TypeVar("T", bound="CategoryResponse")


@_attrs_define
class CategoryResponse:
    """
    Attributes:
        category (Union[Unset, CategoryObject]):  Example: {'description': '', 'html_url':
            'https://company.zendesk.com/hc/en-us/categories/354362577', 'id': 1635, 'locale': 'en-us', 'name': 'Self Help
            Articles', 'source_locale': 'en-us', 'url':
            'https://company.zendesk.com/api/v2/help_center/categories/354362577'}.
    """

    category: Union[Unset, "CategoryObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_object import CategoryObject

        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: Union[Unset, CategoryObject]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = CategoryObject.from_dict(_category)

        category_response = cls(
            category=category,
        )

        category_response.additional_properties = d
        return category_response

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
