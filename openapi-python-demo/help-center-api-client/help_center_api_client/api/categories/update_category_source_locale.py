from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    locale: str,
    category_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v2/help_center/{locale}/categories/{category_id}/source_locale",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[str]:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: str,
    category_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[str]:
    """Update Category Source Locale

     The endpoint updates the category `source_locale` property

    #### Allowed for

    * Agents

    Args:
        locale (str):  Example: en-us.
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        locale=locale,
        category_id=category_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: str,
    category_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[str]:
    """Update Category Source Locale

     The endpoint updates the category `source_locale` property

    #### Allowed for

    * Agents

    Args:
        locale (str):  Example: en-us.
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        locale=locale,
        category_id=category_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    locale: str,
    category_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[str]:
    """Update Category Source Locale

     The endpoint updates the category `source_locale` property

    #### Allowed for

    * Agents

    Args:
        locale (str):  Example: en-us.
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        locale=locale,
        category_id=category_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: str,
    category_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[str]:
    """Update Category Source Locale

     The endpoint updates the category `source_locale` property

    #### Allowed for

    * Agents

    Args:
        locale (str):  Example: en-us.
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            locale=locale,
            category_id=category_id,
            client=client,
        )
    ).parsed
