# validation_minecraft_validator.py
"""
Validation logic for Minecraft Validator.
"""
from pydantic import BaseModel

class MinecraftValidatorRequest(BaseModel):
    input_text: str
    mode: str = "default"
    options: dict = {}
