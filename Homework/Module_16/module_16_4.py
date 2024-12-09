"""Модель пользователя"""
from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
def get_all_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
def add_users(user: User, username: str, age: int):
    i = len(users)
    if i == 0:
        user.id = 1
    else:
        user.id = users[i - 1].id + 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int, user: str = Body()):
    fault_user = True
    for user in users:
        if user.id == user_id:
            fault_user = False
            user.username = username
            user.age = age
            return user
    if fault_user:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    fault_user = True
    i = 0
    for user in users:
        if user.id == user_id:
            fault_user = False
            users.pop(i)
            return user
        i += 1
    if fault_user:
        raise HTTPException(status_code=404, detail='User was not found')
