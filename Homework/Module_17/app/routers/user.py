from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from Homework.Module_17.app.backend.db_depends import get_db
from typing import Annotated
from Homework.Module_17.app.models.user import User
from Homework.Module_17.app.models.task import Task
from Homework.Module_17.app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    return user


@router.get("/user_id/tasks")
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user_tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User and tasks were not found'
        )
    return user_tasks


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], new_user: CreateUser):
    user = db.scalar(select(User).where(User.slug == new_user.username))
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'Username: {new_user.username} already exists.'
        )
    db.execute(insert(User).values(username=new_user.username,
                                   firstname=new_user.firstname,
                                   lastname=new_user.lastname,
                                   age=new_user.age,
                                   slug=slugify(new_user.username)))
    db.commit()

    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put('update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    user_update = db.scalar(select(User).where(User.id == user_id))
    if user_update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db.execute(update(User).where(User.id == user_id).values(firstname=update_user.firstname,
                                                             lastname=update_user.lastname,
                                                             age=update_user.age))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update is successful!'
    }


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User delete is successful!'
    }
