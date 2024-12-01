from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class Sex(Base):
    """Модель пола пользователя."""
    __tablename__ = "sex"

    id = Column(Integer, primary_key=True, index=True)
    sex = Column(String, nullable=False)
    users = relationship("User", back_populates="sex")


class User(Base):
    """Модель пользователя."""
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False, unique=True)
    sex_id = Column(Integer, ForeignKey("sex.id"))
    sex = relationship("Sex", back_populates="users")
    tasks = relationship("Task", back_populates="user")


class StatusTask(Base):
    """Модель для статусов задач."""
    __tablename__ = "status_task"

    id = Column(Integer, primary_key=True, index=True)
    status_name = Column(String, nullable=False, unique=True)
    tasks = relationship("Task", back_populates="status")


class Task(Base):
    """Модель для задач."""
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status_id = Column(Integer, ForeignKey("status_task.id"))
    status = relationship("StatusTask", back_populates="tasks")
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="tasks")
