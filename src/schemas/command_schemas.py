from pydantic import BaseModel

class CreateItemCommand(BaseModel):
    name: str
    description: str
