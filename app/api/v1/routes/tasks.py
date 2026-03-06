from fastapi import APIRouter

from app.schemas.task import TaskCreate, TaskResponse
from app.core.exceptions import NotFoundException

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

@router.get("/tasks/{task_id}", response_model=TaskResponse, status_code=200)
async def get_task(task_id: int):
    if task_id != 1:
        raise NotFoundException("Task not found")
    
    return TaskResponse(
        id=1,
        title="Sample Task",
        description="This is a sample task",
        priority=1,
        created_at="2024-06-01T12:00:00Z"
    )