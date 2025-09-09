from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentSubscriptionObject")


@_attrs_define
class ContentSubscriptionObject:
    """
    Example:
        {'content_id': 65466, 'created_at': '2012-04-04T09:14:57Z', 'id': 1635, 'locale': 'en-us', 'user_id': 3465}

    Attributes:
        locale (str): The locale of the subscribed item
        content_id (Union[Unset, int]): The id of the subscribed item
        content_type (Union[Unset, str]): The type of the subscribed item
        created_at (Union[Unset, str]): The time at which the subscription was created
        id (Union[Unset, int]): Automatically assigned when the subscription is created
        include_comments (Union[Unset, bool]): Subscribe also to article comments / post comments. Only for section /
            topic subscriptions.
        source_locale (Union[Unset, str]): Used only for [Create Section Subscription](#create-section-subscription) and
            [Create Article Subscription](#create-article-subscription), where it's mandatory. Selects the locale of the
            content to be subscribed
        updated_at (Union[Unset, str]): The time at which the subscription was last updated
        url (Union[Unset, str]): The API url of the subscription
        user_id (Union[Unset, int]): The id of the user who has this subscription
    """

    locale: str
    content_id: Union[Unset, int] = UNSET
    content_type: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    include_comments: Union[Unset, bool] = UNSET
    source_locale: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        content_id = self.content_id

        content_type = self.content_type

        created_at = self.created_at

        id = self.id

        include_comments = self.include_comments

        source_locale = self.source_locale

        updated_at = self.updated_at

        url = self.url

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locale": locale,
            }
        )
        if content_id is not UNSET:
            field_dict["content_id"] = content_id
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if include_comments is not UNSET:
            field_dict["include_comments"] = include_comments
        if source_locale is not UNSET:
            field_dict["source_locale"] = source_locale
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        locale = d.pop("locale")

        content_id = d.pop("content_id", UNSET)

        content_type = d.pop("content_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        include_comments = d.pop("include_comments", UNSET)

        source_locale = d.pop("source_locale", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        user_id = d.pop("user_id", UNSET)

        content_subscription_object = cls(
            locale=locale,
            content_id=content_id,
            content_type=content_type,
            created_at=created_at,
            id=id,
            include_comments=include_comments,
            source_locale=source_locale,
            updated_at=updated_at,
            url=url,
            user_id=user_id,
        )

        content_subscription_object.additional_properties = d
        return content_subscription_object

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
