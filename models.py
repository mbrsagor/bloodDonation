from sqlalchemy import Column, String, Text, Integer, Boolean
from database import Base


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    price = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    is_available = Column(Boolean, default=True)

    def __repr__(self):
        return self.name
