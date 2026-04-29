from random import choice
from typing import List

from fastapi import APIRouter, HTTPException

from backend.app.schemas.topic import Topic

router = APIRouter()

# In-memory seed of topics for the MVP. Replace with DB calls later.
SEED_TOPICS: List[Topic] = [
    Topic(id=1, topic="Should college education be free?", difficulty="medium"),
    Topic(id=2, topic="Describe your favorite hobby.", difficulty="easy"),
    Topic(id=3, topic="What are the pros and cons of remote work?", difficulty="medium"),
]


@router.get("/random", response_model=Topic)
async def get_random_topic():
    """Return one random speaking topic."""
    if not SEED_TOPICS:
        raise HTTPException(status_code=404, detail="No topics available")
    return choice(SEED_TOPICS)

