from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.models import TaskCreate
from app.db import get_db
from app.controllers.task import Tasks
from app.observers.base import Observer, Subject
from app.observers.email_notification import EmailNotification

router = APIRouter()

@router.post("/task")
def task(task: TaskCreate, db: Session = Depends(get_db)):
    t = Tasks(db)
    

    t.add_observers(EmailNotification())
    
    task_id = t.add_task(task)
    
    return task_id

@router.get("/task/{task_id}")
def task(task_id, db: Session = Depends(get_db)):
    t = Tasks()
    
    task = t.get_task(task_id)
    
    return task
    
@router.get("/tasks")
def tasks():
    t = Tasks()
    
    tasks = t.get_all_tasks()
    
    return tasks

@router.put("/task/{task_id}")
def task(task_id, task: TaskCreate, db: Session = Depends(get_db)):
    t = Tasks()
    
    task = t.update_task(task_id, task)
    
    return task

