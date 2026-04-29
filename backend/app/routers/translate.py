from random import choice
from typing import List

from fastapi import APIRouter, HTTPException

from backend.app.schemas.translate import TranslateQuestion

router = APIRouter()

# In-memory seed of Hindi sentences for the MVP. Replace with DB calls later.
SEED_QUESTIONS: List[TranslateQuestion] = [
    TranslateQuestion(id=1, hindi_text="मुझे कल जल्दी उठना है", difficulty="easy"),
    TranslateQuestion(id=2, hindi_text="वह बाजार जा रहा है", difficulty="easy"),
    TranslateQuestion(id=3, hindi_text="आज मौसम बहुत अच्छा है", difficulty="easy"),
    TranslateQuestion(id=4, hindi_text="मैं किताब पढ़ रहा हूँ", difficulty="medium"),
]


@router.get("/question", response_model=TranslateQuestion)
async def get_random_question():
    """Return one random Hindi sentence for translation practice."""
    if not SEED_QUESTIONS:
        raise HTTPException(status_code=404, detail="No questions available")
    return choice(SEED_QUESTIONS)

