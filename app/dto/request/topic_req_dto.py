from typing import List
from pydantic import BaseModel, conint
from ...domain.member.type.gender import Gender
from ...domain.member.type.mbti import MBTI
from ...domain.topic.type.keyword import Keyword
from ...domain.topic.type.category_group import CategoryGroup

class TopicReqDTO(BaseModel):
    class PreviousTopic(BaseModel):
        id: conint(ge=0, strict=True) 
        title: str
        detail: str
        keyword: Keyword
        category_group: CategoryGroup
        category: str

    mbti: MBTI
    gender: Gender
    age: int
    previous_topics: List[PreviousTopic] = [] 