from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import func

from database import Base


class Blacklisted(Base):
    __tablename__ = "blacklisted_users_2"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    reason = Column(String, index=True)
    game_id = Column(Integer, index=True)
    date = Column(DateTime(timezone=True), default=func.now())
