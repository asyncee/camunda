import pydantic

CaseDefinitionId = str


class CaseDefinition(pydantic.BaseModel):
    id: CaseDefinitionId
    key: str
    category: str
    name: str
    version: float
    resource: str
    deploymentId: str
    tenantId: str
    historyTimeToLive: float
