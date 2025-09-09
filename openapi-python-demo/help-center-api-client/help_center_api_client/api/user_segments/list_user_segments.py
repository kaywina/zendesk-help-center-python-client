from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_segments_response import UserSegmentsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    built_in: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["built_in"] = built_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/help_center/user_segments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UserSegmentsResponse]:
    if response.status_code == 200:
        response_200 = UserSegmentsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UserSegmentsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    built_in: Union[Unset, bool] = UNSET,
) -> Response[UserSegmentsResponse]:
    r"""List User Segments

     Some user segments can only be applied to sections and topics on certain Guide plans. For instance,
    user segments with a `user_type` of `\"staff\"` cannot be applied to sections and topics on accounts
    on the Guide Lite plan or the Suite Team plan. To request only user segments applicable on the
    account's current Suite plan, use the `/api/v2/help_center/user_segments/applicable.json` endpoint.

    The `/api/v2/help_center/users/{user_id}/user_segments.json` endpoint returns the list of user
    segments that a particular user belongs to. This is the only list endpoint that agents have access
    to. When an agent makes a request to this endpoint with another user's id, the response only
    includes user segments that the requesting agent also belongs to.

    These endpoints support pagination, as described in the [pagination documentation](/api-
    reference/introduction/pagination/).

    #### Allowed for

    * Help Center managers
    * Agents

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        built_in (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserSegmentsResponse]
    """

    kwargs = _get_kwargs(
        built_in=built_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    built_in: Union[Unset, bool] = UNSET,
) -> Optional[UserSegmentsResponse]:
    r"""List User Segments

     Some user segments can only be applied to sections and topics on certain Guide plans. For instance,
    user segments with a `user_type` of `\"staff\"` cannot be applied to sections and topics on accounts
    on the Guide Lite plan or the Suite Team plan. To request only user segments applicable on the
    account's current Suite plan, use the `/api/v2/help_center/user_segments/applicable.json` endpoint.

    The `/api/v2/help_center/users/{user_id}/user_segments.json` endpoint returns the list of user
    segments that a particular user belongs to. This is the only list endpoint that agents have access
    to. When an agent makes a request to this endpoint with another user's id, the response only
    includes user segments that the requesting agent also belongs to.

    These endpoints support pagination, as described in the [pagination documentation](/api-
    reference/introduction/pagination/).

    #### Allowed for

    * Help Center managers
    * Agents

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        built_in (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserSegmentsResponse
    """

    return sync_detailed(
        client=client,
        built_in=built_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    built_in: Union[Unset, bool] = UNSET,
) -> Response[UserSegmentsResponse]:
    r"""List User Segments

     Some user segments can only be applied to sections and topics on certain Guide plans. For instance,
    user segments with a `user_type` of `\"staff\"` cannot be applied to sections and topics on accounts
    on the Guide Lite plan or the Suite Team plan. To request only user segments applicable on the
    account's current Suite plan, use the `/api/v2/help_center/user_segments/applicable.json` endpoint.

    The `/api/v2/help_center/users/{user_id}/user_segments.json` endpoint returns the list of user
    segments that a particular user belongs to. This is the only list endpoint that agents have access
    to. When an agent makes a request to this endpoint with another user's id, the response only
    includes user segments that the requesting agent also belongs to.

    These endpoints support pagination, as described in the [pagination documentation](/api-
    reference/introduction/pagination/).

    #### Allowed for

    * Help Center managers
    * Agents

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        built_in (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserSegmentsResponse]
    """

    kwargs = _get_kwargs(
        built_in=built_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    built_in: Union[Unset, bool] = UNSET,
) -> Optional[UserSegmentsResponse]:
    r"""List User Segments

     Some user segments can only be applied to sections and topics on certain Guide plans. For instance,
    user segments with a `user_type` of `\"staff\"` cannot be applied to sections and topics on accounts
    on the Guide Lite plan or the Suite Team plan. To request only user segments applicable on the
    account's current Suite plan, use the `/api/v2/help_center/user_segments/applicable.json` endpoint.

    The `/api/v2/help_center/users/{user_id}/user_segments.json` endpoint returns the list of user
    segments that a particular user belongs to. This is the only list endpoint that agents have access
    to. When an agent makes a request to this endpoint with another user's id, the response only
    includes user segments that the requesting agent also belongs to.

    These endpoints support pagination, as described in the [pagination documentation](/api-
    reference/introduction/pagination/).

    #### Allowed for

    * Help Center managers
    * Agents

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        built_in (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserSegmentsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            built_in=built_in,
        )
    ).parsed
