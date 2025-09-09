from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_user_subscriptions_by_user_id_type import ListUserSubscriptionsByUserIdType
from ...models.user_subscriptions_response import UserSubscriptionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    type_: Union[Unset, ListUserSubscriptionsByUserIdType] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/help_center/users/{user_id}/user_subscriptions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UserSubscriptionsResponse]:
    if response.status_code == 200:
        response_200 = UserSubscriptionsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UserSubscriptionsResponse]:
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
    type_: Union[Unset, ListUserSubscriptionsByUserIdType] = UNSET,
) -> Response[UserSubscriptionsResponse]:
    """List User Subscriptions By User

     Lists the user subscriptions of a given user. To list your own subscriptions,
    specify `me` as the user id.

    #### Allowed for

    * End users

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sideloads

    The following sideloads are supported:

    | Name          | Will sideload | For
    |---------------|---------------|----
    | users         | users         | all

    Args:
        user_id (int):
        type_ (Union[Unset, ListUserSubscriptionsByUserIdType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserSubscriptionsResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, ListUserSubscriptionsByUserIdType] = UNSET,
) -> Optional[UserSubscriptionsResponse]:
    """List User Subscriptions By User

     Lists the user subscriptions of a given user. To list your own subscriptions,
    specify `me` as the user id.

    #### Allowed for

    * End users

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sideloads

    The following sideloads are supported:

    | Name          | Will sideload | For
    |---------------|---------------|----
    | users         | users         | all

    Args:
        user_id (int):
        type_ (Union[Unset, ListUserSubscriptionsByUserIdType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserSubscriptionsResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, ListUserSubscriptionsByUserIdType] = UNSET,
) -> Response[UserSubscriptionsResponse]:
    """List User Subscriptions By User

     Lists the user subscriptions of a given user. To list your own subscriptions,
    specify `me` as the user id.

    #### Allowed for

    * End users

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sideloads

    The following sideloads are supported:

    | Name          | Will sideload | For
    |---------------|---------------|----
    | users         | users         | all

    Args:
        user_id (int):
        type_ (Union[Unset, ListUserSubscriptionsByUserIdType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserSubscriptionsResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, ListUserSubscriptionsByUserIdType] = UNSET,
) -> Optional[UserSubscriptionsResponse]:
    """List User Subscriptions By User

     Lists the user subscriptions of a given user. To list your own subscriptions,
    specify `me` as the user id.

    #### Allowed for

    * End users

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sideloads

    The following sideloads are supported:

    | Name          | Will sideload | For
    |---------------|---------------|----
    | users         | users         | all

    Args:
        user_id (int):
        type_ (Union[Unset, ListUserSubscriptionsByUserIdType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserSubscriptionsResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            type_=type_,
        )
    ).parsed
