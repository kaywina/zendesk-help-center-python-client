from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request_error_response import BadRequestErrorResponse
from ...models.user_segment_response import UserSegmentResponse
from ...types import Response


def _get_kwargs(
    user_segment_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v2/help_center/user_segments/{user_segment_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequestErrorResponse, UserSegmentResponse]]:
    if response.status_code == 200:
        response_200 = UserSegmentResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BadRequestErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BadRequestErrorResponse, UserSegmentResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_segment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[BadRequestErrorResponse, UserSegmentResponse]]:
    """Update User Segment

     #### Allowed for

    * Help Center managers

    Args:
        user_segment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestErrorResponse, UserSegmentResponse]]
    """

    kwargs = _get_kwargs(
        user_segment_id=user_segment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_segment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[BadRequestErrorResponse, UserSegmentResponse]]:
    """Update User Segment

     #### Allowed for

    * Help Center managers

    Args:
        user_segment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestErrorResponse, UserSegmentResponse]
    """

    return sync_detailed(
        user_segment_id=user_segment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_segment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[BadRequestErrorResponse, UserSegmentResponse]]:
    """Update User Segment

     #### Allowed for

    * Help Center managers

    Args:
        user_segment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestErrorResponse, UserSegmentResponse]]
    """

    kwargs = _get_kwargs(
        user_segment_id=user_segment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_segment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[BadRequestErrorResponse, UserSegmentResponse]]:
    """Update User Segment

     #### Allowed for

    * Help Center managers

    Args:
        user_segment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestErrorResponse, UserSegmentResponse]
    """

    return (
        await asyncio_detailed(
            user_segment_id=user_segment_id,
            client=client,
        )
    ).parsed
