from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.translations_response import TranslationsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    article_id: int,
    *,
    locales: Union[Unset, str] = UNSET,
    outdated: Union[Unset, bool] = UNSET,
    draft: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["locales"] = locales

    params["outdated"] = outdated

    params["draft"] = draft

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/help_center/articles/{article_id}/translations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TranslationsResponse]:
    if response.status_code == 200:
        response_200 = TranslationsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TranslationsResponse]:
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
    locales: Union[Unset, str] = UNSET,
    outdated: Union[Unset, bool] = UNSET,
    draft: Union[Unset, bool] = UNSET,
) -> Response[TranslationsResponse]:
    """List Translations

     Lists all translations for a given [article](/api-reference/help_center/help-center-api/articles),
    [section](/api-reference/help_center/help-center-api/sections), or [category](/api-
    reference/help_center/help-center-api/categories).

    #### Allowed for

    * End users

    For end users, the response will list only the translations for articles, sections, or categories
    that they can view in Help Center.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        article_id (int):
        locales (Union[Unset, str]):
        outdated (Union[Unset, bool]):
        draft (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TranslationsResponse]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
        locales=locales,
        outdated=outdated,
        draft=draft,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    locales: Union[Unset, str] = UNSET,
    outdated: Union[Unset, bool] = UNSET,
    draft: Union[Unset, bool] = UNSET,
) -> Optional[TranslationsResponse]:
    """List Translations

     Lists all translations for a given [article](/api-reference/help_center/help-center-api/articles),
    [section](/api-reference/help_center/help-center-api/sections), or [category](/api-
    reference/help_center/help-center-api/categories).

    #### Allowed for

    * End users

    For end users, the response will list only the translations for articles, sections, or categories
    that they can view in Help Center.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        article_id (int):
        locales (Union[Unset, str]):
        outdated (Union[Unset, bool]):
        draft (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TranslationsResponse
    """

    return sync_detailed(
        article_id=article_id,
        client=client,
        locales=locales,
        outdated=outdated,
        draft=draft,
    ).parsed


async def asyncio_detailed(
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    locales: Union[Unset, str] = UNSET,
    outdated: Union[Unset, bool] = UNSET,
    draft: Union[Unset, bool] = UNSET,
) -> Response[TranslationsResponse]:
    """List Translations

     Lists all translations for a given [article](/api-reference/help_center/help-center-api/articles),
    [section](/api-reference/help_center/help-center-api/sections), or [category](/api-
    reference/help_center/help-center-api/categories).

    #### Allowed for

    * End users

    For end users, the response will list only the translations for articles, sections, or categories
    that they can view in Help Center.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        article_id (int):
        locales (Union[Unset, str]):
        outdated (Union[Unset, bool]):
        draft (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TranslationsResponse]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
        locales=locales,
        outdated=outdated,
        draft=draft,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    locales: Union[Unset, str] = UNSET,
    outdated: Union[Unset, bool] = UNSET,
    draft: Union[Unset, bool] = UNSET,
) -> Optional[TranslationsResponse]:
    """List Translations

     Lists all translations for a given [article](/api-reference/help_center/help-center-api/articles),
    [section](/api-reference/help_center/help-center-api/sections), or [category](/api-
    reference/help_center/help-center-api/categories).

    #### Allowed for

    * End users

    For end users, the response will list only the translations for articles, sections, or categories
    that they can view in Help Center.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        article_id (int):
        locales (Union[Unset, str]):
        outdated (Union[Unset, bool]):
        draft (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TranslationsResponse
    """

    return (
        await asyncio_detailed(
            article_id=article_id,
            client=client,
            locales=locales,
            outdated=outdated,
            draft=draft,
        )
    ).parsed
