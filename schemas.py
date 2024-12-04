from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime


class Todo(BaseModel):
    title : str
    status : str


class TodoRead(Todo):
    id: int
    created_at : datetime
    updated_at : datetime


class TodoPatch(BaseModel):
    # These properties are optional to comply with partial update
    # on PATCH request and can be ommitted
    title: Optional[str] = None
    status: Optional[str] = None


class TodoDelete(BaseModel):
    id: int


class TodoV2(BaseModel):
    title : str
    status : str


class TodoReadV2(TodoV2):
    id: int
    created_at : datetime
    updated_at : datetime

    class Config:
        orm_mode = True


class User(BaseModel):
    name : str
    email : str


class UserCreate(User):
    pass


class UserRead(User):
    id: int
    created_at : datetime
    updated_at : datetime
    #from models we put relationship one to many between
    #User and Todo
    todos : list[Todo] = []


class UserPatch(BaseModel):
    # These properties are optional to comply with partial update
    # on PATCH request and can be ommitted
    name: Optional[str] = None
    email: Optional[str] = None

