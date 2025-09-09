from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.comments_response import CommentsResponse
from ...types import Response


def _get_kwargs(
    locale: str,
    article_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/help_center/{locale}/articles/{article_id}/comments",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CommentsResponse]:
    if response.status_code == 200:
        response_200 = CommentsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CommentsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: str,
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CommentsResponse]:
    """List Comments

     Lists the comments created by a specific user, or all comments made by all users on
    a specific article.

    The `{locale}` for the article comments is required only for end users. Admins and agents can omit
    it.

    #### Allowed for

    * End users

    End-users can only list their own comments. If listing comments by user, they must specify `me` as
    the id.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sideloads

    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | users         | authors
    | articles      | articles

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommentsResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        article_id=article_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: str,
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CommentsResponse]:
    """List Comments

     Lists the comments created by a specific user, or all comments made by all users on
    a specific article.

    The `{locale}` for the article comments is required only for end users. Admins and agents can omit
    it.

    #### Allowed for

    * End users

    End-users can only list their own comments. If listing comments by user, they must specify `me` as
    the id.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sideloads

    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | users         | authors
    | articles      | articles

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommentsResponse
    """

    return sync_detailed(
        locale=locale,
        article_id=article_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    locale: str,
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CommentsResponse]:
    """List Comments

     Lists the comments created by a specific user, or all comments made by all users on
    a specific article.

    The `{locale}` for the article comments is required only for end users. Admins and agents can omit
    it.

    #### Allowed for

    * End users

    End-users can only list their own comments. If listing comments by user, they must specify `me` as
    the id.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sideloads

    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | users         | authors
    | articles      | articles

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommentsResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        article_id=article_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: str,
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CommentsResponse]:
    """List Comments

     Lists the comments created by a specific user, or all comments made by all users on
    a specific article.

    The `{locale}` for the article comments is required only for end users. Admins and agents can omit
    it.

    #### Allowed for

    * End users

    End-users can only list their own comments. If listing comments by user, they must specify `me` as
    the id.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sideloads

    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | users         | authors
    | articles      | articles

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommentsResponse
    """

    return (
        await asyncio_detailed(
            locale=locale,
            article_id=article_id,
            client=client,
        )
    ).parsed
