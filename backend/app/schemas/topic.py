from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Topic(BaseModel):
    id: int
    topic: str
    difficulty: Optional[str] = "easy"
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

