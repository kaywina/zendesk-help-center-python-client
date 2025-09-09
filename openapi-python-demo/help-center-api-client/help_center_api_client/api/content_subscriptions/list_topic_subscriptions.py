from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.content_subscriptions_response import ContentSubscriptionsResponse
from ...types import Response


def _get_kwargs(
    topic_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/community/topics/{topic_id}/subscriptions",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ContentSubscriptionsResponse]:
    if response.status_code == 200:
        response_200 = ContentSubscriptionsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ContentSubscriptionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    topic_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ContentSubscriptionsResponse]:
    """List Topic Subscriptions

     Lists the subscriptions to a given topic.

    #### Allowed for

    * End users

    For end users, the response will list only the subscriptions created by the
    requesting end user.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | users         | users
    | topics        | topics

    Args:
        topic_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContentSubscriptionsResponse]
    """

    kwargs = _get_kwargs(
        topic_id=topic_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    topic_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ContentSubscriptionsResponse]:
    """List Topic Subscriptions

     Lists the subscriptions to a given topic.

    #### Allowed for

    * End users

    For end users, the response will list only the subscriptions created by the
    requesting end user.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | users         | users
    | topics        | topics

    Args:
        topic_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContentSubscriptionsResponse
    """

    return sync_detailed(
        topic_id=topic_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    topic_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ContentSubscriptionsResponse]:
    """List Topic Subscriptions

     Lists the subscriptions to a given topic.

    #### Allowed for

    * End users

    For end users, the response will list only the subscriptions created by the
    requesting end user.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | users         | users
    | topics        | topics

    Args:
        topic_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContentSubscriptionsResponse]
    """

    kwargs = _get_kwargs(
        topic_id=topic_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    topic_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ContentSubscriptionsResponse]:
    """List Topic Subscriptions

     Lists the subscriptions to a given topic.

    #### Allowed for

    * End users

    For end users, the response will list only the subscriptions created by the
    requesting end user.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | users         | users
    | topics        | topics

    Args:
        topic_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContentSubscriptionsResponse
    """

    return (
        await asyncio_detailed(
            topic_id=topic_id,
            client=client,
        )
    ).parsed
