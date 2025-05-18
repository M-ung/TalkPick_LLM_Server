from pydantic import BaseModel
from typing import Optional

class TopicRequest(BaseModel):
    member_id: int
    random_id: int
    mbti: Optional[str]
    age: Optional[int]
    gender: Optional[str]

    class Config:
        from_attributes = True 