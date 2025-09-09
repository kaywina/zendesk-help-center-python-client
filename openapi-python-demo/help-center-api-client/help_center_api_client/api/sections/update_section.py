from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request_error_response import BadRequestErrorResponse
from ...models.section_put_request import SectionPutRequest
from ...models.section_response import SectionResponse
from ...types import Response


def _get_kwargs(
    locale: str,
    section_id: int,
    *,
    body: SectionPutRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v2/help_center/{locale}/sections/{section_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequestErrorResponse, SectionResponse]]:
    if response.status_code == 200:
        response_200 = SectionResponse.from_dict(response.json())

        return response_200

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
    section_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SectionPutRequest,
) -> Response[Union[BadRequestErrorResponse, SectionResponse]]:
    """Update Section

     Update section. This endpoint updates section-level data, specifically:

    * name (in the source locale)
    * description (in the source locale)
    * position
    * sorting
    * category_id
    * parent_section_id
    * theme_template

    To update non-source section translations, see [Translations](/api-reference/help_center/help-
    center-api/translations).

    #### Allowed for

    * Help Center managers

    Args:
        locale (str):  Example: en-us.
        section_id (int):
        body (SectionPutRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestErrorResponse, SectionResponse]]
    """

    kwargs = _get_kwargs(
        locale=locale,
        section_id=section_id,
        body=body,
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
    body: SectionPutRequest,
) -> Optional[Union[BadRequestErrorResponse, SectionResponse]]:
    """Update Section

     Update section. This endpoint updates section-level data, specifically:

    * name (in the source locale)
    * description (in the source locale)
    * position
    * sorting
    * category_id
    * parent_section_id
    * theme_template

    To update non-source section translations, see [Translations](/api-reference/help_center/help-
    center-api/translations).

    #### Allowed for

    * Help Center managers

    Args:
        locale (str):  Example: en-us.
        section_id (int):
        body (SectionPutRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestErrorResponse, SectionResponse]
    """

    return sync_detailed(
        locale=locale,
        section_id=section_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    locale: str,
    section_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SectionPutRequest,
) -> Response[Union[BadRequestErrorResponse, SectionResponse]]:
    """Update Section

     Update section. This endpoint updates section-level data, specifically:

    * name (in the source locale)
    * description (in the source locale)
    * position
    * sorting
    * category_id
    * parent_section_id
    * theme_template

    To update non-source section translations, see [Translations](/api-reference/help_center/help-
    center-api/translations).

    #### Allowed for

    * Help Center managers

    Args:
        locale (str):  Example: en-us.
        section_id (int):
        body (SectionPutRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestErrorResponse, SectionResponse]]
    """

    kwargs = _get_kwargs(
        locale=locale,
        section_id=section_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: str,
    section_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SectionPutRequest,
) -> Optional[Union[BadRequestErrorResponse, SectionResponse]]:
    """Update Section

     Update section. This endpoint updates section-level data, specifically:

    * name (in the source locale)
    * description (in the source locale)
    * position
    * sorting
    * category_id
    * parent_section_id
    * theme_template

    To update non-source section translations, see [Translations](/api-reference/help_center/help-
    center-api/translations).

    #### Allowed for

    * Help Center managers

    Args:
        locale (str):  Example: en-us.
        section_id (int):
        body (SectionPutRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestErrorResponse, SectionResponse]
    """

    return (
        await asyncio_detailed(
            locale=locale,
            section_id=section_id,
            client=client,
            body=body,
        )
    ).parsed
