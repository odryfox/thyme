from fastapi import APIRouter


def build_router(service):
    router = APIRouter()

    @router.get("/")
    async def get_tasks():
        return [{"service": service()}]

    return router
