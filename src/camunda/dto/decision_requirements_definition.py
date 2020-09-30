import pydantic

DecisionRequirementsDefinitionId = str


class DecisionRequirementsDefinition(pydantic.BaseModel):
    id: DecisionRequirementsDefinitionId
    key: str
    category: str
    name: str
    version: float
    resource: str
    deploymentId: str
    tenantId: str
