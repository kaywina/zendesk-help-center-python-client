from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_user_image_response import CreateUserImageResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/guide/user_images",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateUserImageResponse]:
    if response.status_code == 201:
        response_201 = CreateUserImageResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateUserImageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CreateUserImageResponse]:
    """Create Image Path

     Returns the image path that you can use to display the image in a community post.

    You should only use this endpoint after uploading the image. See [Uploading the image with the
    upload URL](#uploading-the-image-with-the-upload-url).

    #### Request Body Format
    The request body must be a JSON object with the following properties:

    | Name         | Type   | Mandatory | Description |
    | ------------ | ------ | --------- | ----------- |
    | token        | string | true      | The image token. See [Create Image Upload URL and
    Token](#create-image-upload-url-and-token) |
    | brand_id     | string | true      | The ID of the brand where this image was uploaded |

    #### Allowed for

    * Anonymous users

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUserImageResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CreateUserImageResponse]:
    """Create Image Path

     Returns the image path that you can use to display the image in a community post.

    You should only use this endpoint after uploading the image. See [Uploading the image with the
    upload URL](#uploading-the-image-with-the-upload-url).

    #### Request Body Format
    The request body must be a JSON object with the following properties:

    | Name         | Type   | Mandatory | Description |
    | ------------ | ------ | --------- | ----------- |
    | token        | string | true      | The image token. See [Create Image Upload URL and
    Token](#create-image-upload-url-and-token) |
    | brand_id     | string | true      | The ID of the brand where this image was uploaded |

    #### Allowed for

    * Anonymous users

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateUserImageResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CreateUserImageResponse]:
    """Create Image Path

     Returns the image path that you can use to display the image in a community post.

    You should only use this endpoint after uploading the image. See [Uploading the image with the
    upload URL](#uploading-the-image-with-the-upload-url).

    #### Request Body Format
    The request body must be a JSON object with the following properties:

    | Name         | Type   | Mandatory | Description |
    | ------------ | ------ | --------- | ----------- |
    | token        | string | true      | The image token. See [Create Image Upload URL and
    Token](#create-image-upload-url-and-token) |
    | brand_id     | string | true      | The ID of the brand where this image was uploaded |

    #### Allowed for

    * Anonymous users

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUserImageResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CreateUserImageResponse]:
    """Create Image Path

     Returns the image path that you can use to display the image in a community post.

    You should only use this endpoint after uploading the image. See [Uploading the image with the
    upload URL](#uploading-the-image-with-the-upload-url).

    #### Request Body Format
    The request body must be a JSON object with the following properties:

    | Name         | Type   | Mandatory | Description |
    | ------------ | ------ | --------- | ----------- |
    | token        | string | true      | The image token. See [Create Image Upload URL and
    Token](#create-image-upload-url-and-token) |
    | brand_id     | string | true      | The ID of the brand where this image was uploaded |

    #### Allowed for

    * Anonymous users

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateUserImageResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
