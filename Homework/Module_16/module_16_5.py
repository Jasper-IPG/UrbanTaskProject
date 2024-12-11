"""Список пользователей в шаблоне"""
from fastapi import FastAPI, HTTPException, Path, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated

app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True}, debug=True)
templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/", response_class=HTMLResponse)
async def get_all_users(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return templates.TemplateResponse('users.html', {'request': request, 'user': user})


@app.post("/user/{username}/{age}", response_model=User)
async def add_user(username: Annotated[str, Path(min_length=4, max_length=20, description='Enter username', example='UrbanUser')],
                   age: Annotated[int, Path(ge=18, le=100, description='Enter age', example='36')]) -> User:
    new_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='User ID')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                      age: Annotated[int, Path(ge=18, le=100, description='Enter age')]) -> User:
    try:
        user = next(user for user in users if user.id == user_id)
        user.username = username
        user.age = age
        return user
    except StopIteration:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: Annotated[int, Path(description='User ID')]) -> User:
    try:
        user = next(user for user in users if user.id == user_id)
        users.remove(user)
        return user
    except StopIteration:
        raise HTTPException(status_code=404, detail='User was not found')
