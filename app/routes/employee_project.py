from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session
from app.db import get_db

from app.controllers.employee_project import EmployeeProject

router = APIRouter()

@router.post("/employee/{employee_id}/project/{project_id}/assign")
def assign(employee_id, project_id, db: Session = Depends(get_db)):
    ep = EmployeeProject(db)
    
    res = ep.assign_project_to_employee(employee_id, project_id)
    
    if res.get("status") == "success":
        return { "message": "Employee Assigned to project" }
    else:
        return { "message": "Unable to assign project" }
