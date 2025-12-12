# backend/schemas.py
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class FeedbackInput(BaseModel):
    content: str

class FeedbackResponse(BaseModel):
    id: int
    content: str
    sentiment_label: Optional[str] = None
    analysis_result: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)