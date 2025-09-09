from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.help_center_locales_response import HelpCenterLocalesResponse
from ...types import Response


def _get_kwargs(
    article_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/help_center/articles/{article_id}/translations/missing",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[HelpCenterLocalesResponse]:
    if response.status_code == 200:
        response_200 = HelpCenterLocalesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[HelpCenterLocalesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[HelpCenterLocalesResponse]:
    """List Missing Translations

     Lists the locales that don't have a translation for a given [article](/api-
    reference/help_center/help-center-api/articles), [section](/api-reference/help_center/help-center-
    api/sections), or [category](/api-reference/help_center/help-center-api/categories).

    #### Allowed for

    * Agents

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HelpCenterLocalesResponse]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[HelpCenterLocalesResponse]:
    """List Missing Translations

     Lists the locales that don't have a translation for a given [article](/api-
    reference/help_center/help-center-api/articles), [section](/api-reference/help_center/help-center-
    api/sections), or [category](/api-reference/help_center/help-center-api/categories).

    #### Allowed for

    * Agents

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HelpCenterLocalesResponse
    """

    return sync_detailed(
        article_id=article_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[HelpCenterLocalesResponse]:
    """List Missing Translations

     Lists the locales that don't have a translation for a given [article](/api-
    reference/help_center/help-center-api/articles), [section](/api-reference/help_center/help-center-
    api/sections), or [category](/api-reference/help_center/help-center-api/categories).

    #### Allowed for

    * Agents

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HelpCenterLocalesResponse]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[HelpCenterLocalesResponse]:
    """List Missing Translations

     Lists the locales that don't have a translation for a given [article](/api-
    reference/help_center/help-center-api/articles), [section](/api-reference/help_center/help-center-
    api/sections), or [category](/api-reference/help_center/help-center-api/categories).

    #### Allowed for

    * Agents

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HelpCenterLocalesResponse
    """

    return (
        await asyncio_detailed(
            article_id=article_id,
            client=client,
        )
    ).parsed
