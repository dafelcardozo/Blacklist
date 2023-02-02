from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Blacklisted(Base):
    __tablename__ = "blacklisted_users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    reason = Column(String, index=True)
    game_id = Column(Integer, index=True)
