from fastapi import HTTPException

from sqlalchemy.orm import Session
from datetime import datetime

import models,schemas


def get_todos(db: Session, skip:int=0, limit: int=100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def delete_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).delete()


def update_todo(db: Session, update_todo: models.Todo, todo_id: int):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo is not None:        
        todo.title = update_todo.title if update_todo.title != None else todo.title
        todo.status = update_todo.status if update_todo.status != None else todo.status
        todo.updated_at = datetime.now()
        db.commit()
        db.refresh(todo)        
        return todo
    else:
        raise HTTPException(status_code=400, detail="Todo is not found")


def create_todo(db: Session, todo:schemas.Todo):
    db_todo = models.Todo(title=todo.title,
                          status=todo.status,
                          created_at=datetime.now(),
                          updated_at=datetime.now())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


#implement CRUD user here
def get_users(db: Session, skip:int=0, limit: int=100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def delete_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).delete()


def update_user(db: Session, update_user: models.User, user_id: int):
    #we check email is already exist or not first
    email_exist = db.query(models.User).filter(models.User.email == update_user.email).first()
    if email_exist is not None:
        raise HTTPException(status_code=400, detail="Email is already in use")

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is not None:        
        user.name = update_user.name if update_user.name != None else user.name
        user.email = update_user.email if update_user.email != None else user.email
        user.updated_at = datetime.now()
        db.commit()
        db.refresh(user)        
        return user
    else:
        raise HTTPException(status_code=400, detail="User is not found")


def create_user(db: Session, user:schemas.User):
    #we check email is already exist or not first
    email_exist = db.query(models.User).filter(models.User.email == user.email).first()
    if email_exist is not None:
        raise HTTPException(status_code=400, detail="Email is already in use")

    db_user = models.User(name=user.name,
                          email=user.email,
                          created_at=datetime.now(),
                          updated_at=datetime.now())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_todos(db: Session, skip:int=0, limit: int=100, user_id: int=0):
    return db.query(models.Todo).filter(models.Todo.user_id == user_id).offset(skip).limit(limit).all()


def get_user_todo(db: Session, user_id: int, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.user_id == user_id
        ).filter(models.Todo.id == todo_id
        ).first()


def create_todo_v2(db: Session, todo:schemas.TodoV2, user_id: int):
    db_todo = models.Todo(user_id=user_id,
                          title=todo.title,
                          status=todo.status,
                          created_at=datetime.now(),
                          updated_at=datetime.now())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# NOTE :
# - To perform CRUD need to add object instance to the database session.
# - do commit changes
# - do refresh your instance to contain new data from the database.