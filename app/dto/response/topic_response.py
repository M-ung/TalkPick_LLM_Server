from pydantic import BaseModel
from typing import List

class TopicResponse(BaseModel):
    id: int
    title: str
    detail: str
    thumbnail: str
    icon: str
    category_id: int

    class Config:
        from_attributes = True

class TopicListResponse(BaseModel):
    topics: List[TopicResponse]
    
    class Config:
        from_attributes = True 