from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_posts_filter_by import ListPostsFilterBy
from ...models.list_posts_sort_by import ListPostsSortBy
from ...models.posts_response import PostsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_by: Union[Unset, ListPostsFilterBy] = UNSET,
    sort_by: Union[Unset, ListPostsSortBy] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_filter_by: Union[Unset, str] = UNSET
    if not isinstance(filter_by, Unset):
        json_filter_by = filter_by.value

    params["filter_by"] = json_filter_by

    json_sort_by: Union[Unset, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/community/posts",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PostsResponse]:
    if response.status_code == 200:
        response_200 = PostsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PostsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filter_by: Union[Unset, ListPostsFilterBy] = UNSET,
    sort_by: Union[Unset, ListPostsSortBy] = UNSET,
) -> Response[PostsResponse]:
    """List Posts

    Args:
        filter_by (Union[Unset, ListPostsFilterBy]):
        sort_by (Union[Unset, ListPostsSortBy]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostsResponse]
    """

    kwargs = _get_kwargs(
        filter_by=filter_by,
        sort_by=sort_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    filter_by: Union[Unset, ListPostsFilterBy] = UNSET,
    sort_by: Union[Unset, ListPostsSortBy] = UNSET,
) -> Optional[PostsResponse]:
    """List Posts

    Args:
        filter_by (Union[Unset, ListPostsFilterBy]):
        sort_by (Union[Unset, ListPostsSortBy]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostsResponse
    """

    return sync_detailed(
        client=client,
        filter_by=filter_by,
        sort_by=sort_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filter_by: Union[Unset, ListPostsFilterBy] = UNSET,
    sort_by: Union[Unset, ListPostsSortBy] = UNSET,
) -> Response[PostsResponse]:
    """List Posts

    Args:
        filter_by (Union[Unset, ListPostsFilterBy]):
        sort_by (Union[Unset, ListPostsSortBy]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostsResponse]
    """

    kwargs = _get_kwargs(
        filter_by=filter_by,
        sort_by=sort_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    filter_by: Union[Unset, ListPostsFilterBy] = UNSET,
    sort_by: Union[Unset, ListPostsSortBy] = UNSET,
) -> Optional[PostsResponse]:
    """List Posts

    Args:
        filter_by (Union[Unset, ListPostsFilterBy]):
        sort_by (Union[Unset, ListPostsSortBy]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_by=filter_by,
            sort_by=sort_by,
        )
    ).parsed
