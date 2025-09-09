from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.section_response import SectionResponse
from ...types import Response


def _get_kwargs(
    locale: str,
    section_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/help_center/{locale}/sections/{section_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SectionResponse]:
    if response.status_code == 200:
        response_200 = SectionResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SectionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: str,
    section_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SectionResponse]:
    """Show Section

     **Note**: `{/locale}` is an optional parameter for admins and agents. End users and anonymous users
    must provide the parameter.

    #### Allowed for

    * Anonymous users

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | categories    | the category
    | translations  | the section and category translations, if any

    Unlike other sideloads, translations are embedded within the section since they're
    not shared between resources.
    [Category](/api-reference/help_center/help-center-api/categories) translations are only sideloaded
    if categories are.

    Args:
        locale (str):  Example: en-us.
        section_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SectionResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        section_id=section_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: str,
    section_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[SectionResponse]:
    """Show Section

     **Note**: `{/locale}` is an optional parameter for admins and agents. End users and anonymous users
    must provide the parameter.

    #### Allowed for

    * Anonymous users

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | categories    | the category
    | translations  | the section and category translations, if any

    Unlike other sideloads, translations are embedded within the section since they're
    not shared between resources.
    [Category](/api-reference/help_center/help-center-api/categories) translations are only sideloaded
    if categories are.

    Args:
        locale (str):  Example: en-us.
        section_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SectionResponse
    """

    return sync_detailed(
        locale=locale,
        section_id=section_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    locale: str,
    section_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SectionResponse]:
    """Show Section

     **Note**: `{/locale}` is an optional parameter for admins and agents. End users and anonymous users
    must provide the parameter.

    #### Allowed for

    * Anonymous users

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | categories    | the category
    | translations  | the section and category translations, if any

    Unlike other sideloads, translations are embedded within the section since they're
    not shared between resources.
    [Category](/api-reference/help_center/help-center-api/categories) translations are only sideloaded
    if categories are.

    Args:
        locale (str):  Example: en-us.
        section_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SectionResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        section_id=section_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: str,
    section_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[SectionResponse]:
    """Show Section

     **Note**: `{/locale}` is an optional parameter for admins and agents. End users and anonymous users
    must provide the parameter.

    #### Allowed for

    * Anonymous users

    #### Sideloads
    The following sideloads are supported:

    | Name          | Will sideload
    |---------------|--------------
    | categories    | the category
    | translations  | the section and category translations, if any

    Unlike other sideloads, translations are embedded within the section since they're
    not shared between resources.
    [Category](/api-reference/help_center/help-center-api/categories) translations are only sideloaded
    if categories are.

    Args:
        locale (str):  Example: en-us.
        section_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SectionResponse
    """

    return (
        await asyncio_detailed(
            locale=locale,
            section_id=section_id,
            client=client,
        )
    ).parsed
