from fastapi import APIRouter

router = APIRouter()

@router.post("/api/minimal-solutions/minecraft_preview")
async def minecraft_preview_endpoint(data: dict):
    return {"status": "success", "data": data}
