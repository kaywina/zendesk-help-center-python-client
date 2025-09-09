from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.service_catalog_item_object import ServiceCatalogItemObject
    from ..models.service_catalog_items_response_links import ServiceCatalogItemsResponseLinks
    from ..models.service_catalog_items_response_meta import ServiceCatalogItemsResponseMeta


T = TypeVar("T", bound="ServiceCatalogItemsResponse")


@_attrs_define
class ServiceCatalogItemsResponse:
    """
    Attributes:
        count (int): The total number of service catalog items returned in the response
        links (ServiceCatalogItemsResponseLinks): Links to navigate to the next and previous pages of results
        meta (ServiceCatalogItemsResponseMeta): Metadata about the service catalog items
        service_catalog_items (list['ServiceCatalogItemObject']):
    """

    count: int
    links: "ServiceCatalogItemsResponseLinks"
    meta: "ServiceCatalogItemsResponseMeta"
    service_catalog_items: list["ServiceCatalogItemObject"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        links = self.links.to_dict()

        meta = self.meta.to_dict()

        service_catalog_items = []
        for service_catalog_items_item_data in self.service_catalog_items:
            service_catalog_items_item = service_catalog_items_item_data.to_dict()
            service_catalog_items.append(service_catalog_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "links": links,
                "meta": meta,
                "service_catalog_items": service_catalog_items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_catalog_item_object import ServiceCatalogItemObject
        from ..models.service_catalog_items_response_links import ServiceCatalogItemsResponseLinks
        from ..models.service_catalog_items_response_meta import ServiceCatalogItemsResponseMeta

        d = dict(src_dict)
        count = d.pop("count")

        links = ServiceCatalogItemsResponseLinks.from_dict(d.pop("links"))

        meta = ServiceCatalogItemsResponseMeta.from_dict(d.pop("meta"))

        service_catalog_items = []
        _service_catalog_items = d.pop("service_catalog_items")
        for service_catalog_items_item_data in _service_catalog_items:
            service_catalog_items_item = ServiceCatalogItemObject.from_dict(service_catalog_items_item_data)

            service_catalog_items.append(service_catalog_items_item)

        service_catalog_items_response = cls(
            count=count,
            links=links,
            meta=meta,
            service_catalog_items=service_catalog_items,
        )

        service_catalog_items_response.additional_properties = d
        return service_catalog_items_response

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
