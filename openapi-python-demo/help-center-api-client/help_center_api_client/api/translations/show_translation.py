from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.translation_response import TranslationResponse
from ...types import Response


def _get_kwargs(
    article_id: int,
    locale: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/help_center/articles/{article_id}/translations/{locale}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TranslationResponse]:
    if response.status_code == 200:
        response_200 = TranslationResponse.from_dict(response.json())

        return response_200

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
    locale: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[TranslationResponse]:
    """Show Translation

     #### Allowed for

    * End users

    Args:
        article_id (int):
        locale (str):  Example: en-us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TranslationResponse]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    article_id: int,
    locale: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[TranslationResponse]:
    """Show Translation

     #### Allowed for

    * End users

    Args:
        article_id (int):
        locale (str):  Example: en-us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TranslationResponse
    """

    return sync_detailed(
        article_id=article_id,
        locale=locale,
        client=client,
    ).parsed


async def asyncio_detailed(
    article_id: int,
    locale: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[TranslationResponse]:
    """Show Translation

     #### Allowed for

    * End users

    Args:
        article_id (int):
        locale (str):  Example: en-us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TranslationResponse]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    article_id: int,
    locale: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[TranslationResponse]:
    """Show Translation

     #### Allowed for

    * End users

    Args:
        article_id (int):
        locale (str):  Example: en-us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TranslationResponse
    """

    return (
        await asyncio_detailed(
            article_id=article_id,
            locale=locale,
            client=client,
        )
    ).parsed
