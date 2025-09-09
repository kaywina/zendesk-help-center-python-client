from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArticleObject")


@_attrs_define
class ArticleObject:
    """
    Example:
        {'author_id': 3465, 'comments_disabled': False, 'id': 1635, 'locale': 'en', 'permission_group_id': 13, 'title':
            'The article', 'user_segment_id': 12}

    Attributes:
        locale (str): The locale that the article is being displayed in
        permission_group_id (int): The id of the permission group which defines who can edit and publish this article
        title (str): The title of the article
        author_id (Union[Unset, int]): The id of the user who wrote the article (set to the user who made the request on
            create by default)
        body (Union[Unset, str]): HTML body of the article. Unsafe tags and attributes may be removed before display.
            For a list of safe tags and attributes, see [Allowing unsafe HTML in Help Center
            articles](https://support.zendesk.com/hc/en-us/articles/115015895948) in Zendesk help
        comments_disabled (Union[Unset, bool]): True if comments are disabled; false otherwise
        content_tag_ids (Union[Unset, list[str]]): The list of content tags attached to the article
        created_at (Union[Unset, str]): The time the article was created
        draft (Union[Unset, bool]): True if the translation for the current locale is a draft; false otherwise. false by
            default. Can be set when creating but not when updating. For updating, see Translations
        edited_at (Union[Unset, str]): The time the article was last edited in its displayed locale
        html_url (Union[Unset, str]): The url of the article in Help Center
        id (Union[Unset, int]): Automatically assigned when the article is created
        label_names (Union[Unset, list[str]]): An array of label names associated with this article. By default no label
            names are used. Only available on certain plans
        outdated (Union[Unset, bool]): Deprecated. Always false because the source translation is always the most up-to-
            date translation
        outdated_locales (Union[Unset, list[str]]): Locales in which the article was marked as outdated
        position (Union[Unset, int]): The position of this article in the article list. 0 by default
        promoted (Union[Unset, bool]): True if this article is promoted; false otherwise. false by default
        section_id (Union[Unset, int]): The id of the section to which this article belongs
        source_locale (Union[Unset, str]): The source (default) locale of the article
        updated_at (Union[Unset, str]): The time the article was last updated
        url (Union[Unset, str]): The API url of the article
        user_segment_id (Union[None, Unset, int]): The id of the user segment which defines who can see this article.
            Set to null to make it accessible to everyone. Either user_segment_id or user_segment_ids must be specified
        user_segment_ids (Union[Unset, list[int]]): List of user segment ids which define who can view this article. Set
            to an empty list to make it accessible to everyone. For Enterprise plans only this may contain more than one
            user_segment_id. Either user_segment_id or user_segment_ids must be specified
        vote_count (Union[Unset, int]): The total number of upvotes and downvotes
        vote_sum (Union[Unset, int]): The sum of upvotes (+1) and downvotes (-1), which may be positive or negative
    """

    locale: str
    permission_group_id: int
    title: str
    author_id: Union[Unset, int] = UNSET
    body: Union[Unset, str] = UNSET
    comments_disabled: Union[Unset, bool] = UNSET
    content_tag_ids: Union[Unset, list[str]] = UNSET
    created_at: Union[Unset, str] = UNSET
    draft: Union[Unset, bool] = UNSET
    edited_at: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    label_names: Union[Unset, list[str]] = UNSET
    outdated: Union[Unset, bool] = UNSET
    outdated_locales: Union[Unset, list[str]] = UNSET
    position: Union[Unset, int] = UNSET
    promoted: Union[Unset, bool] = UNSET
    section_id: Union[Unset, int] = UNSET
    source_locale: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    user_segment_id: Union[None, Unset, int] = UNSET
    user_segment_ids: Union[Unset, list[int]] = UNSET
    vote_count: Union[Unset, int] = UNSET
    vote_sum: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        permission_group_id = self.permission_group_id

        title = self.title

        author_id = self.author_id

        body = self.body

        comments_disabled = self.comments_disabled

        content_tag_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.content_tag_ids, Unset):
            content_tag_ids = self.content_tag_ids

        created_at = self.created_at

        draft = self.draft

        edited_at = self.edited_at

        html_url = self.html_url

        id = self.id

        label_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.label_names, Unset):
            label_names = self.label_names

        outdated = self.outdated

        outdated_locales: Union[Unset, list[str]] = UNSET
        if not isinstance(self.outdated_locales, Unset):
            outdated_locales = self.outdated_locales

        position = self.position

        promoted = self.promoted

        section_id = self.section_id

        source_locale = self.source_locale

        updated_at = self.updated_at

        url = self.url

        user_segment_id: Union[None, Unset, int]
        if isinstance(self.user_segment_id, Unset):
            user_segment_id = UNSET
        else:
            user_segment_id = self.user_segment_id

        user_segment_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.user_segment_ids, Unset):
            user_segment_ids = self.user_segment_ids

        vote_count = self.vote_count

        vote_sum = self.vote_sum

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locale": locale,
                "permission_group_id": permission_group_id,
                "title": title,
            }
        )
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if body is not UNSET:
            field_dict["body"] = body
        if comments_disabled is not UNSET:
            field_dict["comments_disabled"] = comments_disabled
        if content_tag_ids is not UNSET:
            field_dict["content_tag_ids"] = content_tag_ids
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if draft is not UNSET:
            field_dict["draft"] = draft
        if edited_at is not UNSET:
            field_dict["edited_at"] = edited_at
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if label_names is not UNSET:
            field_dict["label_names"] = label_names
        if outdated is not UNSET:
            field_dict["outdated"] = outdated
        if outdated_locales is not UNSET:
            field_dict["outdated_locales"] = outdated_locales
        if position is not UNSET:
            field_dict["position"] = position
        if promoted is not UNSET:
            field_dict["promoted"] = promoted
        if section_id is not UNSET:
            field_dict["section_id"] = section_id
        if source_locale is not UNSET:
            field_dict["source_locale"] = source_locale
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if user_segment_id is not UNSET:
            field_dict["user_segment_id"] = user_segment_id
        if user_segment_ids is not UNSET:
            field_dict["user_segment_ids"] = user_segment_ids
        if vote_count is not UNSET:
            field_dict["vote_count"] = vote_count
        if vote_sum is not UNSET:
            field_dict["vote_sum"] = vote_sum

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        locale = d.pop("locale")

        permission_group_id = d.pop("permission_group_id")

        title = d.pop("title")

        author_id = d.pop("author_id", UNSET)

        body = d.pop("body", UNSET)

        comments_disabled = d.pop("comments_disabled", UNSET)

        content_tag_ids = cast(list[str], d.pop("content_tag_ids", UNSET))

        created_at = d.pop("created_at", UNSET)

        draft = d.pop("draft", UNSET)

        edited_at = d.pop("edited_at", UNSET)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        label_names = cast(list[str], d.pop("label_names", UNSET))

        outdated = d.pop("outdated", UNSET)

        outdated_locales = cast(list[str], d.pop("outdated_locales", UNSET))

        position = d.pop("position", UNSET)

        promoted = d.pop("promoted", UNSET)

        section_id = d.pop("section_id", UNSET)

        source_locale = d.pop("source_locale", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        def _parse_user_segment_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        user_segment_id = _parse_user_segment_id(d.pop("user_segment_id", UNSET))

        user_segment_ids = cast(list[int], d.pop("user_segment_ids", UNSET))

        vote_count = d.pop("vote_count", UNSET)

        vote_sum = d.pop("vote_sum", UNSET)

        article_object = cls(
            locale=locale,
            permission_group_id=permission_group_id,
            title=title,
            author_id=author_id,
            body=body,
            comments_disabled=comments_disabled,
            content_tag_ids=content_tag_ids,
            created_at=created_at,
            draft=draft,
            edited_at=edited_at,
            html_url=html_url,
            id=id,
            label_names=label_names,
            outdated=outdated,
            outdated_locales=outdated_locales,
            position=position,
            promoted=promoted,
            section_id=section_id,
            source_locale=source_locale,
            updated_at=updated_at,
            url=url,
            user_segment_id=user_segment_id,
            user_segment_ids=user_segment_ids,
            vote_count=vote_count,
            vote_sum=vote_sum,
        )

        article_object.additional_properties = d
        return article_object

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
