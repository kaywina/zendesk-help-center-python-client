from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_catalog_item_object import ServiceCatalogItemObject


T = TypeVar("T", bound="ServiceCatalogItemResponse")


@_attrs_define
class ServiceCatalogItemResponse:
    """
    Attributes:
        service_catalog_item (Union[Unset, ServiceCatalogItemObject]):
    """

    service_catalog_item: Union[Unset, "ServiceCatalogItemObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_catalog_item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.service_catalog_item, Unset):
            service_catalog_item = self.service_catalog_item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_catalog_item is not UNSET:
            field_dict["service_catalog_item"] = service_catalog_item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_catalog_item_object import ServiceCatalogItemObject

        d = dict(src_dict)
        _service_catalog_item = d.pop("service_catalog_item", UNSET)
        service_catalog_item: Union[Unset, ServiceCatalogItemObject]
        if isinstance(_service_catalog_item, Unset):
            service_catalog_item = UNSET
        else:
            service_catalog_item = ServiceCatalogItemObject.from_dict(_service_catalog_item)

        service_catalog_item_response = cls(
            service_catalog_item=service_catalog_item,
        )

        service_catalog_item_response.additional_properties = d
        return service_catalog_item_response

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
