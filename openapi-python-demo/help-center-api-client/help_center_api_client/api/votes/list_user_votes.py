from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.votes_response import VotesResponse
from ...types import Response


def _get_kwargs(
    user_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/help_center/users/{user_id}/votes",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[VotesResponse]:
    if response.status_code == 200:
        response_200 = VotesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[VotesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[VotesResponse]:
    """List Votes

     Lists all votes cast by a given user, or all votes cast by all users for a given article, article
    comment, post, or post comment.

    To list only your own votes, specify `me` as the user id.

    The `{locale}` for article and article comment votes is required only for end users. Admins and
    agents can omit it.

    #### Allowed for

    * End users

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VotesResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[VotesResponse]:
    """List Votes

     Lists all votes cast by a given user, or all votes cast by all users for a given article, article
    comment, post, or post comment.

    To list only your own votes, specify `me` as the user id.

    The `{locale}` for article and article comment votes is required only for end users. Admins and
    agents can omit it.

    #### Allowed for

    * End users

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VotesResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[VotesResponse]:
    """List Votes

     Lists all votes cast by a given user, or all votes cast by all users for a given article, article
    comment, post, or post comment.

    To list only your own votes, specify `me` as the user id.

    The `{locale}` for article and article comment votes is required only for end users. Admins and
    agents can omit it.

    #### Allowed for

    * End users

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VotesResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[VotesResponse]:
    """List Votes

     Lists all votes cast by a given user, or all votes cast by all users for a given article, article
    comment, post, or post comment.

    To list only your own votes, specify `me` as the user id.

    The `{locale}` for article and article comment votes is required only for end users. Admins and
    agents can omit it.

    #### Allowed for

    * End users

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VotesResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
