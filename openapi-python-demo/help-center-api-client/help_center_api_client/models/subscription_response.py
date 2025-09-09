from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_subscription_object import ContentSubscriptionObject


T = TypeVar("T", bound="SubscriptionResponse")


@_attrs_define
class SubscriptionResponse:
    """
    Attributes:
        subscription (Union[Unset, ContentSubscriptionObject]):  Example: {'content_id': 65466, 'created_at':
            '2012-04-04T09:14:57Z', 'id': 1635, 'locale': 'en-us', 'user_id': 3465}.
    """

    subscription: Union[Unset, "ContentSubscriptionObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.subscription, Unset):
            subscription = self.subscription.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscription is not UNSET:
            field_dict["subscription"] = subscription

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_subscription_object import ContentSubscriptionObject

        d = dict(src_dict)
        _subscription = d.pop("subscription", UNSET)
        subscription: Union[Unset, ContentSubscriptionObject]
        if isinstance(_subscription, Unset):
            subscription = UNSET
        else:
            subscription = ContentSubscriptionObject.from_dict(_subscription)

        subscription_response = cls(
            subscription=subscription,
        )

        subscription_response.additional_properties = d
        return subscription_response

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
