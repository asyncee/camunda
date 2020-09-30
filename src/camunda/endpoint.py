from typing import Generic, Literal, Optional, Tuple, Type, TypeVar

from numbers import Number
from urllib.parse import urljoin

import httpx
import pydantic
from httpx._client import BaseClient

from . import conf

ApiRequest = TypeVar("ApiRequest", bound=pydantic.BaseModel)
ApiResponse = TypeVar("ApiResponse", bound=pydantic.BaseModel)
ApiRequestType = Type[ApiRequest]
ApiResponseType = Type[ApiResponse]


class Endpoint(Generic[ApiRequest, ApiResponse]):
    method: str
    url: str
    request: ApiRequestType
    response: ApiResponseType
    base_url: Optional[str] = None

    def __init__(
        self,
        method: Optional[str] = None,
        url: Optional[str] = None,
        request: Optional[ApiRequestType] = None,
        response: Optional[ApiResponseType] = None,
        base_url: Optional[str] = None,
    ):
        self.method = method or self.method
        self.url = url or self.url
        self.request = request or self.request
        self.response = response or self.response
        self.base_url = base_url or self.base_url

    def call(
        self, request: ApiRequest, client: Optional[httpx.Client] = None
    ) -> ApiResponse:
        client = client or httpx.Client()
        response = client.send(self.build_httpx_request(request, client))
        response.raise_for_status()
        return self.response(**response.json())

    async def call_async(
        self, request: ApiRequest, client: Optional[httpx.AsyncClient] = None
    ):
        client = client or httpx.AsyncClient()
        async with client:
            response = await client.send(self.build_httpx_request(request, client))
            response.raise_for_status()
            return self.response(**response.json())

    def build_httpx_request(
        self, request: ApiRequest, client: BaseClient
    ) -> httpx.Request:
        safe_methods = ["GET", "OPTIONS", "HEAD"]

        payload = request.dict(by_alias=True)

        if self.method.upper() in safe_methods:
            return client.build_request(self.method, self._url(), params=payload)

        files, data = self._prepare_files(payload)
        return client.build_request(self.method, self._url(), files=files, data=data)

    def _prepare_files(self, dct: dict) -> Tuple[dict, dict]:
        files, data = {}, {}
        for k, v in dct.items():
            # Two element tuple describes file in format (name, content)
            if isinstance(v, tuple) and len(v) == 2:
                files[k] = v
                continue
            elif isinstance(v, bool):
                v = str(v).lower()
            elif isinstance(v, Number):
                v = str(v)
            data[k] = v
        return files, data

    def _url(self) -> str:
        base_url = self.base_url or conf.get_api_url()
        if self.url.startswith("/"):
            url = self.url.lstrip("/")
        else:
            url = self.url
        return urljoin(base_url, url)
