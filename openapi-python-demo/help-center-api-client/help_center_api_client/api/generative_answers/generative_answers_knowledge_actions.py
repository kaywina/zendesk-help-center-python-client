from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generative_answers_knowledge_actions_request import GenerativeAnswersKnowledgeActionsRequest
from ...models.generative_answers_knowledge_actions_response_400 import GenerativeAnswersKnowledgeActionsResponse400
from ...models.generative_answers_knowledge_actions_response_403 import GenerativeAnswersKnowledgeActionsResponse403
from ...types import Response


def _get_kwargs(
    *,
    body: GenerativeAnswersKnowledgeActionsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/hc/api/internal/generative_answers_knowledge/actions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GenerativeAnswersKnowledgeActionsResponse400, GenerativeAnswersKnowledgeActionsResponse403]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = GenerativeAnswersKnowledgeActionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = GenerativeAnswersKnowledgeActionsResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GenerativeAnswersKnowledgeActionsResponse400, GenerativeAnswersKnowledgeActionsResponse403]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GenerativeAnswersKnowledgeActionsRequest,
) -> Response[Union[Any, GenerativeAnswersKnowledgeActionsResponse400, GenerativeAnswersKnowledgeActionsResponse403]]:
    """Submits an action for a generated answer

     Submits an action for a generated answer. This action indicates that user has perfomed further
    actions on the generated answer.

    Args:
        body (GenerativeAnswersKnowledgeActionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GenerativeAnswersKnowledgeActionsResponse400, GenerativeAnswersKnowledgeActionsResponse403]]
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
    body: GenerativeAnswersKnowledgeActionsRequest,
) -> Optional[Union[Any, GenerativeAnswersKnowledgeActionsResponse400, GenerativeAnswersKnowledgeActionsResponse403]]:
    """Submits an action for a generated answer

     Submits an action for a generated answer. This action indicates that user has perfomed further
    actions on the generated answer.

    Args:
        body (GenerativeAnswersKnowledgeActionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GenerativeAnswersKnowledgeActionsResponse400, GenerativeAnswersKnowledgeActionsResponse403]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GenerativeAnswersKnowledgeActionsRequest,
) -> Response[Union[Any, GenerativeAnswersKnowledgeActionsResponse400, GenerativeAnswersKnowledgeActionsResponse403]]:
    """Submits an action for a generated answer

     Submits an action for a generated answer. This action indicates that user has perfomed further
    actions on the generated answer.

    Args:
        body (GenerativeAnswersKnowledgeActionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GenerativeAnswersKnowledgeActionsResponse400, GenerativeAnswersKnowledgeActionsResponse403]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GenerativeAnswersKnowledgeActionsRequest,
) -> Optional[Union[Any, GenerativeAnswersKnowledgeActionsResponse400, GenerativeAnswersKnowledgeActionsResponse403]]:
    """Submits an action for a generated answer

     Submits an action for a generated answer. This action indicates that user has perfomed further
    actions on the generated answer.

    Args:
        body (GenerativeAnswersKnowledgeActionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GenerativeAnswersKnowledgeActionsResponse400, GenerativeAnswersKnowledgeActionsResponse403]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
