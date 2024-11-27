from pydantic import BaseModel

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
    

class User(BaseModel):
    username: str
    password: str
