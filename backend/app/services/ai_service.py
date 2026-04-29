"""Mock AI scoring service for MVP.

Provides `score_translation` which returns a mocked breakdown and overall score.
Replace with OpenAI integration in Phase 3.
"""
from typing import Dict


async def score_translation(transcript: str, expected_meaning: str) -> Dict:
    """Return a mocked scoring breakdown and overall score."""
    # Very simple mock: if transcript is non-empty, return nominal scores.
    if not transcript:
        return {"score": 0, "breakdown": {"meaning": 0, "grammar": 0, "fluency": 0, "vocabulary": 0}}

    breakdown = {"meaning": 85, "grammar": 78, "fluency": 80, "vocabulary": 76}
    overall = int(sum(breakdown.values()) / len(breakdown))
    return {"score": overall, "breakdown": breakdown}

