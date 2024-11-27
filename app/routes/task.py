from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.schemas.models import TaskCreate, TaskStatusUpdate
from app.db import get_db
from app.controllers.task import Tasks
from app.observers.base import Observer, Subject
from app.observers.email_notification import EmailNotification

from app.dependencies.task_dependencies import get_tasks_service
from app.auth.authorisation import authorise

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/task")
@authorise(allowed_roles=["admin", "manager"])
def task(task: TaskCreate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db), task_instance: Tasks = Depends(get_tasks_service)):
    task_id = task_instance.add_task(task)
    
    return task_id

@router.get("/task/{task_id}")
@authorise(allowed_roles=["admin", "manager", "employee"])
def task(task_id, db: Session = Depends(get_db), task_instance: Tasks = Depends(get_tasks_service)):
    
    task = task_instance.get_task(task_id)
    
    return task

@router.get("/tasks")
def tasks(db: Session = Depends(get_db), task_instance: Tasks = Depends(get_tasks_service)):
    
    tasks = task_instance.get_all_tasks()
    
    return tasks

@router.put("/task/{task_id}")
def task(task_id, task: TaskCreate, db: Session = Depends(get_db), task_instance: Tasks = Depends(get_tasks_service)):
    
    task = task_instance.update_task(task_id, task)
    
    return task

@router.put("/tasks/{task_id}/status")
def update_task_status(task_id, task_status: TaskStatusUpdate, db: Session = Depends(get_db), task_instance: Tasks = Depends(get_tasks_service)):
    
    task_instance.change_status(task_id, task_status.status)

