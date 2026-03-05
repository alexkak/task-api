from fastapi import APIRouter
from app.schemas.task import TaskCreate, TaskResponse

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse, status_code=201)
async def create_task(task: TaskCreate):

    return TaskResponse(
        id=1,
        title=task.title,
        description=task.description,
        priority=task.priority,
        created_at="2024-06-01T12:00:00Z"
    )