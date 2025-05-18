from sqlalchemy import Column, BigInteger, Integer, Enum, DateTime
from ....config.database import Base
from ..type.category_group import CategoryGroup
from ..type.keyword import Keyword

class SelectedRandomTopic(Base):
    __tablename__ = "selected_random_topic"

    id = Column(BigInteger, primary_key=True)
    member_id = Column(BigInteger)
    random_id = Column(BigInteger)
    topic_id = Column(BigInteger, nullable=True)
    category = Column(Enum(CategoryGroup))
    keyword = Column(Enum(Keyword), nullable=True)
    order = Column(Integer)
    start_at = Column(DateTime, nullable=True)
    end_at = Column(DateTime, nullable=True) 