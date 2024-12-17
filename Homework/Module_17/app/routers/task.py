from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from Homework.Module_17.app.backend.db_depends import get_db
from typing import Annotated
from Homework.Module_17.app.models.user import User
from Homework.Module_17.app.models.task import Task
from Homework.Module_17.app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    return task


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], user_id: int, new_task: CreateTask):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db.execute(insert(Task).values(title=new_task.title,
                                   content=new_task.content,
                                   priority=new_task.priority,
                                   user_id=user_id,
                                   slug=slugify(new_task.title)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put('update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTask):
    task_update = db.scalar(select(Task).where(Task.id == task_id))
    if task_update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    db.execute(update(Task).where(Task.id == task_id).values(title=update_task.title,
                                                             content=update_task.content,
                                                             priority=update_task.priority))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task update is successful!'
    }


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task delete is successful!'
    }
