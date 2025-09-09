from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_sections_sort_by import ListSectionsSortBy
from ...models.list_sections_sort_order import ListSectionsSortOrder
from ...models.sections_response import SectionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    locale: str,
    *,
    sort_by: Union[Unset, ListSectionsSortBy] = UNSET,
    sort_order: Union[Unset, ListSectionsSortOrder] = UNSET,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/help_center/{locale}/sections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SectionsResponse]:
    if response.status_code == 200:
        response_200 = SectionsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SectionsResponse]:
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
    sort_by: Union[Unset, ListSectionsSortBy] = UNSET,
    sort_order: Union[Unset, ListSectionsSortOrder] = UNSET,
) -> Response[SectionsResponse]:
    """List Sections

     Lists all the sections in Help Center or in a specific [category](/api-reference/help_center/help-
    center-api/categories).

    The `{locale}` is required only for end users and anomynous users. Admins and agents can omit it.

    #### Allowed for

    * Anonymous users

    The response will list only the sections that the requesting agent,
    end user, or anonymous user can view in the help center.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sorting

    You can sort the results with the `sort_by` and `sort_order` query string parameters.

    ```
    GET /api/v2/help_center/en-us/sections.json?sort_by=updated_at&sort_order=asc
    ```

    The `sort_by` parameter can have one of the following values:

    | value         | description
    | ------------- | -----------
    | `position`    | order set manually using the Arrange Content page. Default order
    | `created_at`  | order by creation time
    | `updated_at`  | order by update time

    The `sort_order` parameter can have one of the following values:

    | value   | description
    | ------- | -----------
    | `asc`   | ascending order
    | `desc`  | descending order

    #### Sideloads

    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | categories    | the category
    | translations  | the section and category translations, if any

    Unlike other sideloads, translations are embedded within the section because they're
    not shared between resources.
    Category translations are only sideloaded if categories are.

    Args:
        locale (str):  Example: en-us.
        sort_by (Union[Unset, ListSectionsSortBy]):
        sort_order (Union[Unset, ListSectionsSortOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SectionsResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sort_by: Union[Unset, ListSectionsSortBy] = UNSET,
    sort_order: Union[Unset, ListSectionsSortOrder] = UNSET,
) -> Optional[SectionsResponse]:
    """List Sections

     Lists all the sections in Help Center or in a specific [category](/api-reference/help_center/help-
    center-api/categories).

    The `{locale}` is required only for end users and anomynous users. Admins and agents can omit it.

    #### Allowed for

    * Anonymous users

    The response will list only the sections that the requesting agent,
    end user, or anonymous user can view in the help center.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sorting

    You can sort the results with the `sort_by` and `sort_order` query string parameters.

    ```
    GET /api/v2/help_center/en-us/sections.json?sort_by=updated_at&sort_order=asc
    ```

    The `sort_by` parameter can have one of the following values:

    | value         | description
    | ------------- | -----------
    | `position`    | order set manually using the Arrange Content page. Default order
    | `created_at`  | order by creation time
    | `updated_at`  | order by update time

    The `sort_order` parameter can have one of the following values:

    | value   | description
    | ------- | -----------
    | `asc`   | ascending order
    | `desc`  | descending order

    #### Sideloads

    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | categories    | the category
    | translations  | the section and category translations, if any

    Unlike other sideloads, translations are embedded within the section because they're
    not shared between resources.
    Category translations are only sideloaded if categories are.

    Args:
        locale (str):  Example: en-us.
        sort_by (Union[Unset, ListSectionsSortBy]):
        sort_order (Union[Unset, ListSectionsSortOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SectionsResponse
    """

    return sync_detailed(
        locale=locale,
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    locale: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sort_by: Union[Unset, ListSectionsSortBy] = UNSET,
    sort_order: Union[Unset, ListSectionsSortOrder] = UNSET,
) -> Response[SectionsResponse]:
    """List Sections

     Lists all the sections in Help Center or in a specific [category](/api-reference/help_center/help-
    center-api/categories).

    The `{locale}` is required only for end users and anomynous users. Admins and agents can omit it.

    #### Allowed for

    * Anonymous users

    The response will list only the sections that the requesting agent,
    end user, or anonymous user can view in the help center.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sorting

    You can sort the results with the `sort_by` and `sort_order` query string parameters.

    ```
    GET /api/v2/help_center/en-us/sections.json?sort_by=updated_at&sort_order=asc
    ```

    The `sort_by` parameter can have one of the following values:

    | value         | description
    | ------------- | -----------
    | `position`    | order set manually using the Arrange Content page. Default order
    | `created_at`  | order by creation time
    | `updated_at`  | order by update time

    The `sort_order` parameter can have one of the following values:

    | value   | description
    | ------- | -----------
    | `asc`   | ascending order
    | `desc`  | descending order

    #### Sideloads

    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | categories    | the category
    | translations  | the section and category translations, if any

    Unlike other sideloads, translations are embedded within the section because they're
    not shared between resources.
    Category translations are only sideloaded if categories are.

    Args:
        locale (str):  Example: en-us.
        sort_by (Union[Unset, ListSectionsSortBy]):
        sort_order (Union[Unset, ListSectionsSortOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SectionsResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sort_by: Union[Unset, ListSectionsSortBy] = UNSET,
    sort_order: Union[Unset, ListSectionsSortOrder] = UNSET,
) -> Optional[SectionsResponse]:
    """List Sections

     Lists all the sections in Help Center or in a specific [category](/api-reference/help_center/help-
    center-api/categories).

    The `{locale}` is required only for end users and anomynous users. Admins and agents can omit it.

    #### Allowed for

    * Anonymous users

    The response will list only the sections that the requesting agent,
    end user, or anonymous user can view in the help center.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sorting

    You can sort the results with the `sort_by` and `sort_order` query string parameters.

    ```
    GET /api/v2/help_center/en-us/sections.json?sort_by=updated_at&sort_order=asc
    ```

    The `sort_by` parameter can have one of the following values:

    | value         | description
    | ------------- | -----------
    | `position`    | order set manually using the Arrange Content page. Default order
    | `created_at`  | order by creation time
    | `updated_at`  | order by update time

    The `sort_order` parameter can have one of the following values:

    | value   | description
    | ------- | -----------
    | `asc`   | ascending order
    | `desc`  | descending order

    #### Sideloads

    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | categories    | the category
    | translations  | the section and category translations, if any

    Unlike other sideloads, translations are embedded within the section because they're
    not shared between resources.
    Category translations are only sideloaded if categories are.

    Args:
        locale (str):  Example: en-us.
        sort_by (Union[Unset, ListSectionsSortBy]):
        sort_order (Union[Unset, ListSectionsSortOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SectionsResponse
    """

    return (
        await asyncio_detailed(
            locale=locale,
            client=client,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    ).parsed
