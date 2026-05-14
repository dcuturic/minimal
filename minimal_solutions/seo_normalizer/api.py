from fastapi import APIRouter

router = APIRouter()

@router.post("/api/minimal-solutions/seo_normalizer")
async def seo_normalizer_api():
    return {"status": "success", "message": "SEO Normalizer API initialized"}
