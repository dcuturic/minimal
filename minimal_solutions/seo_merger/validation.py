from pydantic import BaseModel

class SEOMergerRequest(BaseModel):
    topic: str
    target: str
    options: dict = {}
