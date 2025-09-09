from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.vote_response import VoteResponse
from ...types import Response


def _get_kwargs(
    vote_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/help_center/votes/{vote_id}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[VoteResponse]:
    if response.status_code == 200:
        response_200 = VoteResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[VoteResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vote_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[VoteResponse]:
    """Show Vote

     #### Allowed for

    * End users

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | users         | authors
    | articles      | articles
    | translations  | translations of any sideloaded articles
    | posts         | posts
    | comments      | comments

    Note that you must sideload `articles` in order to sideload `translations`.

    Args:
        vote_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VoteResponse]
    """

    kwargs = _get_kwargs(
        vote_id=vote_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vote_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[VoteResponse]:
    """Show Vote

     #### Allowed for

    * End users

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | users         | authors
    | articles      | articles
    | translations  | translations of any sideloaded articles
    | posts         | posts
    | comments      | comments

    Note that you must sideload `articles` in order to sideload `translations`.

    Args:
        vote_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VoteResponse
    """

    return sync_detailed(
        vote_id=vote_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    vote_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[VoteResponse]:
    """Show Vote

     #### Allowed for

    * End users

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | users         | authors
    | articles      | articles
    | translations  | translations of any sideloaded articles
    | posts         | posts
    | comments      | comments

    Note that you must sideload `articles` in order to sideload `translations`.

    Args:
        vote_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VoteResponse]
    """

    kwargs = _get_kwargs(
        vote_id=vote_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vote_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[VoteResponse]:
    """Show Vote

     #### Allowed for

    * End users

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | users         | authors
    | articles      | articles
    | translations  | translations of any sideloaded articles
    | posts         | posts
    | comments      | comments

    Note that you must sideload `articles` in order to sideload `translations`.

    Args:
        vote_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VoteResponse
    """

    return (
        await asyncio_detailed(
            vote_id=vote_id,
            client=client,
        )
    ).parsed
