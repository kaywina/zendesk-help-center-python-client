from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    locale: str,
    article_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v2/help_center/{locale}/articles/{article_id}/source_locale",
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
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[str]:
    """Update Article Source Locale

     Updates the article's `source_locale` property. The source locale is the main language of the
    article. When you delete the article in the source locale, you delete all the article's
    translations.

    The endpoint sets one of the article's translation as the source locale of the article. The article
    in the previous source locale becomes a translation, which you can delete separately.

    The new source locale must be enabled in Guide. See [Enabling languages for your help
    center](https://support.zendesk.com/hc/en-us/articles/224857687#topic_ys2_kxh_tz). You can use the
    [List all enabled locales and default locale](/api-reference/help_center/help-center-
    api/translations/#list-enabled-locales-and-default-locale) endpoint to check for the enabled
    locales.

    #### Allowed for

    * Agents

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        locale=locale,
        article_id=article_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: str,
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[str]:
    """Update Article Source Locale

     Updates the article's `source_locale` property. The source locale is the main language of the
    article. When you delete the article in the source locale, you delete all the article's
    translations.

    The endpoint sets one of the article's translation as the source locale of the article. The article
    in the previous source locale becomes a translation, which you can delete separately.

    The new source locale must be enabled in Guide. See [Enabling languages for your help
    center](https://support.zendesk.com/hc/en-us/articles/224857687#topic_ys2_kxh_tz). You can use the
    [List all enabled locales and default locale](/api-reference/help_center/help-center-
    api/translations/#list-enabled-locales-and-default-locale) endpoint to check for the enabled
    locales.

    #### Allowed for

    * Agents

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        locale=locale,
        article_id=article_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    locale: str,
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[str]:
    """Update Article Source Locale

     Updates the article's `source_locale` property. The source locale is the main language of the
    article. When you delete the article in the source locale, you delete all the article's
    translations.

    The endpoint sets one of the article's translation as the source locale of the article. The article
    in the previous source locale becomes a translation, which you can delete separately.

    The new source locale must be enabled in Guide. See [Enabling languages for your help
    center](https://support.zendesk.com/hc/en-us/articles/224857687#topic_ys2_kxh_tz). You can use the
    [List all enabled locales and default locale](/api-reference/help_center/help-center-
    api/translations/#list-enabled-locales-and-default-locale) endpoint to check for the enabled
    locales.

    #### Allowed for

    * Agents

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        locale=locale,
        article_id=article_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: str,
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[str]:
    """Update Article Source Locale

     Updates the article's `source_locale` property. The source locale is the main language of the
    article. When you delete the article in the source locale, you delete all the article's
    translations.

    The endpoint sets one of the article's translation as the source locale of the article. The article
    in the previous source locale becomes a translation, which you can delete separately.

    The new source locale must be enabled in Guide. See [Enabling languages for your help
    center](https://support.zendesk.com/hc/en-us/articles/224857687#topic_ys2_kxh_tz). You can use the
    [List all enabled locales and default locale](/api-reference/help_center/help-center-
    api/translations/#list-enabled-locales-and-default-locale) endpoint to check for the enabled
    locales.

    #### Allowed for

    * Agents

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            locale=locale,
            article_id=article_id,
            client=client,
        )
    ).parsed
