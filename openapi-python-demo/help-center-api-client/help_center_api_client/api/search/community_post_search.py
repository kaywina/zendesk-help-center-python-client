import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.community_post_search_response import CommunityPostSearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    topic: Union[Unset, int] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_at: Union[Unset, datetime.datetime] = UNSET,
    updated_before: Union[Unset, datetime.datetime] = UNSET,
    updated_after: Union[Unset, datetime.datetime] = UNSET,
    updated_at: Union[Unset, datetime.datetime] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    params["topic"] = topic

    json_created_before: Union[Unset, str] = UNSET
    if not isinstance(created_before, Unset):
        json_created_before = created_before.isoformat()
    params["created_before"] = json_created_before

    json_created_after: Union[Unset, str] = UNSET
    if not isinstance(created_after, Unset):
        json_created_after = created_after.isoformat()
    params["created_after"] = json_created_after

    json_created_at: Union[Unset, str] = UNSET
    if not isinstance(created_at, Unset):
        json_created_at = created_at.isoformat()
    params["created_at"] = json_created_at

    json_updated_before: Union[Unset, str] = UNSET
    if not isinstance(updated_before, Unset):
        json_updated_before = updated_before.isoformat()
    params["updated_before"] = json_updated_before

    json_updated_after: Union[Unset, str] = UNSET
    if not isinstance(updated_after, Unset):
        json_updated_after = updated_after.isoformat()
    params["updated_after"] = json_updated_after

    json_updated_at: Union[Unset, str] = UNSET
    if not isinstance(updated_at, Unset):
        json_updated_at = updated_at.isoformat()
    params["updated_at"] = json_updated_at

    params["sort_by"] = sort_by

    params["sort_order"] = sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/help_center/community_posts/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CommunityPostSearchResponse]:
    if response.status_code == 200:
        response_200 = CommunityPostSearchResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CommunityPostSearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    topic: Union[Unset, int] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_at: Union[Unset, datetime.datetime] = UNSET,
    updated_before: Union[Unset, datetime.datetime] = UNSET,
    updated_after: Union[Unset, datetime.datetime] = UNSET,
    updated_at: Union[Unset, datetime.datetime] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
) -> Response[CommunityPostSearchResponse]:
    """Search Posts

     Returns a maximum of 25 posts per page, up to a maximum of 1000 results. See [Pagination](/api-
    reference/introduction/pagination/).

    The results are sorted by relevance by default. You can also sort the results by `created_at` or
    `updated_at`.

    #### Pagination

    - Offset pagination only

    See [Pagination](/api-reference/introduction/pagination/).

    Returns a maximum of 100 articles per page.

    #### Allowed for

    * End users

    Args:
        query (str):
        topic (Union[Unset, int]):
        created_before (Union[Unset, datetime.datetime]):
        created_after (Union[Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        updated_before (Union[Unset, datetime.datetime]):
        updated_after (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        sort_by (Union[Unset, str]):
        sort_order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommunityPostSearchResponse]
    """

    kwargs = _get_kwargs(
        query=query,
        topic=topic,
        created_before=created_before,
        created_after=created_after,
        created_at=created_at,
        updated_before=updated_before,
        updated_after=updated_after,
        updated_at=updated_at,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    topic: Union[Unset, int] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_at: Union[Unset, datetime.datetime] = UNSET,
    updated_before: Union[Unset, datetime.datetime] = UNSET,
    updated_after: Union[Unset, datetime.datetime] = UNSET,
    updated_at: Union[Unset, datetime.datetime] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
) -> Optional[CommunityPostSearchResponse]:
    """Search Posts

     Returns a maximum of 25 posts per page, up to a maximum of 1000 results. See [Pagination](/api-
    reference/introduction/pagination/).

    The results are sorted by relevance by default. You can also sort the results by `created_at` or
    `updated_at`.

    #### Pagination

    - Offset pagination only

    See [Pagination](/api-reference/introduction/pagination/).

    Returns a maximum of 100 articles per page.

    #### Allowed for

    * End users

    Args:
        query (str):
        topic (Union[Unset, int]):
        created_before (Union[Unset, datetime.datetime]):
        created_after (Union[Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        updated_before (Union[Unset, datetime.datetime]):
        updated_after (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        sort_by (Union[Unset, str]):
        sort_order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommunityPostSearchResponse
    """

    return sync_detailed(
        client=client,
        query=query,
        topic=topic,
        created_before=created_before,
        created_after=created_after,
        created_at=created_at,
        updated_before=updated_before,
        updated_after=updated_after,
        updated_at=updated_at,
        sort_by=sort_by,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    topic: Union[Unset, int] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_at: Union[Unset, datetime.datetime] = UNSET,
    updated_before: Union[Unset, datetime.datetime] = UNSET,
    updated_after: Union[Unset, datetime.datetime] = UNSET,
    updated_at: Union[Unset, datetime.datetime] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
) -> Response[CommunityPostSearchResponse]:
    """Search Posts

     Returns a maximum of 25 posts per page, up to a maximum of 1000 results. See [Pagination](/api-
    reference/introduction/pagination/).

    The results are sorted by relevance by default. You can also sort the results by `created_at` or
    `updated_at`.

    #### Pagination

    - Offset pagination only

    See [Pagination](/api-reference/introduction/pagination/).

    Returns a maximum of 100 articles per page.

    #### Allowed for

    * End users

    Args:
        query (str):
        topic (Union[Unset, int]):
        created_before (Union[Unset, datetime.datetime]):
        created_after (Union[Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        updated_before (Union[Unset, datetime.datetime]):
        updated_after (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        sort_by (Union[Unset, str]):
        sort_order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommunityPostSearchResponse]
    """

    kwargs = _get_kwargs(
        query=query,
        topic=topic,
        created_before=created_before,
        created_after=created_after,
        created_at=created_at,
        updated_before=updated_before,
        updated_after=updated_after,
        updated_at=updated_at,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    topic: Union[Unset, int] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_at: Union[Unset, datetime.datetime] = UNSET,
    updated_before: Union[Unset, datetime.datetime] = UNSET,
    updated_after: Union[Unset, datetime.datetime] = UNSET,
    updated_at: Union[Unset, datetime.datetime] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
) -> Optional[CommunityPostSearchResponse]:
    """Search Posts

     Returns a maximum of 25 posts per page, up to a maximum of 1000 results. See [Pagination](/api-
    reference/introduction/pagination/).

    The results are sorted by relevance by default. You can also sort the results by `created_at` or
    `updated_at`.

    #### Pagination

    - Offset pagination only

    See [Pagination](/api-reference/introduction/pagination/).

    Returns a maximum of 100 articles per page.

    #### Allowed for

    * End users

    Args:
        query (str):
        topic (Union[Unset, int]):
        created_before (Union[Unset, datetime.datetime]):
        created_after (Union[Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        updated_before (Union[Unset, datetime.datetime]):
        updated_after (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        sort_by (Union[Unset, str]):
        sort_order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommunityPostSearchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            topic=topic,
            created_before=created_before,
            created_after=created_after,
            created_at=created_at,
            updated_before=updated_before,
            updated_after=updated_after,
            updated_at=updated_at,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    ).parsed
