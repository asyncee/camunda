from __future__ import annotations

from typing import Dict, List, Optional, Tuple

import datetime

import pydantic
from pydantic import Field

from camunda import endpoint
from camunda.dto.case_definition import CaseDefinition, CaseDefinitionId
from camunda.dto.decision_definition import DecisionDefinition, DecisionDefinitionId
from camunda.dto.decision_requirements_definition import (
    DecisionRequirementsDefinition,
    DecisionRequirementsDefinitionId,
)
from camunda.dto.process_definition import ProcessDefinition, ProcessDefinitionId

Filename = str


class CreateDeploymentRequest(pydantic.BaseModel):
    deployment_name: str = Field(alias="deployment-name")
    enable_duplicate_filtering: bool = Field(False, alias="enable-duplicate-filtering")
    deploy_changed_only: bool = Field(False, alias="deploy-changed-only")
    deployment_source: str = Field(alias="deployment-source")
    tenant_id: str = Field(alias="tenant-id")
    data: Tuple[Filename, bytes] = Field(alias="data")

    @classmethod
    def from_file(cls, filename: str) -> CreateDeploymentRequest:
        raise NotImplemented

    @classmethod
    def from_string(cls, filename: str, content: bytes) -> CreateDeploymentRequest:
        raise NotImplemented

    class Config:
        allow_population_by_field_name = True


class CreateDeploymentResponse(pydantic.BaseModel):
    class Link(pydantic.BaseModel):
        method: str
        href: str
        rel: str

    links: List[Link]
    id: str
    name: Optional[str]
    source: Optional[str]
    deploymentTime: datetime.datetime
    tenantId: Optional[str]
    deployedProcessDefinitions: Optional[Dict[ProcessDefinitionId, ProcessDefinition]]
    deployedCaseDefinitions: Optional[Dict[CaseDefinitionId, CaseDefinition]]
    deployedDecisionDefinitions: Optional[
        Dict[DecisionDefinitionId, DecisionDefinition]
    ]
    deployedDecisionRequirementsDefinitions: Optional[
        Dict[DecisionRequirementsDefinitionId, DecisionRequirementsDefinition]
    ]


class Endpoint(endpoint.Endpoint[CreateDeploymentRequest, CreateDeploymentResponse]):
    method = "POST"
    url = "/deployment/create"
    request = CreateDeploymentRequest
    response = CreateDeploymentResponse


def create(request: CreateDeploymentRequest, **kwargs) -> CreateDeploymentResponse:
    return Endpoint().call(request, **kwargs)


async def create_async(
    request: CreateDeploymentRequest, **kwargs
) -> CreateDeploymentResponse:
    return await Endpoint().call_async(request, **kwargs)
