from pydantic import BaseModel

class ItemDTO(BaseModel):
    id: str
    name: str
    description: str
