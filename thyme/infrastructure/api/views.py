from typing import List

from fastapi import APIRouter
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class Task(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


def build_router(app):
    router = APIRouter()

    @router.get("/", response_model=List[Task])
    async def get_tasks():  # pylint: disable=unused-variable
        tasks = app.get_tasks_usecase.execute()
        return tasks

    return router
