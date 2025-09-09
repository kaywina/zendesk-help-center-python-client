from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.comment_response import CommentResponse
from ...types import Response


def _get_kwargs(
    locale: str,
    article_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v2/help_center/{locale}/articles/{article_id}/comments",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CommentResponse]:
    if response.status_code == 200:
        response_200 = CommentResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CommentResponse]:
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
) -> Response[CommentResponse]:
    r"""Create Comment

     Adds a comment to the specified [article](/api-reference/help_center/help-center-api/articles).
    Because comments are associated
    with a specific article translation, or locale, you must specify a locale.

    #### Allowed for

    * End users

    Agents with the Help Center manager role can optionally supply a `created_at` as part of the
    `comment` object. If not provided, `created_at` is set to the current time.

    Supplying a `notify_subscribers` property with a value of false will prevent subscribers to the
    comment's article from receiving a comment creation email notification. This can be helpful when
    creating many comments at a time. Specify the property in the root of the JSON object, not in the
    \"comment\" object.

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommentResponse]
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
) -> Optional[CommentResponse]:
    r"""Create Comment

     Adds a comment to the specified [article](/api-reference/help_center/help-center-api/articles).
    Because comments are associated
    with a specific article translation, or locale, you must specify a locale.

    #### Allowed for

    * End users

    Agents with the Help Center manager role can optionally supply a `created_at` as part of the
    `comment` object. If not provided, `created_at` is set to the current time.

    Supplying a `notify_subscribers` property with a value of false will prevent subscribers to the
    comment's article from receiving a comment creation email notification. This can be helpful when
    creating many comments at a time. Specify the property in the root of the JSON object, not in the
    \"comment\" object.

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommentResponse
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
) -> Response[CommentResponse]:
    r"""Create Comment

     Adds a comment to the specified [article](/api-reference/help_center/help-center-api/articles).
    Because comments are associated
    with a specific article translation, or locale, you must specify a locale.

    #### Allowed for

    * End users

    Agents with the Help Center manager role can optionally supply a `created_at` as part of the
    `comment` object. If not provided, `created_at` is set to the current time.

    Supplying a `notify_subscribers` property with a value of false will prevent subscribers to the
    comment's article from receiving a comment creation email notification. This can be helpful when
    creating many comments at a time. Specify the property in the root of the JSON object, not in the
    \"comment\" object.

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommentResponse]
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
) -> Optional[CommentResponse]:
    r"""Create Comment

     Adds a comment to the specified [article](/api-reference/help_center/help-center-api/articles).
    Because comments are associated
    with a specific article translation, or locale, you must specify a locale.

    #### Allowed for

    * End users

    Agents with the Help Center manager role can optionally supply a `created_at` as part of the
    `comment` object. If not provided, `created_at` is set to the current time.

    Supplying a `notify_subscribers` property with a value of false will prevent subscribers to the
    comment's article from receiving a comment creation email notification. This can be helpful when
    creating many comments at a time. Specify the property in the root of the JSON object, not in the
    \"comment\" object.

    Args:
        locale (str):  Example: en-us.
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommentResponse
    """

    return (
        await asyncio_detailed(
            locale=locale,
            article_id=article_id,
            client=client,
        )
    ).parsed
