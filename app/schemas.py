from pydantic import BaseModel

class DescriptionRequest(BaseModel):
    description: str

class GenreResponse(BaseModel):
    genre: str
    confidence: float