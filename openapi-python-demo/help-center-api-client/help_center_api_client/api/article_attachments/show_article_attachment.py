from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.article_attachment_response import ArticleAttachmentResponse
from ...types import Response


def _get_kwargs(
    article_id: int,
    article_attachment_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/help_center/articles/{article_id}/attachments/{article_attachment_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ArticleAttachmentResponse]:
    if response.status_code == 200:
        response_200 = ArticleAttachmentResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ArticleAttachmentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    article_id: int,
    article_attachment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ArticleAttachmentResponse]:
    """Show Article Attachment

     Shows the properties of the specified attachment.

    **Note**: Omit `{/article_id}` to access unassociated article attachments.

    #### Allowed for

    * Agents
    * End users, as long as they can view the associated article

    Args:
        article_id (int):
        article_attachment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArticleAttachmentResponse]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
        article_attachment_id=article_attachment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    article_id: int,
    article_attachment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ArticleAttachmentResponse]:
    """Show Article Attachment

     Shows the properties of the specified attachment.

    **Note**: Omit `{/article_id}` to access unassociated article attachments.

    #### Allowed for

    * Agents
    * End users, as long as they can view the associated article

    Args:
        article_id (int):
        article_attachment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArticleAttachmentResponse
    """

    return sync_detailed(
        article_id=article_id,
        article_attachment_id=article_attachment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    article_id: int,
    article_attachment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ArticleAttachmentResponse]:
    """Show Article Attachment

     Shows the properties of the specified attachment.

    **Note**: Omit `{/article_id}` to access unassociated article attachments.

    #### Allowed for

    * Agents
    * End users, as long as they can view the associated article

    Args:
        article_id (int):
        article_attachment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArticleAttachmentResponse]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
        article_attachment_id=article_attachment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    article_id: int,
    article_attachment_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ArticleAttachmentResponse]:
    """Show Article Attachment

     Shows the properties of the specified attachment.

    **Note**: Omit `{/article_id}` to access unassociated article attachments.

    #### Allowed for

    * Agents
    * End users, as long as they can view the associated article

    Args:
        article_id (int):
        article_attachment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArticleAttachmentResponse
    """

    return (
        await asyncio_detailed(
            article_id=article_id,
            article_attachment_id=article_attachment_id,
            client=client,
        )
    ).parsed
