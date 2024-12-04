from pydantic import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from database import Base
from sqlalchemy.orm import relationship


# We import Base which is created from database.py 
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    status = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    user = relationship("User", back_populates="todos")    


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    todos = relationship("Todo", back_populates="user")
    created_at = Column(DateTime)
    updated_at = Column(DateTime)    
