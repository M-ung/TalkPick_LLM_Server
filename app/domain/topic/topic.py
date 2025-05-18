from sqlalchemy import Column, Integer, String, Enum
from ....config.database import Base
from ...base_time import BaseTime
from ..type.talk_pick_status import TalkPickStatus

class Topic(Base, BaseTime):
    __tablename__ = "topic"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    detail = Column(String)
    thumbnail = Column(String)
    icon = Column(String)
    category_id = Column(Integer)
    status = Column(Enum(TalkPickStatus))
    created_by_id = Column(Integer) 