from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TranslateQuestion(BaseModel):
    id: int
    hindi_text: str
    difficulty: Optional[str] = "easy"
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

