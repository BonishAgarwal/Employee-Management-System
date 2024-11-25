from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    age: int
    salary: int
    role: str

class ProjectCreate(BaseModel):
    name: str