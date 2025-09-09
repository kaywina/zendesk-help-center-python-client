from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request_error_response import BadRequestErrorResponse
from ...models.section_response import SectionResponse
from ...types import Response


def _get_kwargs(
    locale: str,
    category_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v2/help_center/{locale}/categories/{category_id}/sections",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequestErrorResponse, SectionResponse]]:
    if response.status_code == 201:
        response_201 = SectionResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = BadRequestErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BadRequestErrorResponse, SectionResponse]]:
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
) -> Response[Union[BadRequestErrorResponse, SectionResponse]]:
    """Create Section

     Creates a section in a given [category](/api-reference/help_center/help-center-api/categories). You
    must
    specify a section name and locale. The locale can be omitted if it's specified
    in the URL. Optionally, you can specify multiple [translations](/api-reference/help_center/help-
    center-api/translations)
    for the section. The specified locales must be enabled for
    the current Help Center.

    #### Allowed for

    * Agents

    Args:
        locale (str):  Example: en-us.
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestErrorResponse, SectionResponse]]
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
) -> Optional[Union[BadRequestErrorResponse, SectionResponse]]:
    """Create Section

     Creates a section in a given [category](/api-reference/help_center/help-center-api/categories). You
    must
    specify a section name and locale. The locale can be omitted if it's specified
    in the URL. Optionally, you can specify multiple [translations](/api-reference/help_center/help-
    center-api/translations)
    for the section. The specified locales must be enabled for
    the current Help Center.

    #### Allowed for

    * Agents

    Args:
        locale (str):  Example: en-us.
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestErrorResponse, SectionResponse]
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
) -> Response[Union[BadRequestErrorResponse, SectionResponse]]:
    """Create Section

     Creates a section in a given [category](/api-reference/help_center/help-center-api/categories). You
    must
    specify a section name and locale. The locale can be omitted if it's specified
    in the URL. Optionally, you can specify multiple [translations](/api-reference/help_center/help-
    center-api/translations)
    for the section. The specified locales must be enabled for
    the current Help Center.

    #### Allowed for

    * Agents

    Args:
        locale (str):  Example: en-us.
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestErrorResponse, SectionResponse]]
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
) -> Optional[Union[BadRequestErrorResponse, SectionResponse]]:
    """Create Section

     Creates a section in a given [category](/api-reference/help_center/help-center-api/categories). You
    must
    specify a section name and locale. The locale can be omitted if it's specified
    in the URL. Optionally, you can specify multiple [translations](/api-reference/help_center/help-
    center-api/translations)
    for the section. The specified locales must be enabled for
    the current Help Center.

    #### Allowed for

    * Agents

    Args:
        locale (str):  Example: en-us.
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestErrorResponse, SectionResponse]
    """

    return (
        await asyncio_detailed(
            locale=locale,
            category_id=category_id,
            client=client,
        )
    ).parsed
