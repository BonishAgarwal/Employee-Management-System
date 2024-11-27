# https://fastapi.tiangolo.com/tutorial/dependencies/#import-depends

# So using dependency injection we can keep our code cleaner by code reusability.

# In this, we had to create tasks instance every single route and add observer, but using dependency injection,
# we can create a reusable code and use this method.

# Depends(get_db) where get_db is a callable function

from fastapi import Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.controllers.task import Tasks
from app.observers.email_notification import EmailNotification

# Global variable for the instance of Tasks (singleton)
tasks_service_instance = None

def get_tasks_service(db: Session = Depends(get_db)):
    global tasks_service_instance # Following singelton design pattern

    if tasks_service_instance is None:
        tasks_service_instance = Tasks(db)
        
        tasks_service_instance.add_observers(EmailNotification())
    
    return tasks_service_instance
    