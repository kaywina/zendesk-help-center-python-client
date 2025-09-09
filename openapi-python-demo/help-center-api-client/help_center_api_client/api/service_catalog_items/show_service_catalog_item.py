from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_catalog_item_response import ServiceCatalogItemResponse
from ...types import Response


def _get_kwargs(
    item_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/help_center/service_catalog/items/{item_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ServiceCatalogItemResponse]:
    if response.status_code == 200:
        response_200 = ServiceCatalogItemResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ServiceCatalogItemResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ServiceCatalogItemResponse]:
    """Show Service Catalog Item

     Returns a service catalog item by its id.

    #### Allowed for

    * End users

    Args:
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceCatalogItemResponse]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ServiceCatalogItemResponse]:
    """Show Service Catalog Item

     Returns a service catalog item by its id.

    #### Allowed for

    * End users

    Args:
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceCatalogItemResponse
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ServiceCatalogItemResponse]:
    """Show Service Catalog Item

     Returns a service catalog item by its id.

    #### Allowed for

    * End users

    Args:
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceCatalogItemResponse]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ServiceCatalogItemResponse]:
    """Show Service Catalog Item

     Returns a service catalog item by its id.

    #### Allowed for

    * End users

    Args:
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceCatalogItemResponse
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
        )
    ).parsed
