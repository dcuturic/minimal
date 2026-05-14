from pydantic import BaseModel

class MinecraftPreviewRequest(BaseModel):
    input_text: str
