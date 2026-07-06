from fastapi import APIRouter

router = APIRouter()


@router.get("/api/v1/health")
async def health_check():
    return {"status": "ok"}
