from fastapi import FastAPI
from Homework.Module_17.app.routers import task
from Homework.Module_17.app.routers import user

app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True}, debug=True)


@app.get('/')
def welcome():
    return {'message': "Welcome to Taskmanager"}


app.include_router(user.router)
app.include_router(task.router)

# Запуск: python -m uvicorn Homework.Module_17.app.main:app --reload
