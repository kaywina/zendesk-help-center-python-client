from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.translation_response import TranslationResponse
from ...types import Response


def _get_kwargs(
    article_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v2/help_center/articles/{article_id}/translations",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TranslationResponse]:
    if response.status_code == 201:
        response_201 = TranslationResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TranslationResponse]:
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
) -> Response[TranslationResponse]:
    """Create Translation

     Creates a translation for a given [article](/api-reference/help_center/help-center-api/articles),
    [section](/api-reference/help_center/help-center-api/sections), or [category](/api-
    reference/help_center/help-center-api/categories). Any locale
    that you specify must be enabled for the current Help Center. The locale must also be
    different from that of any existing translation associated with the source object.

    #### Allowed for

    * Help Center Managers
    * Agents (article translations only)

    The requesting agent can create an article translation only if they can edit the article in Help
    Center.

    Args:
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TranslationResponse]
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
) -> Optional[TranslationResponse]:
    """Create Translation

     Creates a translation for a given [article](/api-reference/help_center/help-center-api/articles),
    [section](/api-reference/help_center/help-center-api/sections), or [category](/api-
    reference/help_center/help-center-api/categories). Any locale
    that you specify must be enabled for the current Help Center. The locale must also be
    different from that of any existing translation associated with the source object.

    #### Allowed for

    * Help Center Managers
    * Agents (article translations only)

    The requesting agent can create an article translation only if they can edit the article in Help
    Center.

    Args:
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TranslationResponse
    """

    return sync_detailed(
        article_id=article_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[TranslationResponse]:
    """Create Translation

     Creates a translation for a given [article](/api-reference/help_center/help-center-api/articles),
    [section](/api-reference/help_center/help-center-api/sections), or [category](/api-
    reference/help_center/help-center-api/categories). Any locale
    that you specify must be enabled for the current Help Center. The locale must also be
    different from that of any existing translation associated with the source object.

    #### Allowed for

    * Help Center Managers
    * Agents (article translations only)

    The requesting agent can create an article translation only if they can edit the article in Help
    Center.

    Args:
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TranslationResponse]
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
) -> Optional[TranslationResponse]:
    """Create Translation

     Creates a translation for a given [article](/api-reference/help_center/help-center-api/articles),
    [section](/api-reference/help_center/help-center-api/sections), or [category](/api-
    reference/help_center/help-center-api/categories). Any locale
    that you specify must be enabled for the current Help Center. The locale must also be
    different from that of any existing translation associated with the source object.

    #### Allowed for

    * Help Center Managers
    * Agents (article translations only)

    The requesting agent can create an article translation only if they can edit the article in Help
    Center.

    Args:
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TranslationResponse
    """

    return (
        await asyncio_detailed(
            article_id=article_id,
            client=client,
        )
    ).parsed
