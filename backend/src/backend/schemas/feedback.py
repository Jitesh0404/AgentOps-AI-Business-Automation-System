from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class FeedbackCreate(BaseModel):
    customer_id: UUID | None = None

    feedback_text: str = Field(min_length=1, max_length=10000)

    category: str | None = None
    sentiment: str | None = None

    rating: int | None = Field(default=None, ge=1, le=5)
    created_at: datetime

    metadata: dict = Field(default_factory=dict)


class FeedbackResponse(FeedbackCreate):
    id: UUID

    model_config = ConfigDict(from_attributes=True)
