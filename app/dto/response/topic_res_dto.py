from typing import List
from pydantic import BaseModel, conint

class TopicResDTO(BaseModel):
    topic_ids: List[conint(ge=0, strict=True)] 