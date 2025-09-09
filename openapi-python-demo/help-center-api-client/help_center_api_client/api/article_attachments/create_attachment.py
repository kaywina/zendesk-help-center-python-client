from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.article_attachment_response import ArticleAttachmentResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/help_center/articles/attachments",
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
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ArticleAttachmentResponse]:
    """Create Unassociated Attachment

     You can use this endpoint for bulk imports. It lets you upload a file without associating it
    to an article until later. See [Associate Attachments in Bulk to Article](/api-
    reference/help_center/help-center-api/articles#associate-attachments-in-bulk-to-article).

     If you plan on adding attachments to article translations, import a separate article attachment for
    each translation and set the locale in advance. For more information on translation attachments, see
    [Create Article Attachment](/api-reference/help_center/help-center-api/article_attachments/#create-
    article-attachment).

    *Notes:*

      - Zendesk recommends to first create a [Guide media object](/api-reference/help_center/help-
    center-api/guide_medias/#create-guide-media) and then [create an article attachment](/api-
    reference/help_center/help-center-api/article_attachments/#create-article-attachment) with the value
    of the media object's `id`. When creating the attachment, use the value of the media object's `id`
    as the value of the attachment's `guide_media_id` property.
      - Associate attachments to articles as soon as possible. For example, if you use the endpoint to
    bulk-import inline images, only signed-in end users can see the images; anonymous users don't have
    permission to view unassociated images. Also, from time to time, we purge old article attachments
    not associated to any article. To ensure you don't lose an uploaded file, associate it to an
    article.
    #### Allowed for

      * Agents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArticleAttachmentResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ArticleAttachmentResponse]:
    """Create Unassociated Attachment

     You can use this endpoint for bulk imports. It lets you upload a file without associating it
    to an article until later. See [Associate Attachments in Bulk to Article](/api-
    reference/help_center/help-center-api/articles#associate-attachments-in-bulk-to-article).

     If you plan on adding attachments to article translations, import a separate article attachment for
    each translation and set the locale in advance. For more information on translation attachments, see
    [Create Article Attachment](/api-reference/help_center/help-center-api/article_attachments/#create-
    article-attachment).

    *Notes:*

      - Zendesk recommends to first create a [Guide media object](/api-reference/help_center/help-
    center-api/guide_medias/#create-guide-media) and then [create an article attachment](/api-
    reference/help_center/help-center-api/article_attachments/#create-article-attachment) with the value
    of the media object's `id`. When creating the attachment, use the value of the media object's `id`
    as the value of the attachment's `guide_media_id` property.
      - Associate attachments to articles as soon as possible. For example, if you use the endpoint to
    bulk-import inline images, only signed-in end users can see the images; anonymous users don't have
    permission to view unassociated images. Also, from time to time, we purge old article attachments
    not associated to any article. To ensure you don't lose an uploaded file, associate it to an
    article.
    #### Allowed for

      * Agents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArticleAttachmentResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ArticleAttachmentResponse]:
    """Create Unassociated Attachment

     You can use this endpoint for bulk imports. It lets you upload a file without associating it
    to an article until later. See [Associate Attachments in Bulk to Article](/api-
    reference/help_center/help-center-api/articles#associate-attachments-in-bulk-to-article).

     If you plan on adding attachments to article translations, import a separate article attachment for
    each translation and set the locale in advance. For more information on translation attachments, see
    [Create Article Attachment](/api-reference/help_center/help-center-api/article_attachments/#create-
    article-attachment).

    *Notes:*

      - Zendesk recommends to first create a [Guide media object](/api-reference/help_center/help-
    center-api/guide_medias/#create-guide-media) and then [create an article attachment](/api-
    reference/help_center/help-center-api/article_attachments/#create-article-attachment) with the value
    of the media object's `id`. When creating the attachment, use the value of the media object's `id`
    as the value of the attachment's `guide_media_id` property.
      - Associate attachments to articles as soon as possible. For example, if you use the endpoint to
    bulk-import inline images, only signed-in end users can see the images; anonymous users don't have
    permission to view unassociated images. Also, from time to time, we purge old article attachments
    not associated to any article. To ensure you don't lose an uploaded file, associate it to an
    article.
    #### Allowed for

      * Agents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArticleAttachmentResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ArticleAttachmentResponse]:
    """Create Unassociated Attachment

     You can use this endpoint for bulk imports. It lets you upload a file without associating it
    to an article until later. See [Associate Attachments in Bulk to Article](/api-
    reference/help_center/help-center-api/articles#associate-attachments-in-bulk-to-article).

     If you plan on adding attachments to article translations, import a separate article attachment for
    each translation and set the locale in advance. For more information on translation attachments, see
    [Create Article Attachment](/api-reference/help_center/help-center-api/article_attachments/#create-
    article-attachment).

    *Notes:*

      - Zendesk recommends to first create a [Guide media object](/api-reference/help_center/help-
    center-api/guide_medias/#create-guide-media) and then [create an article attachment](/api-
    reference/help_center/help-center-api/article_attachments/#create-article-attachment) with the value
    of the media object's `id`. When creating the attachment, use the value of the media object's `id`
    as the value of the attachment's `guide_media_id` property.
      - Associate attachments to articles as soon as possible. For example, if you use the endpoint to
    bulk-import inline images, only signed-in end users can see the images; anonymous users don't have
    permission to view unassociated images. Also, from time to time, we purge old article attachments
    not associated to any article. To ensure you don't lose an uploaded file, associate it to an
    article.
    #### Allowed for

      * Agents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArticleAttachmentResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
