import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentObject")


@_attrs_define
class CommentObject:
    """
    Example:
        {'author_id': 3465, 'body': 'Thanks for your help!', 'created_at': '2012-04-04T09:14:57Z', 'id': 1635, 'locale':
            'en-us', 'source_id': 65466, 'source_type': 'Article'}

    Attributes:
        body (str): The comment made by the author. See [User content](#user-content)
        locale (str): The locale in which this comment was made
        author_id (Union[Unset, int]): The id of the author of this comment. Writable on create by Help Center managers.
            See [Create Comment](#create-comment)
        created_at (Union[Unset, str]): The time the comment was created. Writable on create by Help Center managers.
            See [Create Comment](#create-comment)
        html_url (Union[Unset, str]): The url at which the comment is presented in Help Center
        id (Union[Unset, int]): Automatically assigned when the comment is created
        non_author_editor_id (Union[Unset, int]): The user id of whoever performed the most recent (if any) non-author
            edit. A non-author edit consists of an edit make by a user other than the author that creates or updates the
            `body` or `author_id`. Note that only edits made after May 17, 2021 will be reflected in this field. If no non-
            author edits have occured since May 17, 2021, then this field will be `null`.
        non_author_updated_at (Union[Unset, datetime.datetime]): When the comment was last edited by a non-author user
        source_id (Union[Unset, int]): The id of the item on which this comment was made
        source_type (Union[Unset, str]): The type of the item on which this comment was made. Currently only supports
            'Article'
        updated_at (Union[Unset, str]): The time at which the comment was last updated
        url (Union[Unset, str]): The API url of this comment
        vote_count (Union[Unset, int]): The total number of upvotes and downvotes
        vote_sum (Union[Unset, int]): The sum of upvotes (+1) and downvotes (-1), which may be positive or negative
    """

    body: str
    locale: str
    author_id: Union[Unset, int] = UNSET
    created_at: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    non_author_editor_id: Union[Unset, int] = UNSET
    non_author_updated_at: Union[Unset, datetime.datetime] = UNSET
    source_id: Union[Unset, int] = UNSET
    source_type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vote_count: Union[Unset, int] = UNSET
    vote_sum: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        locale = self.locale

        author_id = self.author_id

        created_at = self.created_at

        html_url = self.html_url

        id = self.id

        non_author_editor_id = self.non_author_editor_id

        non_author_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.non_author_updated_at, Unset):
            non_author_updated_at = self.non_author_updated_at.isoformat()

        source_id = self.source_id

        source_type = self.source_type

        updated_at = self.updated_at

        url = self.url

        vote_count = self.vote_count

        vote_sum = self.vote_sum

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "locale": locale,
            }
        )
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if non_author_editor_id is not UNSET:
            field_dict["non_author_editor_id"] = non_author_editor_id
        if non_author_updated_at is not UNSET:
            field_dict["non_author_updated_at"] = non_author_updated_at
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if vote_count is not UNSET:
            field_dict["vote_count"] = vote_count
        if vote_sum is not UNSET:
            field_dict["vote_sum"] = vote_sum

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body")

        locale = d.pop("locale")

        author_id = d.pop("author_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        non_author_editor_id = d.pop("non_author_editor_id", UNSET)

        _non_author_updated_at = d.pop("non_author_updated_at", UNSET)
        non_author_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_non_author_updated_at, Unset):
            non_author_updated_at = UNSET
        else:
            non_author_updated_at = isoparse(_non_author_updated_at)

        source_id = d.pop("source_id", UNSET)

        source_type = d.pop("source_type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        vote_count = d.pop("vote_count", UNSET)

        vote_sum = d.pop("vote_sum", UNSET)

        comment_object = cls(
            body=body,
            locale=locale,
            author_id=author_id,
            created_at=created_at,
            html_url=html_url,
            id=id,
            non_author_editor_id=non_author_editor_id,
            non_author_updated_at=non_author_updated_at,
            source_id=source_id,
            source_type=source_type,
            updated_at=updated_at,
            url=url,
            vote_count=vote_count,
            vote_sum=vote_sum,
        )

        comment_object.additional_properties = d
        return comment_object

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
