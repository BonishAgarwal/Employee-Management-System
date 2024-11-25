from app.models.models import Project #contains sqlalchemy models


class Projects:
    def __init__(self, db):
        self.db = db
    
    def add_project(self, p):
        print(p)
        new_project = Project(
            name = p.name
        )
        
        self.db.add(new_project)
        self.db.commit()
        self.db.refresh(new_project)
        
        return { "project_id": new_project.id }

    def get_all_projects(self):
        projects = self.db.query(Project).all()
        
        return projects

    def get_project_by_id(self, p_id):
        project = self.db.query(Project).filter(Project.id == p_id).first()
        
        return project

    def update_project(self, p_id, emp):
        project = self.db.query(Project).filter(Project.id == p_id).first()
        
        if project:
            project.name = emp.name
            project.age = emp.age
            project.salary = emp.salary
            project.role = emp.role
            
            self.db.commit()
            self.db.refresh(project)  # Refresh to get the updated data

        return project