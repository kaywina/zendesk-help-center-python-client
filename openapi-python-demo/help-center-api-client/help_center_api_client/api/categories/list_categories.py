from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.categories_response import CategoriesResponse
from ...models.list_categories_sort_by import ListCategoriesSortBy
from ...models.list_categories_sort_order import ListCategoriesSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    locale: str,
    *,
    sort_by: Union[Unset, ListCategoriesSortBy] = UNSET,
    sort_order: Union[Unset, ListCategoriesSortOrder] = UNSET,
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
        "url": f"/api/v2/help_center/{locale}/categories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CategoriesResponse]:
    if response.status_code == 200:
        response_200 = CategoriesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CategoriesResponse]:
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
    sort_by: Union[Unset, ListCategoriesSortBy] = UNSET,
    sort_order: Union[Unset, ListCategoriesSortOrder] = UNSET,
) -> Response[CategoriesResponse]:
    """List Categories

     **Note**: `{/locale}` is an optional parameter for admins and agents. End users and anonymous users
    must provide the parameter.

    #### Allowed for

    * Anonymous users

    The response will list only the categories that the agent, end user, or
    anonymous user can view in the help center.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sorting

    You can sort the results with the `sort_by` and `sort_order` query string parameters.

    ```
    GET /api/v2/help_center/en-us/categories.json?sort_by=updated_at&sort_order=asc
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
    | translations  | the category translations, if any

    Translations are embedded within the category because they're
    not shared between resources.

    Args:
        locale (str):  Example: en-us.
        sort_by (Union[Unset, ListCategoriesSortBy]):
        sort_order (Union[Unset, ListCategoriesSortOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CategoriesResponse]
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
    sort_by: Union[Unset, ListCategoriesSortBy] = UNSET,
    sort_order: Union[Unset, ListCategoriesSortOrder] = UNSET,
) -> Optional[CategoriesResponse]:
    """List Categories

     **Note**: `{/locale}` is an optional parameter for admins and agents. End users and anonymous users
    must provide the parameter.

    #### Allowed for

    * Anonymous users

    The response will list only the categories that the agent, end user, or
    anonymous user can view in the help center.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sorting

    You can sort the results with the `sort_by` and `sort_order` query string parameters.

    ```
    GET /api/v2/help_center/en-us/categories.json?sort_by=updated_at&sort_order=asc
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
    | translations  | the category translations, if any

    Translations are embedded within the category because they're
    not shared between resources.

    Args:
        locale (str):  Example: en-us.
        sort_by (Union[Unset, ListCategoriesSortBy]):
        sort_order (Union[Unset, ListCategoriesSortOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CategoriesResponse
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
    sort_by: Union[Unset, ListCategoriesSortBy] = UNSET,
    sort_order: Union[Unset, ListCategoriesSortOrder] = UNSET,
) -> Response[CategoriesResponse]:
    """List Categories

     **Note**: `{/locale}` is an optional parameter for admins and agents. End users and anonymous users
    must provide the parameter.

    #### Allowed for

    * Anonymous users

    The response will list only the categories that the agent, end user, or
    anonymous user can view in the help center.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sorting

    You can sort the results with the `sort_by` and `sort_order` query string parameters.

    ```
    GET /api/v2/help_center/en-us/categories.json?sort_by=updated_at&sort_order=asc
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
    | translations  | the category translations, if any

    Translations are embedded within the category because they're
    not shared between resources.

    Args:
        locale (str):  Example: en-us.
        sort_by (Union[Unset, ListCategoriesSortBy]):
        sort_order (Union[Unset, ListCategoriesSortOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CategoriesResponse]
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
    sort_by: Union[Unset, ListCategoriesSortBy] = UNSET,
    sort_order: Union[Unset, ListCategoriesSortOrder] = UNSET,
) -> Optional[CategoriesResponse]:
    """List Categories

     **Note**: `{/locale}` is an optional parameter for admins and agents. End users and anonymous users
    must provide the parameter.

    #### Allowed for

    * Anonymous users

    The response will list only the categories that the agent, end user, or
    anonymous user can view in the help center.

    #### Pagination

    * Cursor pagination (recommended)
    * Offset pagination

    See [Pagination](/api-reference/introduction/pagination/).

    #### Sorting

    You can sort the results with the `sort_by` and `sort_order` query string parameters.

    ```
    GET /api/v2/help_center/en-us/categories.json?sort_by=updated_at&sort_order=asc
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
    | translations  | the category translations, if any

    Translations are embedded within the category because they're
    not shared between resources.

    Args:
        locale (str):  Example: en-us.
        sort_by (Union[Unset, ListCategoriesSortBy]):
        sort_order (Union[Unset, ListCategoriesSortOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CategoriesResponse
    """

    return (
        await asyncio_detailed(
            locale=locale,
            client=client,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    ).parsed
