# backend/models.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from database import Base

class Feedback(Base):
    __tablename__ = "feedback_logs"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    sentiment_label = Column(String, nullable=True)
    analysis_result = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())