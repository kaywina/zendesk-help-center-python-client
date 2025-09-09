from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generative_answers_help_center_response import GenerativeAnswersHelpCenterResponse
from ...models.generative_answers_help_center_response_400 import GenerativeAnswersHelpCenterResponse400
from ...models.generative_answers_help_center_response_403 import GenerativeAnswersHelpCenterResponse403
from ...types import UNSET, Response


def _get_kwargs(
    *,
    contents_data: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["contents_data"] = contents_data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/hc/api/internal/generative_answers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GenerativeAnswersHelpCenterResponse,
        GenerativeAnswersHelpCenterResponse400,
        GenerativeAnswersHelpCenterResponse403,
    ]
]:
    if response.status_code == 200:
        response_200 = GenerativeAnswersHelpCenterResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GenerativeAnswersHelpCenterResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = GenerativeAnswersHelpCenterResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GenerativeAnswersHelpCenterResponse,
        GenerativeAnswersHelpCenterResponse400,
        GenerativeAnswersHelpCenterResponse403,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    contents_data: str,
) -> Response[
    Union[
        GenerativeAnswersHelpCenterResponse,
        GenerativeAnswersHelpCenterResponse400,
        GenerativeAnswersHelpCenterResponse403,
    ]
]:
    """Generates answer for the provided query and contents

     Generates an answer for the provided query and contents. The contents can be a list of articles,
    community posts, or external contents.
    The response will include the generated answer and the source of the information used to generate
    it.

    Args:
        contents_data (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GenerativeAnswersHelpCenterResponse, GenerativeAnswersHelpCenterResponse400, GenerativeAnswersHelpCenterResponse403]]
    """

    kwargs = _get_kwargs(
        contents_data=contents_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    contents_data: str,
) -> Optional[
    Union[
        GenerativeAnswersHelpCenterResponse,
        GenerativeAnswersHelpCenterResponse400,
        GenerativeAnswersHelpCenterResponse403,
    ]
]:
    """Generates answer for the provided query and contents

     Generates an answer for the provided query and contents. The contents can be a list of articles,
    community posts, or external contents.
    The response will include the generated answer and the source of the information used to generate
    it.

    Args:
        contents_data (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GenerativeAnswersHelpCenterResponse, GenerativeAnswersHelpCenterResponse400, GenerativeAnswersHelpCenterResponse403]
    """

    return sync_detailed(
        client=client,
        contents_data=contents_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    contents_data: str,
) -> Response[
    Union[
        GenerativeAnswersHelpCenterResponse,
        GenerativeAnswersHelpCenterResponse400,
        GenerativeAnswersHelpCenterResponse403,
    ]
]:
    """Generates answer for the provided query and contents

     Generates an answer for the provided query and contents. The contents can be a list of articles,
    community posts, or external contents.
    The response will include the generated answer and the source of the information used to generate
    it.

    Args:
        contents_data (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GenerativeAnswersHelpCenterResponse, GenerativeAnswersHelpCenterResponse400, GenerativeAnswersHelpCenterResponse403]]
    """

    kwargs = _get_kwargs(
        contents_data=contents_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    contents_data: str,
) -> Optional[
    Union[
        GenerativeAnswersHelpCenterResponse,
        GenerativeAnswersHelpCenterResponse400,
        GenerativeAnswersHelpCenterResponse403,
    ]
]:
    """Generates answer for the provided query and contents

     Generates an answer for the provided query and contents. The contents can be a list of articles,
    community posts, or external contents.
    The response will include the generated answer and the source of the information used to generate
    it.

    Args:
        contents_data (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GenerativeAnswersHelpCenterResponse, GenerativeAnswersHelpCenterResponse400, GenerativeAnswersHelpCenterResponse403]
    """

    return (
        await asyncio_detailed(
            client=client,
            contents_data=contents_data,
        )
    ).parsed
