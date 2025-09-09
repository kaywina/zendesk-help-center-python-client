import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.article_search_response import ArticleSearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: Union[Unset, str] = UNSET,
    category: Union[Unset, int] = UNSET,
    section: Union[Unset, int] = UNSET,
    label_names: Union[Unset, str] = UNSET,
    locale: Union[Unset, str] = UNSET,
    multibrand: Union[Unset, bool] = UNSET,
    brand_id: Union[Unset, int] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_at: Union[Unset, datetime.datetime] = UNSET,
    updated_before: Union[Unset, datetime.datetime] = UNSET,
    updated_after: Union[Unset, datetime.datetime] = UNSET,
    updated_at: Union[Unset, datetime.datetime] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    params["category"] = category

    params["section"] = section

    params["label_names"] = label_names

    params["locale"] = locale

    params["multibrand"] = multibrand

    params["brand_id"] = brand_id

    json_created_before: Union[Unset, str] = UNSET
    if not isinstance(created_before, Unset):
        json_created_before = created_before.isoformat()
    params["created_before"] = json_created_before

    json_created_after: Union[Unset, str] = UNSET
    if not isinstance(created_after, Unset):
        json_created_after = created_after.isoformat()
    params["created_after"] = json_created_after

    json_created_at: Union[Unset, str] = UNSET
    if not isinstance(created_at, Unset):
        json_created_at = created_at.isoformat()
    params["created_at"] = json_created_at

    json_updated_before: Union[Unset, str] = UNSET
    if not isinstance(updated_before, Unset):
        json_updated_before = updated_before.isoformat()
    params["updated_before"] = json_updated_before

    json_updated_after: Union[Unset, str] = UNSET
    if not isinstance(updated_after, Unset):
        json_updated_after = updated_after.isoformat()
    params["updated_after"] = json_updated_after

    json_updated_at: Union[Unset, str] = UNSET
    if not isinstance(updated_at, Unset):
        json_updated_at = updated_at.isoformat()
    params["updated_at"] = json_updated_at

    params["sort_by"] = sort_by

    params["sort_order"] = sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/help_center/articles/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ArticleSearchResponse]:
    if response.status_code == 200:
        response_200 = ArticleSearchResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ArticleSearchResponse]:
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
    category: Union[Unset, int] = UNSET,
    section: Union[Unset, int] = UNSET,
    label_names: Union[Unset, str] = UNSET,
    locale: Union[Unset, str] = UNSET,
    multibrand: Union[Unset, bool] = UNSET,
    brand_id: Union[Unset, int] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_at: Union[Unset, datetime.datetime] = UNSET,
    updated_before: Union[Unset, datetime.datetime] = UNSET,
    updated_after: Union[Unset, datetime.datetime] = UNSET,
    updated_at: Union[Unset, datetime.datetime] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
) -> Response[ArticleSearchResponse]:
    r"""Search Articles

     Returns a default number of 25 articles per page, up to a maximum of 1000 results. See
    [Pagination](/api-reference/introduction/pagination/). The `per_page` parameter, if provided, must
    be an integer between 1 and 100.

    The `page` parameter, if provided, must be an integer greater than 0.

    The results are sorted by relevance by default. You can also sort the results by `created_at` or
    `updated_at`.

    The [article objects](/api-reference/help_center/help-center-api/articles) returned by the search
    endpoint contain two additional properties:

    | Name        | Type   | Read-only | Mandatory | Comment
    |-------------|--------|-----------|-----------|-------
    | result_type | string | yes       | no        | For articles, always the string \"article\"
    | snippet     | string | yes       | no        | The portion of an article that is relevant to the
    search query, with matching words or phrases delimited by `<em></em>` tags. Example: a query for
    \"carrot potato\" might return the snippet \"...don't confuse `<em>`carrots`</em>` with
    `<em>`potatoes`</em>`...\"

    You must specify at least one of the following parameters in your request:

    - query
    - category
    - section
    - label_names

    #### Pagination

    - Offset pagination only

    See [Pagination](/api-reference/introduction/pagination/).

    Returns a maximum of 100 articles per page.

    #### Allowed for

    * Anonymous users

    Args:
        query (Union[Unset, str]):
        category (Union[Unset, int]):
        section (Union[Unset, int]):
        label_names (Union[Unset, str]):
        locale (Union[Unset, str]):
        multibrand (Union[Unset, bool]):
        brand_id (Union[Unset, int]):
        created_before (Union[Unset, datetime.datetime]):
        created_after (Union[Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        updated_before (Union[Unset, datetime.datetime]):
        updated_after (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        sort_by (Union[Unset, str]):
        sort_order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArticleSearchResponse]
    """

    kwargs = _get_kwargs(
        query=query,
        category=category,
        section=section,
        label_names=label_names,
        locale=locale,
        multibrand=multibrand,
        brand_id=brand_id,
        created_before=created_before,
        created_after=created_after,
        created_at=created_at,
        updated_before=updated_before,
        updated_after=updated_after,
        updated_at=updated_at,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    category: Union[Unset, int] = UNSET,
    section: Union[Unset, int] = UNSET,
    label_names: Union[Unset, str] = UNSET,
    locale: Union[Unset, str] = UNSET,
    multibrand: Union[Unset, bool] = UNSET,
    brand_id: Union[Unset, int] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_at: Union[Unset, datetime.datetime] = UNSET,
    updated_before: Union[Unset, datetime.datetime] = UNSET,
    updated_after: Union[Unset, datetime.datetime] = UNSET,
    updated_at: Union[Unset, datetime.datetime] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
) -> Optional[ArticleSearchResponse]:
    r"""Search Articles

     Returns a default number of 25 articles per page, up to a maximum of 1000 results. See
    [Pagination](/api-reference/introduction/pagination/). The `per_page` parameter, if provided, must
    be an integer between 1 and 100.

    The `page` parameter, if provided, must be an integer greater than 0.

    The results are sorted by relevance by default. You can also sort the results by `created_at` or
    `updated_at`.

    The [article objects](/api-reference/help_center/help-center-api/articles) returned by the search
    endpoint contain two additional properties:

    | Name        | Type   | Read-only | Mandatory | Comment
    |-------------|--------|-----------|-----------|-------
    | result_type | string | yes       | no        | For articles, always the string \"article\"
    | snippet     | string | yes       | no        | The portion of an article that is relevant to the
    search query, with matching words or phrases delimited by `<em></em>` tags. Example: a query for
    \"carrot potato\" might return the snippet \"...don't confuse `<em>`carrots`</em>` with
    `<em>`potatoes`</em>`...\"

    You must specify at least one of the following parameters in your request:

    - query
    - category
    - section
    - label_names

    #### Pagination

    - Offset pagination only

    See [Pagination](/api-reference/introduction/pagination/).

    Returns a maximum of 100 articles per page.

    #### Allowed for

    * Anonymous users

    Args:
        query (Union[Unset, str]):
        category (Union[Unset, int]):
        section (Union[Unset, int]):
        label_names (Union[Unset, str]):
        locale (Union[Unset, str]):
        multibrand (Union[Unset, bool]):
        brand_id (Union[Unset, int]):
        created_before (Union[Unset, datetime.datetime]):
        created_after (Union[Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        updated_before (Union[Unset, datetime.datetime]):
        updated_after (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        sort_by (Union[Unset, str]):
        sort_order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArticleSearchResponse
    """

    return sync_detailed(
        client=client,
        query=query,
        category=category,
        section=section,
        label_names=label_names,
        locale=locale,
        multibrand=multibrand,
        brand_id=brand_id,
        created_before=created_before,
        created_after=created_after,
        created_at=created_at,
        updated_before=updated_before,
        updated_after=updated_after,
        updated_at=updated_at,
        sort_by=sort_by,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    category: Union[Unset, int] = UNSET,
    section: Union[Unset, int] = UNSET,
    label_names: Union[Unset, str] = UNSET,
    locale: Union[Unset, str] = UNSET,
    multibrand: Union[Unset, bool] = UNSET,
    brand_id: Union[Unset, int] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_at: Union[Unset, datetime.datetime] = UNSET,
    updated_before: Union[Unset, datetime.datetime] = UNSET,
    updated_after: Union[Unset, datetime.datetime] = UNSET,
    updated_at: Union[Unset, datetime.datetime] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
) -> Response[ArticleSearchResponse]:
    r"""Search Articles

     Returns a default number of 25 articles per page, up to a maximum of 1000 results. See
    [Pagination](/api-reference/introduction/pagination/). The `per_page` parameter, if provided, must
    be an integer between 1 and 100.

    The `page` parameter, if provided, must be an integer greater than 0.

    The results are sorted by relevance by default. You can also sort the results by `created_at` or
    `updated_at`.

    The [article objects](/api-reference/help_center/help-center-api/articles) returned by the search
    endpoint contain two additional properties:

    | Name        | Type   | Read-only | Mandatory | Comment
    |-------------|--------|-----------|-----------|-------
    | result_type | string | yes       | no        | For articles, always the string \"article\"
    | snippet     | string | yes       | no        | The portion of an article that is relevant to the
    search query, with matching words or phrases delimited by `<em></em>` tags. Example: a query for
    \"carrot potato\" might return the snippet \"...don't confuse `<em>`carrots`</em>` with
    `<em>`potatoes`</em>`...\"

    You must specify at least one of the following parameters in your request:

    - query
    - category
    - section
    - label_names

    #### Pagination

    - Offset pagination only

    See [Pagination](/api-reference/introduction/pagination/).

    Returns a maximum of 100 articles per page.

    #### Allowed for

    * Anonymous users

    Args:
        query (Union[Unset, str]):
        category (Union[Unset, int]):
        section (Union[Unset, int]):
        label_names (Union[Unset, str]):
        locale (Union[Unset, str]):
        multibrand (Union[Unset, bool]):
        brand_id (Union[Unset, int]):
        created_before (Union[Unset, datetime.datetime]):
        created_after (Union[Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        updated_before (Union[Unset, datetime.datetime]):
        updated_after (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        sort_by (Union[Unset, str]):
        sort_order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArticleSearchResponse]
    """

    kwargs = _get_kwargs(
        query=query,
        category=category,
        section=section,
        label_names=label_names,
        locale=locale,
        multibrand=multibrand,
        brand_id=brand_id,
        created_before=created_before,
        created_after=created_after,
        created_at=created_at,
        updated_before=updated_before,
        updated_after=updated_after,
        updated_at=updated_at,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    category: Union[Unset, int] = UNSET,
    section: Union[Unset, int] = UNSET,
    label_names: Union[Unset, str] = UNSET,
    locale: Union[Unset, str] = UNSET,
    multibrand: Union[Unset, bool] = UNSET,
    brand_id: Union[Unset, int] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_at: Union[Unset, datetime.datetime] = UNSET,
    updated_before: Union[Unset, datetime.datetime] = UNSET,
    updated_after: Union[Unset, datetime.datetime] = UNSET,
    updated_at: Union[Unset, datetime.datetime] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    sort_order: Union[Unset, str] = UNSET,
) -> Optional[ArticleSearchResponse]:
    r"""Search Articles

     Returns a default number of 25 articles per page, up to a maximum of 1000 results. See
    [Pagination](/api-reference/introduction/pagination/). The `per_page` parameter, if provided, must
    be an integer between 1 and 100.

    The `page` parameter, if provided, must be an integer greater than 0.

    The results are sorted by relevance by default. You can also sort the results by `created_at` or
    `updated_at`.

    The [article objects](/api-reference/help_center/help-center-api/articles) returned by the search
    endpoint contain two additional properties:

    | Name        | Type   | Read-only | Mandatory | Comment
    |-------------|--------|-----------|-----------|-------
    | result_type | string | yes       | no        | For articles, always the string \"article\"
    | snippet     | string | yes       | no        | The portion of an article that is relevant to the
    search query, with matching words or phrases delimited by `<em></em>` tags. Example: a query for
    \"carrot potato\" might return the snippet \"...don't confuse `<em>`carrots`</em>` with
    `<em>`potatoes`</em>`...\"

    You must specify at least one of the following parameters in your request:

    - query
    - category
    - section
    - label_names

    #### Pagination

    - Offset pagination only

    See [Pagination](/api-reference/introduction/pagination/).

    Returns a maximum of 100 articles per page.

    #### Allowed for

    * Anonymous users

    Args:
        query (Union[Unset, str]):
        category (Union[Unset, int]):
        section (Union[Unset, int]):
        label_names (Union[Unset, str]):
        locale (Union[Unset, str]):
        multibrand (Union[Unset, bool]):
        brand_id (Union[Unset, int]):
        created_before (Union[Unset, datetime.datetime]):
        created_after (Union[Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        updated_before (Union[Unset, datetime.datetime]):
        updated_after (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        sort_by (Union[Unset, str]):
        sort_order (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArticleSearchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            category=category,
            section=section,
            label_names=label_names,
            locale=locale,
            multibrand=multibrand,
            brand_id=brand_id,
            created_before=created_before,
            created_after=created_after,
            created_at=created_at,
            updated_before=updated_before,
            updated_after=updated_after,
            updated_at=updated_at,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    ).parsed
