from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.models import ProjectCreate
from app.db import get_db

from app.controllers.project import Projects

router = APIRouter()

@router.post("/project")
def project(project: ProjectCreate, db: Session = Depends(get_db)):
    
    p = Projects(db)
    res = p.add_project(project)
    
    project_id = res.get("project_id")
    
    return {"message": "Project created successfully!", "employee": project_id} 

@router.get('/project')
def project(db: Session = Depends(get_db)):
    
    p = Projects(db)
    projects = p.get_all_projects()
    
    return projects

@router.get("/project/{project_id}")
def get_project(project_id, db: Session = Depends(get_db)):
    p = Projects(db)
    
    project = p.get_project_by_id(project_id)
    
    return project

@router.put("/project/{project_id}")
def project(project_id, project: ProjectCreate, db: Session = Depends(get_db)):
    p = Projects(db)
    
    project = p.update_project(project_id, project)
    
    return project
