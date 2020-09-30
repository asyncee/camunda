import pydantic


class DecisionDefinition(pydantic.BaseModel):
    id: str
    key: str
    category: str
    name: str
    version: float
    resource: str
    deploymentId: str
    decisionRequirementsDefinitionId: str
    decisionRequirementsDefinitionKey: str
    tenantId: str
    versionTag: str
    historyTimeToLive: float


DecisionDefinitionId = str
