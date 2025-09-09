from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.subscription_response import SubscriptionResponse
from ...types import Response


def _get_kwargs(
    locale: str,
    article_id: int,
    subscription_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/help_center/{locale}/articles/{article_id}/subscriptions/{subscription_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SubscriptionResponse]:
    if response.status_code == 200:
        response_200 = SubscriptionResponse.from_dict(response.json())

        return response_200

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
    locale: str,
    article_id: int,
    subscription_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SubscriptionResponse]:
    """Show Article Subscription

     **Note**: `{/locale}` is an optional parameter for admins and agents. End users and anonymous users
    must provide the parameter.

    #### Allowed for

    * End users

    For end-users, the response will only show a subscription created by the requesting end-user.

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload | For
    |---------------|---------------|----
    | users         | users         | all
    | articles      | articles      | article subscriptions
    | sections      | sections      | section subscriptions

    Args:
        locale (str):  Example: en-us.
        article_id (int):
        subscription_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubscriptionResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        article_id=article_id,
        subscription_id=subscription_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: str,
    article_id: int,
    subscription_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[SubscriptionResponse]:
    """Show Article Subscription

     **Note**: `{/locale}` is an optional parameter for admins and agents. End users and anonymous users
    must provide the parameter.

    #### Allowed for

    * End users

    For end-users, the response will only show a subscription created by the requesting end-user.

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload | For
    |---------------|---------------|----
    | users         | users         | all
    | articles      | articles      | article subscriptions
    | sections      | sections      | section subscriptions

    Args:
        locale (str):  Example: en-us.
        article_id (int):
        subscription_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubscriptionResponse
    """

    return sync_detailed(
        locale=locale,
        article_id=article_id,
        subscription_id=subscription_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    locale: str,
    article_id: int,
    subscription_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SubscriptionResponse]:
    """Show Article Subscription

     **Note**: `{/locale}` is an optional parameter for admins and agents. End users and anonymous users
    must provide the parameter.

    #### Allowed for

    * End users

    For end-users, the response will only show a subscription created by the requesting end-user.

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload | For
    |---------------|---------------|----
    | users         | users         | all
    | articles      | articles      | article subscriptions
    | sections      | sections      | section subscriptions

    Args:
        locale (str):  Example: en-us.
        article_id (int):
        subscription_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubscriptionResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        article_id=article_id,
        subscription_id=subscription_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: str,
    article_id: int,
    subscription_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[SubscriptionResponse]:
    """Show Article Subscription

     **Note**: `{/locale}` is an optional parameter for admins and agents. End users and anonymous users
    must provide the parameter.

    #### Allowed for

    * End users

    For end-users, the response will only show a subscription created by the requesting end-user.

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload | For
    |---------------|---------------|----
    | users         | users         | all
    | articles      | articles      | article subscriptions
    | sections      | sections      | section subscriptions

    Args:
        locale (str):  Example: en-us.
        article_id (int):
        subscription_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubscriptionResponse
    """

    return (
        await asyncio_detailed(
            locale=locale,
            article_id=article_id,
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed
