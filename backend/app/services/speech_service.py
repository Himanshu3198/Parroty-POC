"""Mock speech service for MVP.

This module provides a placeholder `speech_to_text` function. Replace with real
integration (OpenAI / Whisper / other) later.
"""

from typing import Optional


async def speech_to_text(audio_bytes: bytes) -> str:
    """Mock conversion: returns a fixed string for now.

    In production this should call a speech-to-text provider and return the transcript.
    """
    # TODO: integrate with real STT provider
    return "(mock transcript)"

