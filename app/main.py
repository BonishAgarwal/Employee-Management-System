from fastapi import FastAPI
from app.routes.employee import router as employee_router
from app.routes.project import router as project_router
from app.routes.employee_project import router as employee_project_router
from app.routes.login import router as login_router
from app.routes.task import router as task_router
app = FastAPI()

from app.db import create_db
create_db()

# Include the routers
app.include_router(employee_router)
app.include_router(project_router)
app.include_router(employee_project_router)
app.include_router(login_router)
app.include_router(task_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Employee-Project API"}

