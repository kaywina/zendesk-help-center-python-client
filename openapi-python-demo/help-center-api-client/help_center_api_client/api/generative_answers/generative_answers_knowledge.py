from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generative_answers_knowledge_request import GenerativeAnswersKnowledgeRequest
from ...models.generative_answers_knowledge_response import GenerativeAnswersKnowledgeResponse
from ...models.generative_answers_knowledge_response_400 import GenerativeAnswersKnowledgeResponse400
from ...models.generative_answers_knowledge_response_403 import GenerativeAnswersKnowledgeResponse403
from ...types import Response


def _get_kwargs(
    *,
    body: GenerativeAnswersKnowledgeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/hc/api/internal/generative_answers_knowledge",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GenerativeAnswersKnowledgeResponse, GenerativeAnswersKnowledgeResponse400, GenerativeAnswersKnowledgeResponse403
    ]
]:
    if response.status_code == 200:
        response_200 = GenerativeAnswersKnowledgeResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GenerativeAnswersKnowledgeResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = GenerativeAnswersKnowledgeResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GenerativeAnswersKnowledgeResponse, GenerativeAnswersKnowledgeResponse400, GenerativeAnswersKnowledgeResponse403
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
    body: GenerativeAnswersKnowledgeRequest,
) -> Response[
    Union[
        GenerativeAnswersKnowledgeResponse, GenerativeAnswersKnowledgeResponse400, GenerativeAnswersKnowledgeResponse403
    ]
]:
    """Generates answer for the provided query and contents

     Generates an answer for the provided query and contents. The contents can be a list of articles,
    community posts, or external contents.
    The response will include the generated answer and the source of the information used to generate
    it.

    Args:
        body (GenerativeAnswersKnowledgeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GenerativeAnswersKnowledgeResponse, GenerativeAnswersKnowledgeResponse400, GenerativeAnswersKnowledgeResponse403]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GenerativeAnswersKnowledgeRequest,
) -> Optional[
    Union[
        GenerativeAnswersKnowledgeResponse, GenerativeAnswersKnowledgeResponse400, GenerativeAnswersKnowledgeResponse403
    ]
]:
    """Generates answer for the provided query and contents

     Generates an answer for the provided query and contents. The contents can be a list of articles,
    community posts, or external contents.
    The response will include the generated answer and the source of the information used to generate
    it.

    Args:
        body (GenerativeAnswersKnowledgeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GenerativeAnswersKnowledgeResponse, GenerativeAnswersKnowledgeResponse400, GenerativeAnswersKnowledgeResponse403]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GenerativeAnswersKnowledgeRequest,
) -> Response[
    Union[
        GenerativeAnswersKnowledgeResponse, GenerativeAnswersKnowledgeResponse400, GenerativeAnswersKnowledgeResponse403
    ]
]:
    """Generates answer for the provided query and contents

     Generates an answer for the provided query and contents. The contents can be a list of articles,
    community posts, or external contents.
    The response will include the generated answer and the source of the information used to generate
    it.

    Args:
        body (GenerativeAnswersKnowledgeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GenerativeAnswersKnowledgeResponse, GenerativeAnswersKnowledgeResponse400, GenerativeAnswersKnowledgeResponse403]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GenerativeAnswersKnowledgeRequest,
) -> Optional[
    Union[
        GenerativeAnswersKnowledgeResponse, GenerativeAnswersKnowledgeResponse400, GenerativeAnswersKnowledgeResponse403
    ]
]:
    """Generates answer for the provided query and contents

     Generates an answer for the provided query and contents. The contents can be a list of articles,
    community posts, or external contents.
    The response will include the generated answer and the source of the information used to generate
    it.

    Args:
        body (GenerativeAnswersKnowledgeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GenerativeAnswersKnowledgeResponse, GenerativeAnswersKnowledgeResponse400, GenerativeAnswersKnowledgeResponse403]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
