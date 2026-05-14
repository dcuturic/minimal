from fastapi import APIRouter

router = APIRouter()

@router.post("/api/minimal-solutions/seo_merger")
async def seo_merger_api():
    return {"status": "success", "message": "SEO Merger API initialized"}
