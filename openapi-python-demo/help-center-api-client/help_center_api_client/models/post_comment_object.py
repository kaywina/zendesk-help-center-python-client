import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostCommentObject")


@_attrs_define
class PostCommentObject:
    """
    Example:
        {'author_id': 89567, 'body': 'My printer is on fire!', 'id': 35467, 'official': False, 'vote_count': 15,
            'vote_sum': 10}

    Attributes:
        body (str): The comment made by the author. See [User content](#user-content)
        author_id (Union[Unset, int]): The id of the author of the comment. Writable on create by Help Center managers.
            See [Create Post Comment](#create-post-comment)
        created_at (Union[Unset, str]): When the comment was created. Writable on create by Help Center managers. See
            [Create Post Comment](#create-post-comment)
        html_url (Union[Unset, str]): The community url of the comment
        id (Union[Unset, int]): Automatically assigned when the comment is created
        non_author_editor_id (Union[Unset, int]): The user id of whoever performed the most recent (if any) non-author
            edit. A non-author edit consists of an edit make by a user other than the author that creates or updates the
            `body`. Note that only edits made after May 17, 2021 will be reflected in this field. If no non-author edits
            have occured since May 17, 2021, then this field will be `null`.
        non_author_updated_at (Union[Unset, datetime.datetime]): When the comment was last edited by a non-author user
        official (Union[Unset, bool]): Whether the comment is marked as official
        post_id (Union[Unset, int]): The id of the post on which the comment was made
        updated_at (Union[Unset, str]): When the comment was last updated
        url (Union[Unset, str]): The API url of the comment
        vote_count (Union[Unset, int]): The total number of upvotes and downvotes
        vote_sum (Union[Unset, int]): The sum of upvotes (+1) and downvotes (-1), which may be positive or negative
    """

    body: str
    author_id: Union[Unset, int] = UNSET
    created_at: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    non_author_editor_id: Union[Unset, int] = UNSET
    non_author_updated_at: Union[Unset, datetime.datetime] = UNSET
    official: Union[Unset, bool] = UNSET
    post_id: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vote_count: Union[Unset, int] = UNSET
    vote_sum: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        author_id = self.author_id

        created_at = self.created_at

        html_url = self.html_url

        id = self.id

        non_author_editor_id = self.non_author_editor_id

        non_author_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.non_author_updated_at, Unset):
            non_author_updated_at = self.non_author_updated_at.isoformat()

        official = self.official

        post_id = self.post_id

        updated_at = self.updated_at

        url = self.url

        vote_count = self.vote_count

        vote_sum = self.vote_sum

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
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
        if official is not UNSET:
            field_dict["official"] = official
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
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

        official = d.pop("official", UNSET)

        post_id = d.pop("post_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        vote_count = d.pop("vote_count", UNSET)

        vote_sum = d.pop("vote_sum", UNSET)

        post_comment_object = cls(
            body=body,
            author_id=author_id,
            created_at=created_at,
            html_url=html_url,
            id=id,
            non_author_editor_id=non_author_editor_id,
            non_author_updated_at=non_author_updated_at,
            official=official,
            post_id=post_id,
            updated_at=updated_at,
            url=url,
            vote_count=vote_count,
            vote_sum=vote_sum,
        )

        post_comment_object.additional_properties = d
        return post_comment_object

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
