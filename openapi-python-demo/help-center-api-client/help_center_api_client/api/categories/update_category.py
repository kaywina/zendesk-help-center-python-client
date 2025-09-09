from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.category_response import CategoryResponse
from ...types import Response


def _get_kwargs(
    locale: str,
    category_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v2/help_center/{locale}/categories/{category_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CategoryResponse]:
    if response.status_code == 200:
        response_200 = CategoryResponse.from_dict(response.json())

        return response_200

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
    category_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CategoryResponse]:
    """Update Category

     These endpoints only update category-level metadata such as the sorting position.
    They don't update category translations.

    #### Allowed for

    * Help Center managers

    Args:
        locale (str):  Example: en-us.
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CategoryResponse]
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
) -> Optional[CategoryResponse]:
    """Update Category

     These endpoints only update category-level metadata such as the sorting position.
    They don't update category translations.

    #### Allowed for

    * Help Center managers

    Args:
        locale (str):  Example: en-us.
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CategoryResponse
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
) -> Response[CategoryResponse]:
    """Update Category

     These endpoints only update category-level metadata such as the sorting position.
    They don't update category translations.

    #### Allowed for

    * Help Center managers

    Args:
        locale (str):  Example: en-us.
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CategoryResponse]
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
) -> Optional[CategoryResponse]:
    """Update Category

     These endpoints only update category-level metadata such as the sorting position.
    They don't update category translations.

    #### Allowed for

    * Help Center managers

    Args:
        locale (str):  Example: en-us.
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CategoryResponse
    """

    return (
        await asyncio_detailed(
            locale=locale,
            category_id=category_id,
            client=client,
        )
    ).parsed
