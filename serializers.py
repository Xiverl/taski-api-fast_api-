from pydantic import BaseModel


class Sex(BaseModel):
    """Сериализатор для чтения половой принадлежности."""
    id: int
    sex: str

    class Config:
        from_attributes = True


class SexCreate(BaseModel):
    """Серипализатор для создания пола."""
    sex: str


class UserCreate(BaseModel):
    """Сериализатор для содания пользователей"""
    first_name: str
    last_name: str
    age: int
    email: str
    sex_id: int


class User(BaseModel):
    """Сериализатор для чтения пользователей."""
    id: int
    first_name: str
    last_name: str
    age: int
    email: str
    sex: Sex

    class Config:
        from_attributes = True


class StatusTaskCreate(BaseModel):
    """Сериализатор для создания статусов задач."""
    status_name: str


class StatusTask(BaseModel):
    """Сериализатор для чтения статусов задач."""
    id: int
    status_name: str

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    """Сериализатор для создания задач."""
    title: str
    description: str
    status_id: int
    user_id: int


class Task(BaseModel):
    """Сериализатор для чтения зачач."""
    id: int
    title: str
    description: str
    status: StatusTask
    user: User

    class Config:
        from_attributes = True
