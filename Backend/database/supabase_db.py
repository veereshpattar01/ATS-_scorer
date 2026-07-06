import logging
import httpx
from typing import Dict

from Backend.core.config import (
    SUPABASE_URL,
    SUPABASE_KEY,
)


logger = logging.getLogger('ats_resume_scorer')


def _get_headers():
    if not SUPABASE_URL or not SUPABASE_KEY:
        return None
    return {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "prefer": "return=representation",
    }


async def save_analysis(user_id: str, filename: str, analysis_result: Dict) -> str:
    url = f"{SUPABASE_URL.rstrip('/')}/rest/v1/analyses"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=analysis_result, headers=_get_headers())
            response.raise_for_status()
            data = response.json()
            if data and len(data) > 0:
                inserted_id = str(data[0].get('id'))
                logger.info(f"Analysis result saved successfully with ID: {inserted_id}")
                return inserted_id
            return None
    except Exception as exc:
        logger.error(f"Failed to save analysis to supabase: {exc}")
        return None
