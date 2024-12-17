from fastapi import FastAPI
from Homework.Module_17.app.routers import task, user


app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True}, debug=True)


@app.get('/')
def welcome() -> dict:
    return {'message': "Welcome to Taskmanager"}


# Подключаем роутер
app.include_router(user.router)
app.include_router(task.router)

# Создаём таблицы в базе данных
# Base.metadata.create_all(bind=engine)

# Запуск: python -m uvicorn Homework.Module_17.app.main:app --reload
