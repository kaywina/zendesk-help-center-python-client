from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.subscription_response import SubscriptionResponse
from ...types import Response


def _get_kwargs(
    post_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v2/community/posts/{post_id}/subscriptions",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SubscriptionResponse]:
    if response.status_code == 201:
        response_201 = SubscriptionResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SubscriptionResponse]:
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
) -> Response[SubscriptionResponse]:
    """Create Post Subscription

     Creates a subscription to a given [post](/api-reference/help_center/help-center-api/posts).

    #### Allowed for

    * End users

    Agents with the Help Center manager role can optionally supply a
    `subscription` object containing a `user_id` value. If provided,
    the user associated with `user_id` will be subscrbed to the post.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        post_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubscriptionResponse]
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
) -> Optional[SubscriptionResponse]:
    """Create Post Subscription

     Creates a subscription to a given [post](/api-reference/help_center/help-center-api/posts).

    #### Allowed for

    * End users

    Agents with the Help Center manager role can optionally supply a
    `subscription` object containing a `user_id` value. If provided,
    the user associated with `user_id` will be subscrbed to the post.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        post_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubscriptionResponse
    """

    return sync_detailed(
        post_id=post_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    post_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SubscriptionResponse]:
    """Create Post Subscription

     Creates a subscription to a given [post](/api-reference/help_center/help-center-api/posts).

    #### Allowed for

    * End users

    Agents with the Help Center manager role can optionally supply a
    `subscription` object containing a `user_id` value. If provided,
    the user associated with `user_id` will be subscrbed to the post.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        post_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubscriptionResponse]
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
) -> Optional[SubscriptionResponse]:
    """Create Post Subscription

     Creates a subscription to a given [post](/api-reference/help_center/help-center-api/posts).

    #### Allowed for

    * End users

    Agents with the Help Center manager role can optionally supply a
    `subscription` object containing a `user_id` value. If provided,
    the user associated with `user_id` will be subscrbed to the post.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        post_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubscriptionResponse
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            client=client,
        )
    ).parsed
