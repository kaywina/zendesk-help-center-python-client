from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCatalogItemObject")


@_attrs_define
class ServiceCatalogItemObject:
    """
    Attributes:
        description (str): The description of the service catalog item
        name (str): The name of the service catalog item
        form_id (Union[Unset, int]): The id of the form the service catalog item is associated with
        id (Union[Unset, str]): Automatically assigned when the service catalog item is created
        thumbnail_url (Union[None, Unset, str]): The url of the thumbnail image for the service catalog item
    """

    description: str
    name: str
    form_id: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    thumbnail_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        form_id = self.form_id

        id = self.id

        thumbnail_url: Union[None, Unset, str]
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
            }
        )
        if form_id is not UNSET:
            field_dict["form_id"] = form_id
        if id is not UNSET:
            field_dict["id"] = id
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        name = d.pop("name")

        form_id = d.pop("form_id", UNSET)

        id = d.pop("id", UNSET)

        def _parse_thumbnail_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnail_url", UNSET))

        service_catalog_item_object = cls(
            description=description,
            name=name,
            form_id=form_id,
            id=id,
            thumbnail_url=thumbnail_url,
        )

        service_catalog_item_object.additional_properties = d
        return service_catalog_item_object

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
