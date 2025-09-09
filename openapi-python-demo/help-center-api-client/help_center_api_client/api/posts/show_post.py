from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_response import PostResponse
from ...types import Response


def _get_kwargs(
    post_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/community/posts/{post_id}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PostResponse]:
    if response.status_code == 200:
        response_200 = PostResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PostResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    post_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PostResponse]:
    """Show Post

     Gets information about a given post.

    #### Allowed for

    * Anonymous users

    #### Sideloads
    The following sideloads are supported:

    | Name        | Will sideload
    |-------------|--------------
    | users       | authors
    | topics      | topics

    Args:
        post_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    post_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PostResponse]:
    """Show Post

     Gets information about a given post.

    #### Allowed for

    * Anonymous users

    #### Sideloads
    The following sideloads are supported:

    | Name        | Will sideload
    |-------------|--------------
    | users       | authors
    | topics      | topics

    Args:
        post_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostResponse
    """

    return sync_detailed(
        post_id=post_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    post_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PostResponse]:
    """Show Post

     Gets information about a given post.

    #### Allowed for

    * Anonymous users

    #### Sideloads
    The following sideloads are supported:

    | Name        | Will sideload
    |-------------|--------------
    | users       | authors
    | topics      | topics

    Args:
        post_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    post_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PostResponse]:
    """Show Post

     Gets information about a given post.

    #### Allowed for

    * Anonymous users

    #### Sideloads
    The following sideloads are supported:

    | Name        | Will sideload
    |-------------|--------------
    | users       | authors
    | topics      | topics

    Args:
        post_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostResponse
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            client=client,
        )
    ).parsed
