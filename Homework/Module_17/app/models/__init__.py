from Homework.Module_17.app.models.user import User
from Homework.Module_17.app.models.task import Task
from sqlalchemy.schema import CreateTable


print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))
