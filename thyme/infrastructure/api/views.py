from typing import List

from fastapi import APIRouter
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


def build_router(app):
    router = APIRouter()

    @router.get("/", response_model=List[Task])
    async def get_tasks():
        tasks = app.get_tasks_usecase.execute()
        return tasks

    return router
