import uuid
from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, text, Integer



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer , primary_key=True, nullable=False)
    name = Column(String,  nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    photo = Column(String, nullable=True)
    verified = Column(Boolean, nullable=False, server_default='False')
    role = Column(String, server_default='user', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    

