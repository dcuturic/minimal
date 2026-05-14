from pydantic import BaseModel

class SEOMaskerRequest(BaseModel):
    topic: str
    target: str
    options: dict = {}
