import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostObject")


@_attrs_define
class PostObject:
    """
    Example:
        {'author_id': 3465, 'featured': True, 'id': 1635, 'title': 'The post'}

    Attributes:
        title (str): The title of the post
        author_id (Union[Unset, int]): The id of the author of the post. *Writable on create by Help Center managers --
            see Create Post
        closed (Union[Unset, bool]): Whether further comments are allowed
        comment_count (Union[Unset, int]): The number of comments on the post
        content_tag_ids (Union[Unset, list[int]]): The list of content tags attached to the post
        created_at (Union[Unset, datetime.datetime]): When the post was created. Writable on create by Help Center
            managers -- see [Create Post](#create-post)
        details (Union[Unset, str]): The details of the post made by the author. See [User content](#user-content)
        featured (Union[Unset, bool]): Whether the post is featured
        follower_count (Union[Unset, int]): The number of followers of the post
        html_url (Union[Unset, str]): The community url of the post
        id (Union[Unset, int]): Automatically assigned when the post is created
        non_author_editor_id (Union[Unset, int]): The user id of whoever performed the most recent (if any) non-author
            edit. A non-author edit consists of an edit make by a user other than the author that creates or updates the
            `title` or `details`. Note that only edits made after May 17, 2021 will be reflected in this field. If no non-
            author edits have occured since May 17, 2021, then this field will be `null`.
        non_author_updated_at (Union[Unset, datetime.datetime]): When the post was last edited by a non-author user
        pinned (Union[Unset, bool]): When true, pins the post to the top of its topic
        status (Union[Unset, str]): The status of the post. Possible values: "planned", "not_planned" , "answered", or
            "completed"
        topic_id (Union[Unset, int]): The id of the topic that the post belongs to
        updated_at (Union[Unset, datetime.datetime]): When the post was last updated
        url (Union[Unset, str]): The API url of the post
        vote_count (Union[Unset, int]): The total number of upvotes and downvotes
        vote_sum (Union[Unset, int]): The sum of upvotes (+1) and downvotes (-1), which may be positive or negative
    """

    title: str
    author_id: Union[Unset, int] = UNSET
    closed: Union[Unset, bool] = UNSET
    comment_count: Union[Unset, int] = UNSET
    content_tag_ids: Union[Unset, list[int]] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    details: Union[Unset, str] = UNSET
    featured: Union[Unset, bool] = UNSET
    follower_count: Union[Unset, int] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    non_author_editor_id: Union[Unset, int] = UNSET
    non_author_updated_at: Union[Unset, datetime.datetime] = UNSET
    pinned: Union[Unset, bool] = UNSET
    status: Union[Unset, str] = UNSET
    topic_id: Union[Unset, int] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    url: Union[Unset, str] = UNSET
    vote_count: Union[Unset, int] = UNSET
    vote_sum: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        author_id = self.author_id

        closed = self.closed

        comment_count = self.comment_count

        content_tag_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.content_tag_ids, Unset):
            content_tag_ids = self.content_tag_ids

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        details = self.details

        featured = self.featured

        follower_count = self.follower_count

        html_url = self.html_url

        id = self.id

        non_author_editor_id = self.non_author_editor_id

        non_author_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.non_author_updated_at, Unset):
            non_author_updated_at = self.non_author_updated_at.isoformat()

        pinned = self.pinned

        status = self.status

        topic_id = self.topic_id

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        url = self.url

        vote_count = self.vote_count

        vote_sum = self.vote_sum

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if closed is not UNSET:
            field_dict["closed"] = closed
        if comment_count is not UNSET:
            field_dict["comment_count"] = comment_count
        if content_tag_ids is not UNSET:
            field_dict["content_tag_ids"] = content_tag_ids
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if details is not UNSET:
            field_dict["details"] = details
        if featured is not UNSET:
            field_dict["featured"] = featured
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if non_author_editor_id is not UNSET:
            field_dict["non_author_editor_id"] = non_author_editor_id
        if non_author_updated_at is not UNSET:
            field_dict["non_author_updated_at"] = non_author_updated_at
        if pinned is not UNSET:
            field_dict["pinned"] = pinned
        if status is not UNSET:
            field_dict["status"] = status
        if topic_id is not UNSET:
            field_dict["topic_id"] = topic_id
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
        title = d.pop("title")

        author_id = d.pop("author_id", UNSET)

        closed = d.pop("closed", UNSET)

        comment_count = d.pop("comment_count", UNSET)

        content_tag_ids = cast(list[int], d.pop("content_tag_ids", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        details = d.pop("details", UNSET)

        featured = d.pop("featured", UNSET)

        follower_count = d.pop("follower_count", UNSET)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        non_author_editor_id = d.pop("non_author_editor_id", UNSET)

        _non_author_updated_at = d.pop("non_author_updated_at", UNSET)
        non_author_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_non_author_updated_at, Unset):
            non_author_updated_at = UNSET
        else:
            non_author_updated_at = isoparse(_non_author_updated_at)

        pinned = d.pop("pinned", UNSET)

        status = d.pop("status", UNSET)

        topic_id = d.pop("topic_id", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        url = d.pop("url", UNSET)

        vote_count = d.pop("vote_count", UNSET)

        vote_sum = d.pop("vote_sum", UNSET)

        post_object = cls(
            title=title,
            author_id=author_id,
            closed=closed,
            comment_count=comment_count,
            content_tag_ids=content_tag_ids,
            created_at=created_at,
            details=details,
            featured=featured,
            follower_count=follower_count,
            html_url=html_url,
            id=id,
            non_author_editor_id=non_author_editor_id,
            non_author_updated_at=non_author_updated_at,
            pinned=pinned,
            status=status,
            topic_id=topic_id,
            updated_at=updated_at,
            url=url,
            vote_count=vote_count,
            vote_sum=vote_sum,
        )

        post_object.additional_properties = d
        return post_object

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
