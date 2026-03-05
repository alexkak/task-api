from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class TaskCreate(BaseModel):
    title: str 
    description: str | None = None
    priority: int = 1

    @field_validator("title")
    @classmethod
    def title_must_not_be_empty(cls, title: str) -> str:
        if len(title) == 0 or title.isspace():
            raise ValueError("Title must not be empty")
        return title
    
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    priority: int
    created_at: datetime

