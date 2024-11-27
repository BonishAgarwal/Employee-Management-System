from app.models.models import Task
from app.observers.base import Subject

class Tasks(Subject):
    
    def __init__(self, db):
        self.db = db
        super().__init__()
    
    def add_task(self, task):
        task = Task(
            title = task.title,
            description = task.description,
            status = task.status,
            employee_id = task.employee_id,
            project_id = task.project_id
        )
        
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        
        self.notify_observers({"email": "bonishgarg@gmail.com"})
        
        return { "task_id": task.id } 
        
    
    def get_task(self, task_id):
        task = self.db.query(Task).filter(Task.id==task_id).first()
        
        return task

    def get_all_tasks(self):
        tasks = self.db.query(Task).all()
        
        return tasks
    
    def update_task(self, task_id, task):
        exis_task = self.db.query(Task).filter(Task.id==task_id).first()
        
        if exis_task:
            exis_task.title = task.title
            exis_task.descripton = task.description
            exis_task.status = task.status
            
            self.db.commit()
            self.db.refresh(exis_task)
            
        return exis_task