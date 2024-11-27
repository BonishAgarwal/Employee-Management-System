from pydantic import BaseModel
from enum import Enum

class EmployeeCreate(BaseModel):
    name: str
    age: int
    salary: int
    role: str

class ProjectCreate(BaseModel):
    name: str

class TaskCreate(BaseModel):
    title: str
    description: str
    status: str
    project_id: int
    employee_id: int

class TaskStatusUpdate(BaseModel):
    status: str
    

class RoleEnum(str, Enum):
    admin = "Admin"
    manager = "Manager"
    employee = "Employee"

class UserLogin(BaseModel):
    password: str
    email: str
