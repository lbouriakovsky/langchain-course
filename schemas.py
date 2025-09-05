from typing import List

from pydantic import BaseModel, Field


class SourceDocument(BaseModel):
    """Schema for a source used by the agent"""

    ur: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for the agent response"""

    answer: str = Field(description="The agents anser to the query")

    sources: List[SourceDocument] = Field(
        default_factory=list,
        description="List of sources used by the agent to generate the answer",
    )
