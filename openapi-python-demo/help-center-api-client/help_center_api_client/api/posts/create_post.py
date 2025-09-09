from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_response import PostResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/community/posts",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PostResponse]:
    if response.status_code == 201:
        response_201 = PostResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PostResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PostResponse]:
    r"""Create Post

     Adds a post to the specified [topic](/api-reference/help_center/help-center-api/topics).

    #### Allowed for

    * End users

    Agents with the Help Center manager role can optionally supply an
    `author_id` as part of the `post` object. If it is provided, the post's
    author will be set to the value of the `author_id` key.

    Agents with the Help Center manager role can optionally supply a `created_at` as part of the `post`
    object. If it is not provided `created_at` is set to the current time.

    Supplying a `notify_subscribers` property with a value of false will prevent subscribers to the
    post's topic from receiving a post creation email notification. This can be helpful when creating
    many posts at a time. Specify the property in the root of the JSON object, not in the \"post\"
    object.
    Optionally, you can attach existing [content tags](/api-reference/help_center/help-center-
    api/content_tags) by specifying their ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PostResponse]:
    r"""Create Post

     Adds a post to the specified [topic](/api-reference/help_center/help-center-api/topics).

    #### Allowed for

    * End users

    Agents with the Help Center manager role can optionally supply an
    `author_id` as part of the `post` object. If it is provided, the post's
    author will be set to the value of the `author_id` key.

    Agents with the Help Center manager role can optionally supply a `created_at` as part of the `post`
    object. If it is not provided `created_at` is set to the current time.

    Supplying a `notify_subscribers` property with a value of false will prevent subscribers to the
    post's topic from receiving a post creation email notification. This can be helpful when creating
    many posts at a time. Specify the property in the root of the JSON object, not in the \"post\"
    object.
    Optionally, you can attach existing [content tags](/api-reference/help_center/help-center-
    api/content_tags) by specifying their ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PostResponse]:
    r"""Create Post

     Adds a post to the specified [topic](/api-reference/help_center/help-center-api/topics).

    #### Allowed for

    * End users

    Agents with the Help Center manager role can optionally supply an
    `author_id` as part of the `post` object. If it is provided, the post's
    author will be set to the value of the `author_id` key.

    Agents with the Help Center manager role can optionally supply a `created_at` as part of the `post`
    object. If it is not provided `created_at` is set to the current time.

    Supplying a `notify_subscribers` property with a value of false will prevent subscribers to the
    post's topic from receiving a post creation email notification. This can be helpful when creating
    many posts at a time. Specify the property in the root of the JSON object, not in the \"post\"
    object.
    Optionally, you can attach existing [content tags](/api-reference/help_center/help-center-
    api/content_tags) by specifying their ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PostResponse]:
    r"""Create Post

     Adds a post to the specified [topic](/api-reference/help_center/help-center-api/topics).

    #### Allowed for

    * End users

    Agents with the Help Center manager role can optionally supply an
    `author_id` as part of the `post` object. If it is provided, the post's
    author will be set to the value of the `author_id` key.

    Agents with the Help Center manager role can optionally supply a `created_at` as part of the `post`
    object. If it is not provided `created_at` is set to the current time.

    Supplying a `notify_subscribers` property with a value of false will prevent subscribers to the
    post's topic from receiving a post creation email notification. This can be helpful when creating
    many posts at a time. Specify the property in the root of the JSON object, not in the \"post\"
    object.
    Optionally, you can attach existing [content tags](/api-reference/help_center/help-center-
    api/content_tags) by specifying their ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
