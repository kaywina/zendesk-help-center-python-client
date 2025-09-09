from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.request_user_image_upload_response import RequestUserImageUploadResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/guide/user_images/uploads",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RequestUserImageUploadResponse]:
    if response.status_code == 200:
        response_200 = RequestUserImageUploadResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RequestUserImageUploadResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[RequestUserImageUploadResponse]:
    r""" Create Image Upload URL and Token

     Returns an upload URL and token. Use the upload URL in a PUT request to upload the image to the help
    center. See [Uploading the image with the upload URL](#uploading-the-image-with-the-upload-url)
    below.

    After uploading the image, use the image token to create the image path. See [Create Image
    Path](#create-image-path).

    #### Uploading the image with the upload URL

    The endpoint returns an object with the `url` and `headers` properties:

    ```json
    \"headers\": {
      \"Content-Disposition\": \"attachment; filename=\\"01GC9JEN2X052BAKW905PH9C36.jpeg\\"\",
      \"Content-Type\": \"image/jpeg\",
      \"X-Amz-Server-Side-Encryption\": \"AES256\"
    },
    ...
    \"url\": \"https://aus-uploaded-assets-
    production.s3-accelerate.amazonaws.com/20/13633840/01GC9JEN2X052BAKW905PH9C36?Content-
    Type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ACCESS_KEY%2F20220906%2Fus-
    east-1%2Fs3%2Faws4_request&X-Amz-Date=20220906T141448Z&X-Amz-Expires=3600&X-Amz-
    Signature=476f8f09a97cae0bb582716d54dc58cdfbc754c5e20a2c492515d7ffce954971&X-Amz-
    SignedHeaders=content-disposition%3Bhost%3Bx-amz-server-side-encryption&x-amz-server-side-
    encryption=AES256\"
    ```

    To upload the image, make a PUT request to the URL and with the specified headers. Agents, end
    users, or anonymous users can make the request. The maximum file size is 2MB.

    The following curl example uploads the image:

    ```sh
    curl -L -X PUT 'https://aus-uploaded-assets-
    production.s3-accelerate.amazonaws.com/20/13633840/01GC9JEN2X052BAKW905PH9C36?Content-
    Type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ACCESS_KEY%2F20220906%2Fus-
    east-1%2Fs3%2Faws4_request&X-Amz-Date=20220906T141448Z&X-Amz-Expires=3600&X-Amz-
    Signature=476f8f09a97cae0bb582716d54dc58cdfbc754c5e20a2c492515d7ffce954971&X-Amz-
    SignedHeaders=content-disposition%3Bhost%3Bx-amz-server-side-encryption&x-amz-server-side-
    encryption=AES256' \
      -H 'Content-Disposition: attachment; filename=\"01GC9JEN2X052BAKW905PH9C36.jpeg\"' \
      -H 'Content-Type: image/jpeg' \
      -H 'X-Amz-Server-Side-Encryption: AES256' \
      --data-binary \"@{file}\"
    ```

    A successful response will return:

    ```
    Status 200 OK
    ```

    #### Request Body Format
    The request body of `POST /api/v2/guide/user_images/uploads` must be a JSON object with the
    following properties:

    | Name         | Type   | Mandatory | Description |
    | ------------ | ------ | --------- | ----------- |
    | content_type | string | true      | The content type of the file to upload |
    | file_size    | number | true      | Size of the file in bytes. Max size is 2000000 (2MB). |

    #### Allowed for

    * Anonymous users

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequestUserImageUploadResponse]
     """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[RequestUserImageUploadResponse]:
    r""" Create Image Upload URL and Token

     Returns an upload URL and token. Use the upload URL in a PUT request to upload the image to the help
    center. See [Uploading the image with the upload URL](#uploading-the-image-with-the-upload-url)
    below.

    After uploading the image, use the image token to create the image path. See [Create Image
    Path](#create-image-path).

    #### Uploading the image with the upload URL

    The endpoint returns an object with the `url` and `headers` properties:

    ```json
    \"headers\": {
      \"Content-Disposition\": \"attachment; filename=\\"01GC9JEN2X052BAKW905PH9C36.jpeg\\"\",
      \"Content-Type\": \"image/jpeg\",
      \"X-Amz-Server-Side-Encryption\": \"AES256\"
    },
    ...
    \"url\": \"https://aus-uploaded-assets-
    production.s3-accelerate.amazonaws.com/20/13633840/01GC9JEN2X052BAKW905PH9C36?Content-
    Type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ACCESS_KEY%2F20220906%2Fus-
    east-1%2Fs3%2Faws4_request&X-Amz-Date=20220906T141448Z&X-Amz-Expires=3600&X-Amz-
    Signature=476f8f09a97cae0bb582716d54dc58cdfbc754c5e20a2c492515d7ffce954971&X-Amz-
    SignedHeaders=content-disposition%3Bhost%3Bx-amz-server-side-encryption&x-amz-server-side-
    encryption=AES256\"
    ```

    To upload the image, make a PUT request to the URL and with the specified headers. Agents, end
    users, or anonymous users can make the request. The maximum file size is 2MB.

    The following curl example uploads the image:

    ```sh
    curl -L -X PUT 'https://aus-uploaded-assets-
    production.s3-accelerate.amazonaws.com/20/13633840/01GC9JEN2X052BAKW905PH9C36?Content-
    Type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ACCESS_KEY%2F20220906%2Fus-
    east-1%2Fs3%2Faws4_request&X-Amz-Date=20220906T141448Z&X-Amz-Expires=3600&X-Amz-
    Signature=476f8f09a97cae0bb582716d54dc58cdfbc754c5e20a2c492515d7ffce954971&X-Amz-
    SignedHeaders=content-disposition%3Bhost%3Bx-amz-server-side-encryption&x-amz-server-side-
    encryption=AES256' \
      -H 'Content-Disposition: attachment; filename=\"01GC9JEN2X052BAKW905PH9C36.jpeg\"' \
      -H 'Content-Type: image/jpeg' \
      -H 'X-Amz-Server-Side-Encryption: AES256' \
      --data-binary \"@{file}\"
    ```

    A successful response will return:

    ```
    Status 200 OK
    ```

    #### Request Body Format
    The request body of `POST /api/v2/guide/user_images/uploads` must be a JSON object with the
    following properties:

    | Name         | Type   | Mandatory | Description |
    | ------------ | ------ | --------- | ----------- |
    | content_type | string | true      | The content type of the file to upload |
    | file_size    | number | true      | Size of the file in bytes. Max size is 2000000 (2MB). |

    #### Allowed for

    * Anonymous users

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequestUserImageUploadResponse
     """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[RequestUserImageUploadResponse]:
    r""" Create Image Upload URL and Token

     Returns an upload URL and token. Use the upload URL in a PUT request to upload the image to the help
    center. See [Uploading the image with the upload URL](#uploading-the-image-with-the-upload-url)
    below.

    After uploading the image, use the image token to create the image path. See [Create Image
    Path](#create-image-path).

    #### Uploading the image with the upload URL

    The endpoint returns an object with the `url` and `headers` properties:

    ```json
    \"headers\": {
      \"Content-Disposition\": \"attachment; filename=\\"01GC9JEN2X052BAKW905PH9C36.jpeg\\"\",
      \"Content-Type\": \"image/jpeg\",
      \"X-Amz-Server-Side-Encryption\": \"AES256\"
    },
    ...
    \"url\": \"https://aus-uploaded-assets-
    production.s3-accelerate.amazonaws.com/20/13633840/01GC9JEN2X052BAKW905PH9C36?Content-
    Type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ACCESS_KEY%2F20220906%2Fus-
    east-1%2Fs3%2Faws4_request&X-Amz-Date=20220906T141448Z&X-Amz-Expires=3600&X-Amz-
    Signature=476f8f09a97cae0bb582716d54dc58cdfbc754c5e20a2c492515d7ffce954971&X-Amz-
    SignedHeaders=content-disposition%3Bhost%3Bx-amz-server-side-encryption&x-amz-server-side-
    encryption=AES256\"
    ```

    To upload the image, make a PUT request to the URL and with the specified headers. Agents, end
    users, or anonymous users can make the request. The maximum file size is 2MB.

    The following curl example uploads the image:

    ```sh
    curl -L -X PUT 'https://aus-uploaded-assets-
    production.s3-accelerate.amazonaws.com/20/13633840/01GC9JEN2X052BAKW905PH9C36?Content-
    Type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ACCESS_KEY%2F20220906%2Fus-
    east-1%2Fs3%2Faws4_request&X-Amz-Date=20220906T141448Z&X-Amz-Expires=3600&X-Amz-
    Signature=476f8f09a97cae0bb582716d54dc58cdfbc754c5e20a2c492515d7ffce954971&X-Amz-
    SignedHeaders=content-disposition%3Bhost%3Bx-amz-server-side-encryption&x-amz-server-side-
    encryption=AES256' \
      -H 'Content-Disposition: attachment; filename=\"01GC9JEN2X052BAKW905PH9C36.jpeg\"' \
      -H 'Content-Type: image/jpeg' \
      -H 'X-Amz-Server-Side-Encryption: AES256' \
      --data-binary \"@{file}\"
    ```

    A successful response will return:

    ```
    Status 200 OK
    ```

    #### Request Body Format
    The request body of `POST /api/v2/guide/user_images/uploads` must be a JSON object with the
    following properties:

    | Name         | Type   | Mandatory | Description |
    | ------------ | ------ | --------- | ----------- |
    | content_type | string | true      | The content type of the file to upload |
    | file_size    | number | true      | Size of the file in bytes. Max size is 2000000 (2MB). |

    #### Allowed for

    * Anonymous users

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequestUserImageUploadResponse]
     """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[RequestUserImageUploadResponse]:
    r""" Create Image Upload URL and Token

     Returns an upload URL and token. Use the upload URL in a PUT request to upload the image to the help
    center. See [Uploading the image with the upload URL](#uploading-the-image-with-the-upload-url)
    below.

    After uploading the image, use the image token to create the image path. See [Create Image
    Path](#create-image-path).

    #### Uploading the image with the upload URL

    The endpoint returns an object with the `url` and `headers` properties:

    ```json
    \"headers\": {
      \"Content-Disposition\": \"attachment; filename=\\"01GC9JEN2X052BAKW905PH9C36.jpeg\\"\",
      \"Content-Type\": \"image/jpeg\",
      \"X-Amz-Server-Side-Encryption\": \"AES256\"
    },
    ...
    \"url\": \"https://aus-uploaded-assets-
    production.s3-accelerate.amazonaws.com/20/13633840/01GC9JEN2X052BAKW905PH9C36?Content-
    Type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ACCESS_KEY%2F20220906%2Fus-
    east-1%2Fs3%2Faws4_request&X-Amz-Date=20220906T141448Z&X-Amz-Expires=3600&X-Amz-
    Signature=476f8f09a97cae0bb582716d54dc58cdfbc754c5e20a2c492515d7ffce954971&X-Amz-
    SignedHeaders=content-disposition%3Bhost%3Bx-amz-server-side-encryption&x-amz-server-side-
    encryption=AES256\"
    ```

    To upload the image, make a PUT request to the URL and with the specified headers. Agents, end
    users, or anonymous users can make the request. The maximum file size is 2MB.

    The following curl example uploads the image:

    ```sh
    curl -L -X PUT 'https://aus-uploaded-assets-
    production.s3-accelerate.amazonaws.com/20/13633840/01GC9JEN2X052BAKW905PH9C36?Content-
    Type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ACCESS_KEY%2F20220906%2Fus-
    east-1%2Fs3%2Faws4_request&X-Amz-Date=20220906T141448Z&X-Amz-Expires=3600&X-Amz-
    Signature=476f8f09a97cae0bb582716d54dc58cdfbc754c5e20a2c492515d7ffce954971&X-Amz-
    SignedHeaders=content-disposition%3Bhost%3Bx-amz-server-side-encryption&x-amz-server-side-
    encryption=AES256' \
      -H 'Content-Disposition: attachment; filename=\"01GC9JEN2X052BAKW905PH9C36.jpeg\"' \
      -H 'Content-Type: image/jpeg' \
      -H 'X-Amz-Server-Side-Encryption: AES256' \
      --data-binary \"@{file}\"
    ```

    A successful response will return:

    ```
    Status 200 OK
    ```

    #### Request Body Format
    The request body of `POST /api/v2/guide/user_images/uploads` must be a JSON object with the
    following properties:

    | Name         | Type   | Mandatory | Description |
    | ------------ | ------ | --------- | ----------- |
    | content_type | string | true      | The content type of the file to upload |
    | file_size    | number | true      | Size of the file in bytes. Max size is 2000000 (2MB). |

    #### Allowed for

    * Anonymous users

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequestUserImageUploadResponse
     """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
