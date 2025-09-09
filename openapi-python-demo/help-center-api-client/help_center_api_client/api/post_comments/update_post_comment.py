from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_comment_response import PostCommentResponse
from ...types import Response


def _get_kwargs(
    post_id: int,
    post_comment_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v2/community/posts/{post_id}/comments/{post_comment_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostCommentResponse]:
    if response.status_code == 200:
        response_200 = PostCommentResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostCommentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    post_id: int,
    post_comment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PostCommentResponse]:
    """Update Comment

     Updates the specified comment.

    #### Allowed for

    * Agents
    * The end user who created the comment

    Args:
        post_id (int):
        post_comment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCommentResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        post_comment_id=post_comment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    post_id: int,
    post_comment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PostCommentResponse]:
    """Update Comment

     Updates the specified comment.

    #### Allowed for

    * Agents
    * The end user who created the comment

    Args:
        post_id (int):
        post_comment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCommentResponse
    """

    return sync_detailed(
        post_id=post_id,
        post_comment_id=post_comment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    post_id: int,
    post_comment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PostCommentResponse]:
    """Update Comment

     Updates the specified comment.

    #### Allowed for

    * Agents
    * The end user who created the comment

    Args:
        post_id (int):
        post_comment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCommentResponse]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        post_comment_id=post_comment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    post_id: int,
    post_comment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PostCommentResponse]:
    """Update Comment

     Updates the specified comment.

    #### Allowed for

    * Agents
    * The end user who created the comment

    Args:
        post_id (int):
        post_comment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCommentResponse
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            post_comment_id=post_comment_id,
            client=client,
        )
    ).parsed
