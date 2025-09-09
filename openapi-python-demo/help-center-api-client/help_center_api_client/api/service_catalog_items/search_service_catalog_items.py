from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_catalog_items_response import ServiceCatalogItemsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: Union[Unset, str] = UNSET,
    pageafter: Union[Unset, str] = UNSET,
    pagebefore: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    params["page[after]"] = pageafter

    params["page[before]"] = pagebefore

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/help_center/service_catalog/items/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ServiceCatalogItemsResponse]:
    if response.status_code == 200:
        response_200 = ServiceCatalogItemsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ServiceCatalogItemsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    pageafter: Union[Unset, str] = UNSET,
    pagebefore: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Response[ServiceCatalogItemsResponse]:
    """Search Service Catalog Items

     Returns an array of service catalog item object records that meet the search criteria. Returns the
    records sorted by relevancy with page limits

    #### Allowed for

    * End users

    #### Pagination

    * Cursor pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        query (Union[Unset, str]):
        pageafter (Union[Unset, str]):
        pagebefore (Union[Unset, str]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceCatalogItemsResponse]
    """

    kwargs = _get_kwargs(
        query=query,
        pageafter=pageafter,
        pagebefore=pagebefore,
        pagesize=pagesize,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    pageafter: Union[Unset, str] = UNSET,
    pagebefore: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[ServiceCatalogItemsResponse]:
    """Search Service Catalog Items

     Returns an array of service catalog item object records that meet the search criteria. Returns the
    records sorted by relevancy with page limits

    #### Allowed for

    * End users

    #### Pagination

    * Cursor pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        query (Union[Unset, str]):
        pageafter (Union[Unset, str]):
        pagebefore (Union[Unset, str]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceCatalogItemsResponse
    """

    return sync_detailed(
        client=client,
        query=query,
        pageafter=pageafter,
        pagebefore=pagebefore,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    pageafter: Union[Unset, str] = UNSET,
    pagebefore: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Response[ServiceCatalogItemsResponse]:
    """Search Service Catalog Items

     Returns an array of service catalog item object records that meet the search criteria. Returns the
    records sorted by relevancy with page limits

    #### Allowed for

    * End users

    #### Pagination

    * Cursor pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        query (Union[Unset, str]):
        pageafter (Union[Unset, str]):
        pagebefore (Union[Unset, str]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceCatalogItemsResponse]
    """

    kwargs = _get_kwargs(
        query=query,
        pageafter=pageafter,
        pagebefore=pagebefore,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    pageafter: Union[Unset, str] = UNSET,
    pagebefore: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[ServiceCatalogItemsResponse]:
    """Search Service Catalog Items

     Returns an array of service catalog item object records that meet the search criteria. Returns the
    records sorted by relevancy with page limits

    #### Allowed for

    * End users

    #### Pagination

    * Cursor pagination

    See [Pagination](/api-reference/introduction/pagination/).

    Args:
        query (Union[Unset, str]):
        pageafter (Union[Unset, str]):
        pagebefore (Union[Unset, str]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceCatalogItemsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            pageafter=pageafter,
            pagebefore=pagebefore,
            pagesize=pagesize,
        )
    ).parsed
