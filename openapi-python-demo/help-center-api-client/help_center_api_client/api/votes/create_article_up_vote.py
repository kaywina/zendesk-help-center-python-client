from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.vote_response import VoteResponse
from ...types import Response


def _get_kwargs(
    locale: str,
    article_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v2/help_center/{locale}/articles/{article_id}/up",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[VoteResponse]:
    if response.status_code == 200:
        response_200 = VoteResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[VoteResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: str,
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[VoteResponse]:
    """Create Vote

     Creates an up or down vote for a given [article](/api-reference/help_center/help-center-
    api/articles), [article comment](/api-reference/help_center/help-center-api/article_comments/),
    [post](/api-reference/help_center/help-center-api/posts), or [post comment](/api-
    reference/help_center/help-center-api/post_comments).
    If a vote already exists for the source object, it's updated.

    #### Allowed for

    * End users

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VoteResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        article_id=article_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: str,
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[VoteResponse]:
    """Create Vote

     Creates an up or down vote for a given [article](/api-reference/help_center/help-center-
    api/articles), [article comment](/api-reference/help_center/help-center-api/article_comments/),
    [post](/api-reference/help_center/help-center-api/posts), or [post comment](/api-
    reference/help_center/help-center-api/post_comments).
    If a vote already exists for the source object, it's updated.

    #### Allowed for

    * End users

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VoteResponse
    """

    return sync_detailed(
        locale=locale,
        article_id=article_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    locale: str,
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[VoteResponse]:
    """Create Vote

     Creates an up or down vote for a given [article](/api-reference/help_center/help-center-
    api/articles), [article comment](/api-reference/help_center/help-center-api/article_comments/),
    [post](/api-reference/help_center/help-center-api/posts), or [post comment](/api-
    reference/help_center/help-center-api/post_comments).
    If a vote already exists for the source object, it's updated.

    #### Allowed for

    * End users

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VoteResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        article_id=article_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: str,
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[VoteResponse]:
    """Create Vote

     Creates an up or down vote for a given [article](/api-reference/help_center/help-center-
    api/articles), [article comment](/api-reference/help_center/help-center-api/article_comments/),
    [post](/api-reference/help_center/help-center-api/posts), or [post comment](/api-
    reference/help_center/help-center-api/post_comments).
    If a vote already exists for the source object, it's updated.

    #### Allowed for

    * End users

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VoteResponse
    """

    return (
        await asyncio_detailed(
            locale=locale,
            article_id=article_id,
            client=client,
        )
    ).parsed
