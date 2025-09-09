from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.articles_response import ArticlesResponse
from ...models.list_articles_sort_by import ListArticlesSortBy
from ...models.list_articles_sort_order import ListArticlesSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    locale: str,
    *,
    sort_by: Union[Unset, ListArticlesSortBy] = UNSET,
    sort_order: Union[Unset, ListArticlesSortOrder] = UNSET,
    start_time: Union[Unset, int] = UNSET,
    label_names: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_sort_by: Union[Unset, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    json_sort_order: Union[Unset, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    params["start_time"] = start_time

    params["label_names"] = label_names

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/help_center/{locale}/articles",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ArticlesResponse]:
    if response.status_code == 200:
        response_200 = ArticlesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ArticlesResponse]:
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
    sort_by: Union[Unset, ListArticlesSortBy] = UNSET,
    sort_order: Union[Unset, ListArticlesSortOrder] = UNSET,
    start_time: Union[Unset, int] = UNSET,
    label_names: Union[Unset, str] = UNSET,
) -> Response[ArticlesResponse]:
    """List Articles

    Args:
        locale (str):  Example: en-us.
        sort_by (Union[Unset, ListArticlesSortBy]):
        sort_order (Union[Unset, ListArticlesSortOrder]):
        start_time (Union[Unset, int]):
        label_names (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArticlesResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        sort_by=sort_by,
        sort_order=sort_order,
        start_time=start_time,
        label_names=label_names,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sort_by: Union[Unset, ListArticlesSortBy] = UNSET,
    sort_order: Union[Unset, ListArticlesSortOrder] = UNSET,
    start_time: Union[Unset, int] = UNSET,
    label_names: Union[Unset, str] = UNSET,
) -> Optional[ArticlesResponse]:
    """List Articles

    Args:
        locale (str):  Example: en-us.
        sort_by (Union[Unset, ListArticlesSortBy]):
        sort_order (Union[Unset, ListArticlesSortOrder]):
        start_time (Union[Unset, int]):
        label_names (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArticlesResponse
    """

    return sync_detailed(
        locale=locale,
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        start_time=start_time,
        label_names=label_names,
    ).parsed


async def asyncio_detailed(
    locale: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sort_by: Union[Unset, ListArticlesSortBy] = UNSET,
    sort_order: Union[Unset, ListArticlesSortOrder] = UNSET,
    start_time: Union[Unset, int] = UNSET,
    label_names: Union[Unset, str] = UNSET,
) -> Response[ArticlesResponse]:
    """List Articles

    Args:
        locale (str):  Example: en-us.
        sort_by (Union[Unset, ListArticlesSortBy]):
        sort_order (Union[Unset, ListArticlesSortOrder]):
        start_time (Union[Unset, int]):
        label_names (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArticlesResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        sort_by=sort_by,
        sort_order=sort_order,
        start_time=start_time,
        label_names=label_names,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sort_by: Union[Unset, ListArticlesSortBy] = UNSET,
    sort_order: Union[Unset, ListArticlesSortOrder] = UNSET,
    start_time: Union[Unset, int] = UNSET,
    label_names: Union[Unset, str] = UNSET,
) -> Optional[ArticlesResponse]:
    """List Articles

    Args:
        locale (str):  Example: en-us.
        sort_by (Union[Unset, ListArticlesSortBy]):
        sort_order (Union[Unset, ListArticlesSortOrder]):
        start_time (Union[Unset, int]):
        label_names (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArticlesResponse
    """

    return (
        await asyncio_detailed(
            locale=locale,
            client=client,
            sort_by=sort_by,
            sort_order=sort_order,
            start_time=start_time,
            label_names=label_names,
        )
    ).parsed
