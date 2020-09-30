from typing import Optional

import pydantic

ProcessDefinitionId = str


class ProcessDefinition(pydantic.BaseModel):
    id: ProcessDefinitionId
    key: str
    category: str
    description: Optional[str]
    name: Optional[str]
    version: int
    resource: str
    deploymentId: str
    diagram: Optional[str]
    suspended: bool
    tenantId: Optional[str]
    versionTag: Optional[str]
    historyTimeToLive: Optional[float]
    startableInTasklist: bool
