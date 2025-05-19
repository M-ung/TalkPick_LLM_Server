from typing import List, Optional
from pydantic import BaseModel, conint
from ...domain.member.type.gender import Gender
from ...domain.member.type.mbti import MBTI
from ...domain.topic.type.keyword import Keyword
from ...domain.topic.type.category_group import CategoryGroup

class TopicReqDTO(BaseModel):
    class PreviousTopicData(BaseModel):
        id: conint(ge=0, strict=True) 
        title: str
        detail: str
        keyword: Keyword
        category_group: CategoryGroup
        category: str

    class TopicData(BaseModel):
        topic_id: conint(ge=0, strict=True) 
        topic_title: str
        topic_detail: str
        topic_thumbnail: Optional[str]
        topic_icon: Optional[str]
        category_title: str
        category_description: str
        category_image_url: Optional[str]
        category_group: CategoryGroup
        keyword: Keyword
        
        # MBTI 통계
        e_count: int
        i_count: int
        s_count: int
        n_count: int
        f_count: int
        t_count: int
        j_count: int
        p_count: int
        
        # 연령대 통계
        teen_count: int
        twenties_count: int
        thirties_count: int
        forties_count: int
        fifties_count: int
        
        # 성별 통계
        male_count: int
        female_count: int

    mbti: MBTI
    gender: Gender
    age: int
    previous_topics: List[PreviousTopicData] = [] 
    available_topics: List[TopicData]  