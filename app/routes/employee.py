from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer
from app.schemas.models import EmployeeCreate #contains pydantic models

from sqlalchemy.orm import Session
from app.db import get_db

from app.controllers.employee import Employees
from app.auth.decode_token import authenticate

router = APIRouter()

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/")
@authenticate
def home(token: str = Depends(oauth2_scheme), user: dict = None):
    return "Hello World!!"

@router.post("/employee")
def employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    
    emp = Employees(db)
    res = emp.add_employee(employee)
    
    employee_id = res.get("employee_id")
    
    return {"message": "Employee created successfully!", "employee": employee_id}

@router.get('/employee')
def employee(db: Session = Depends(get_db)):
    
    emp = Employees(db)
    employees = emp.get_all_employees()
    
    return employees

@router.get("/employee/{employee_id}")
def get_employee(employee_id, db: Session = Depends(get_db)):
    emp = Employees(db)
    
    employee = emp.get_employee_by_id(employee_id)
    
    return employee

@router.put("/employee/{employee_id}")
def employee(employee_id, employee: EmployeeCreate, db: Session = Depends(get_db)):
    emp = Employees(db)
    
    employee = emp.update_employee(employee_id, employee)
    
    return employee

@router.get("/employee/{employee_id}/projects")
def get_projects_for_employee(employee_id, db: Session = Depends(get_db)):
    emp = Employees(db)
    
    all_projects = emp.get_all_project_for_employee(employee_id)
    
    return all_projects
    