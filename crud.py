from sqlalchemy.orm import Session

from db.models import User, Sex, StatusTask, Task
from serializers import SexCreate, UserCreate, StatusTaskCreate, TaskCreate


def create_sex(db: Session, sex: SexCreate):
    """Создаем пол для пользователей в таблице sex."""
    db_sex = Sex(sex=sex.sex)
    db.add(db_sex)
    db.commit()
    db.refresh(db_sex)
    return db_sex


def create_user(db: Session, user: UserCreate):
    """Создаем пользователя в таблице user."""
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_status(db: Session, status: StatusTaskCreate):
    """Создаем статус в таблице status_task."""
    db_status = StatusTask(status_name=status.status_name)
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status


def create_task(db: Session, task: TaskCreate):
    """Создаем задачу в таблице task."""
    db_task = Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
