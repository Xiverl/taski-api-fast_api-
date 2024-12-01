from fastapi import FastAPI, status, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session, joinedload

from db import database, models
from serializers import (
    UserCreate, SexCreate,
    User, Task, TaskCreate,
    StatusTaskCreate
)
from crud import create_user, create_sex, create_status, create_task

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():
    """Фунция для выдачи сессии для работы с БД."""
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/sex")
def add_sex(sex: SexCreate, db: Session = Depends(get_db)):
    db_sex = create_sex(db, sex)
    if db_sex is None:
        return JSONResponse(
            content={"message": "Ошибка при создании пола"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    return db_sex


@app.get("/users", response_model=list[User])
def read_root(request: Request, db: Session = Depends(get_db)):
    users = db.query(models.User).options(joinedload(models.User.sex)).all()
    return users


@app.post("/users")
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    if db_user is None:
        return JSONResponse(
            content={"message": "Ошибка при создании пользователя"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    return db_user


@app.get("/users/{id}")
def get_user(request: Request, id: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None:
        return JSONResponse(
            content={"message": "Пользователь не найден..."},
            status_code=status.HTTP_404_NOT_FOUND
        )
    return user


@app.post("/status")
def add_status_task(status: StatusTaskCreate, db: Session = Depends(get_db)):
    db_status = create_status(db, status)
    if db_status is None:
        return JSONResponse(
            content={"message": "Ошибка при создании пола"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    return db_status


@app.get("/tasks", response_model=list[Task])
def get_tasks(request: Request, db: Session = Depends(get_db)):
    tasks = db.query(models.Task).options(joinedload(models.Task.status)).all()
    return tasks


@app.post("/tasks")
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = create_task(db, task)
    if db_task is None:
        return JSONResponse(
            content={"message": "Ошибка при создании задачи"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    return db_task


@app.get("/tasks/{id}")
def ge_task(request: Request, id: str, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    if task is None:
        return JSONResponse(
            content={"message": "Задача не найдена..."},
            status_code=status.HTTP_404_NOT_FOUND
        )
    return task
