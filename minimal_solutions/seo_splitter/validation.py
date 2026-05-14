from pydantic import BaseModel

class SEOSplitterRequest(BaseModel):
    topic: str
    target: str
    options: dict = {}
