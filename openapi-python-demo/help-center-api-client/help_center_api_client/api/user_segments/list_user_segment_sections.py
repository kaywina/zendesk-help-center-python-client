from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sections_response import SectionsResponse
from ...types import Response


def _get_kwargs(
    user_segment_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/help_center/user_segments/{user_segment_id}/sections",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SectionsResponse]:
    if response.status_code == 200:
        response_200 = SectionsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SectionsResponse]:
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
) -> Response[SectionsResponse]:
    """List Sections with User Segment

     Lists the sections that use the specified user segment.

    This endpoint supports pagination as described in [Pagination](/api-reference/help_center/help-
    center-api/help-center-api/#pagination).

    #### Allowed for

    * Help Center managers

    Args:
        user_segment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SectionsResponse]
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
) -> Optional[SectionsResponse]:
    """List Sections with User Segment

     Lists the sections that use the specified user segment.

    This endpoint supports pagination as described in [Pagination](/api-reference/help_center/help-
    center-api/help-center-api/#pagination).

    #### Allowed for

    * Help Center managers

    Args:
        user_segment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SectionsResponse
    """

    return sync_detailed(
        user_segment_id=user_segment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_segment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SectionsResponse]:
    """List Sections with User Segment

     Lists the sections that use the specified user segment.

    This endpoint supports pagination as described in [Pagination](/api-reference/help_center/help-
    center-api/help-center-api/#pagination).

    #### Allowed for

    * Help Center managers

    Args:
        user_segment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SectionsResponse]
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
) -> Optional[SectionsResponse]:
    """List Sections with User Segment

     Lists the sections that use the specified user segment.

    This endpoint supports pagination as described in [Pagination](/api-reference/help_center/help-
    center-api/help-center-api/#pagination).

    #### Allowed for

    * Help Center managers

    Args:
        user_segment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SectionsResponse
    """

    return (
        await asyncio_detailed(
            user_segment_id=user_segment_id,
            client=client,
        )
    ).parsed
