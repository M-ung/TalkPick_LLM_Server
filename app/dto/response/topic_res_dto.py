from typing import List
from pydantic import BaseModel, conint

class RandomTopic(BaseModel):
    order: int
    topic_id: conint(ge=0, strict=True) 
    category: str
    image_url: str
    keyword: str
    thumbnail: str
    icon: str

class TopicResDTO(BaseModel):
    topics: List[RandomTopic] 