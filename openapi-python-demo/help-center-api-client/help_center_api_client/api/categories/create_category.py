from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.category_response import CategoryResponse
from ...types import Response


def _get_kwargs(
    locale: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v2/help_center/{locale}/categories",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CategoryResponse]:
    if response.status_code == 201:
        response_201 = CategoryResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CategoryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CategoryResponse]:
    """Create Category

     You must specify a category name and locale. The locale can be omitted if it's specified
    in the URL. Optionally, you can specify multiple [translations](/api-reference/help_center/help-
    center-api/translations) for
    the category. The specified locales must be enabled for the current Help Center.

    #### Allowed for

    * Help Center managers

    Args:
        locale (str):  Example: en-us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CategoryResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CategoryResponse]:
    """Create Category

     You must specify a category name and locale. The locale can be omitted if it's specified
    in the URL. Optionally, you can specify multiple [translations](/api-reference/help_center/help-
    center-api/translations) for
    the category. The specified locales must be enabled for the current Help Center.

    #### Allowed for

    * Help Center managers

    Args:
        locale (str):  Example: en-us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CategoryResponse
    """

    return sync_detailed(
        locale=locale,
        client=client,
    ).parsed


async def asyncio_detailed(
    locale: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CategoryResponse]:
    """Create Category

     You must specify a category name and locale. The locale can be omitted if it's specified
    in the URL. Optionally, you can specify multiple [translations](/api-reference/help_center/help-
    center-api/translations) for
    the category. The specified locales must be enabled for the current Help Center.

    #### Allowed for

    * Help Center managers

    Args:
        locale (str):  Example: en-us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CategoryResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CategoryResponse]:
    """Create Category

     You must specify a category name and locale. The locale can be omitted if it's specified
    in the URL. Optionally, you can specify multiple [translations](/api-reference/help_center/help-
    center-api/translations) for
    the category. The specified locales must be enabled for the current Help Center.

    #### Allowed for

    * Help Center managers

    Args:
        locale (str):  Example: en-us.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CategoryResponse
    """

    return (
        await asyncio_detailed(
            locale=locale,
            client=client,
        )
    ).parsed
