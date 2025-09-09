from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.unified_search_result_set import UnifiedSearchResultSet
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: Union[Unset, str] = UNSET,
    filterlocales: str,
    filtercategory_ids: Union[Unset, str] = UNSET,
    filtersection_ids: Union[Unset, str] = UNSET,
    filtertopic_ids: Union[Unset, str] = UNSET,
    filterexternal_source_ids: Union[Unset, str] = UNSET,
    filterbrand_ids: Union[Unset, str] = UNSET,
    filtercontent_types: Union[Unset, str] = UNSET,
    pageafter: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    params["filter[locales]"] = filterlocales

    params["filter[category_ids]"] = filtercategory_ids

    params["filter[section_ids]"] = filtersection_ids

    params["filter[topic_ids]"] = filtertopic_ids

    params["filter[external_source_ids]"] = filterexternal_source_ids

    params["filter[brand_ids]"] = filterbrand_ids

    params["filter[content_types]"] = filtercontent_types

    params["page[after]"] = pageafter

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/guide/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UnifiedSearchResultSet]:
    if response.status_code == 200:
        response_200 = UnifiedSearchResultSet.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UnifiedSearchResultSet]:
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
    filterlocales: str,
    filtercategory_ids: Union[Unset, str] = UNSET,
    filtersection_ids: Union[Unset, str] = UNSET,
    filtertopic_ids: Union[Unset, str] = UNSET,
    filterexternal_source_ids: Union[Unset, str] = UNSET,
    filterbrand_ids: Union[Unset, str] = UNSET,
    filtercontent_types: Union[Unset, str] = UNSET,
    pageafter: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Response[UnifiedSearchResultSet]:
    """Unified Search

    Args:
        query (Union[Unset, str]):
        filterlocales (str):
        filtercategory_ids (Union[Unset, str]):
        filtersection_ids (Union[Unset, str]):
        filtertopic_ids (Union[Unset, str]):
        filterexternal_source_ids (Union[Unset, str]):
        filterbrand_ids (Union[Unset, str]):
        filtercontent_types (Union[Unset, str]):
        pageafter (Union[Unset, str]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnifiedSearchResultSet]
    """

    kwargs = _get_kwargs(
        query=query,
        filterlocales=filterlocales,
        filtercategory_ids=filtercategory_ids,
        filtersection_ids=filtersection_ids,
        filtertopic_ids=filtertopic_ids,
        filterexternal_source_ids=filterexternal_source_ids,
        filterbrand_ids=filterbrand_ids,
        filtercontent_types=filtercontent_types,
        pageafter=pageafter,
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
    filterlocales: str,
    filtercategory_ids: Union[Unset, str] = UNSET,
    filtersection_ids: Union[Unset, str] = UNSET,
    filtertopic_ids: Union[Unset, str] = UNSET,
    filterexternal_source_ids: Union[Unset, str] = UNSET,
    filterbrand_ids: Union[Unset, str] = UNSET,
    filtercontent_types: Union[Unset, str] = UNSET,
    pageafter: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[UnifiedSearchResultSet]:
    """Unified Search

    Args:
        query (Union[Unset, str]):
        filterlocales (str):
        filtercategory_ids (Union[Unset, str]):
        filtersection_ids (Union[Unset, str]):
        filtertopic_ids (Union[Unset, str]):
        filterexternal_source_ids (Union[Unset, str]):
        filterbrand_ids (Union[Unset, str]):
        filtercontent_types (Union[Unset, str]):
        pageafter (Union[Unset, str]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnifiedSearchResultSet
    """

    return sync_detailed(
        client=client,
        query=query,
        filterlocales=filterlocales,
        filtercategory_ids=filtercategory_ids,
        filtersection_ids=filtersection_ids,
        filtertopic_ids=filtertopic_ids,
        filterexternal_source_ids=filterexternal_source_ids,
        filterbrand_ids=filterbrand_ids,
        filtercontent_types=filtercontent_types,
        pageafter=pageafter,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    filterlocales: str,
    filtercategory_ids: Union[Unset, str] = UNSET,
    filtersection_ids: Union[Unset, str] = UNSET,
    filtertopic_ids: Union[Unset, str] = UNSET,
    filterexternal_source_ids: Union[Unset, str] = UNSET,
    filterbrand_ids: Union[Unset, str] = UNSET,
    filtercontent_types: Union[Unset, str] = UNSET,
    pageafter: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Response[UnifiedSearchResultSet]:
    """Unified Search

    Args:
        query (Union[Unset, str]):
        filterlocales (str):
        filtercategory_ids (Union[Unset, str]):
        filtersection_ids (Union[Unset, str]):
        filtertopic_ids (Union[Unset, str]):
        filterexternal_source_ids (Union[Unset, str]):
        filterbrand_ids (Union[Unset, str]):
        filtercontent_types (Union[Unset, str]):
        pageafter (Union[Unset, str]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnifiedSearchResultSet]
    """

    kwargs = _get_kwargs(
        query=query,
        filterlocales=filterlocales,
        filtercategory_ids=filtercategory_ids,
        filtersection_ids=filtersection_ids,
        filtertopic_ids=filtertopic_ids,
        filterexternal_source_ids=filterexternal_source_ids,
        filterbrand_ids=filterbrand_ids,
        filtercontent_types=filtercontent_types,
        pageafter=pageafter,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    filterlocales: str,
    filtercategory_ids: Union[Unset, str] = UNSET,
    filtersection_ids: Union[Unset, str] = UNSET,
    filtertopic_ids: Union[Unset, str] = UNSET,
    filterexternal_source_ids: Union[Unset, str] = UNSET,
    filterbrand_ids: Union[Unset, str] = UNSET,
    filtercontent_types: Union[Unset, str] = UNSET,
    pageafter: Union[Unset, str] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[UnifiedSearchResultSet]:
    """Unified Search

    Args:
        query (Union[Unset, str]):
        filterlocales (str):
        filtercategory_ids (Union[Unset, str]):
        filtersection_ids (Union[Unset, str]):
        filtertopic_ids (Union[Unset, str]):
        filterexternal_source_ids (Union[Unset, str]):
        filterbrand_ids (Union[Unset, str]):
        filtercontent_types (Union[Unset, str]):
        pageafter (Union[Unset, str]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnifiedSearchResultSet
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            filterlocales=filterlocales,
            filtercategory_ids=filtercategory_ids,
            filtersection_ids=filtersection_ids,
            filtertopic_ids=filtertopic_ids,
            filterexternal_source_ids=filterexternal_source_ids,
            filterbrand_ids=filterbrand_ids,
            filtercontent_types=filtercontent_types,
            pageafter=pageafter,
            pagesize=pagesize,
        )
    ).parsed
