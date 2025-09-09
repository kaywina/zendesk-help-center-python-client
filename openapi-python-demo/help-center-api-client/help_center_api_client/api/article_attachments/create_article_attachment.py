from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.article_attachment_response import ArticleAttachmentResponse
from ...types import Response


def _get_kwargs(
    article_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v2/help_center/articles/{article_id}/attachments",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ArticleAttachmentResponse]:
    if response.status_code == 201:
        response_201 = ArticleAttachmentResponse.from_dict(response.json())

        return response_201

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
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ArticleAttachmentResponse]:
    """Create Article Attachment

     Creates an attachment for the specified [article](/api-reference/help_center/help-center-
    api/articles). You can specify whether the attachment is inline or not. The default is false.

    The `guide_media_id` parameter is required and must be submitted as multipart form data. This is the
    id of the media object to be attached to the article. See [Create guide media object](/api-
    reference/help_center/help-center-api/guide_medias/#create-guide-media). The 'inline' parameter is
    optional.

    If your integration depends on keeping the translation body in sync with an external system, create
    a separate article attachment for each translation and set the locale in advance.
    Inline article attachments are automatically assigned a locale when they are embedded in a
    translation body. If the same attachment is inserted in multiple translations, it will create
    multiple article attachment records, all linked to the same file, and the references in the
    translation bodies will be updated accordingly.

    *Notes:*

      - First create a [Guide media object](/api-reference/help_center/help-center-
    api/guide_medias/#create-guide-media) and then [create an article attachment](/api-
    reference/help_center/help-center-api/article_attachments/#create-article-attachment) with the value
    of the media object's `id`. When creating the attachment, use the value of the media object's `id`
    as the value of the attachment's `guide_media_id` property.
      - Inline article attachments that are no longer embedded in the translation get deleted. However
    the corresponding file is kept in the account's media library.

    #### Allowed for

    * Agents

    Args:
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArticleAttachmentResponse]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ArticleAttachmentResponse]:
    """Create Article Attachment

     Creates an attachment for the specified [article](/api-reference/help_center/help-center-
    api/articles). You can specify whether the attachment is inline or not. The default is false.

    The `guide_media_id` parameter is required and must be submitted as multipart form data. This is the
    id of the media object to be attached to the article. See [Create guide media object](/api-
    reference/help_center/help-center-api/guide_medias/#create-guide-media). The 'inline' parameter is
    optional.

    If your integration depends on keeping the translation body in sync with an external system, create
    a separate article attachment for each translation and set the locale in advance.
    Inline article attachments are automatically assigned a locale when they are embedded in a
    translation body. If the same attachment is inserted in multiple translations, it will create
    multiple article attachment records, all linked to the same file, and the references in the
    translation bodies will be updated accordingly.

    *Notes:*

      - First create a [Guide media object](/api-reference/help_center/help-center-
    api/guide_medias/#create-guide-media) and then [create an article attachment](/api-
    reference/help_center/help-center-api/article_attachments/#create-article-attachment) with the value
    of the media object's `id`. When creating the attachment, use the value of the media object's `id`
    as the value of the attachment's `guide_media_id` property.
      - Inline article attachments that are no longer embedded in the translation get deleted. However
    the corresponding file is kept in the account's media library.

    #### Allowed for

    * Agents

    Args:
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArticleAttachmentResponse
    """

    return sync_detailed(
        article_id=article_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ArticleAttachmentResponse]:
    """Create Article Attachment

     Creates an attachment for the specified [article](/api-reference/help_center/help-center-
    api/articles). You can specify whether the attachment is inline or not. The default is false.

    The `guide_media_id` parameter is required and must be submitted as multipart form data. This is the
    id of the media object to be attached to the article. See [Create guide media object](/api-
    reference/help_center/help-center-api/guide_medias/#create-guide-media). The 'inline' parameter is
    optional.

    If your integration depends on keeping the translation body in sync with an external system, create
    a separate article attachment for each translation and set the locale in advance.
    Inline article attachments are automatically assigned a locale when they are embedded in a
    translation body. If the same attachment is inserted in multiple translations, it will create
    multiple article attachment records, all linked to the same file, and the references in the
    translation bodies will be updated accordingly.

    *Notes:*

      - First create a [Guide media object](/api-reference/help_center/help-center-
    api/guide_medias/#create-guide-media) and then [create an article attachment](/api-
    reference/help_center/help-center-api/article_attachments/#create-article-attachment) with the value
    of the media object's `id`. When creating the attachment, use the value of the media object's `id`
    as the value of the attachment's `guide_media_id` property.
      - Inline article attachments that are no longer embedded in the translation get deleted. However
    the corresponding file is kept in the account's media library.

    #### Allowed for

    * Agents

    Args:
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArticleAttachmentResponse]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    article_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ArticleAttachmentResponse]:
    """Create Article Attachment

     Creates an attachment for the specified [article](/api-reference/help_center/help-center-
    api/articles). You can specify whether the attachment is inline or not. The default is false.

    The `guide_media_id` parameter is required and must be submitted as multipart form data. This is the
    id of the media object to be attached to the article. See [Create guide media object](/api-
    reference/help_center/help-center-api/guide_medias/#create-guide-media). The 'inline' parameter is
    optional.

    If your integration depends on keeping the translation body in sync with an external system, create
    a separate article attachment for each translation and set the locale in advance.
    Inline article attachments are automatically assigned a locale when they are embedded in a
    translation body. If the same attachment is inserted in multiple translations, it will create
    multiple article attachment records, all linked to the same file, and the references in the
    translation bodies will be updated accordingly.

    *Notes:*

      - First create a [Guide media object](/api-reference/help_center/help-center-
    api/guide_medias/#create-guide-media) and then [create an article attachment](/api-
    reference/help_center/help-center-api/article_attachments/#create-article-attachment) with the value
    of the media object's `id`. When creating the attachment, use the value of the media object's `id`
    as the value of the attachment's `guide_media_id` property.
      - Inline article attachments that are no longer embedded in the translation get deleted. However
    the corresponding file is kept in the account's media library.

    #### Allowed for

    * Agents

    Args:
        article_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArticleAttachmentResponse
    """

    return (
        await asyncio_detailed(
            article_id=article_id,
            client=client,
        )
    ).parsed
