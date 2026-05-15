"""
Validation logic for Minecraft Merger
"""

def validate_input(data):
    if not data:
        return False, "Input data is required."
    return True, ""
