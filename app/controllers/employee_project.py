from app.models.models import Employee, Project, EmployeeProjectMapping

class EmployeeProject:
    def __init__(self, db):
        self.db = db
        
    def assign_project_to_employee(self, employee_id, project_id):
        employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        
        project = self.db.query(Project).filter(Project.id == project_id).first()
        
        if employee and project:
            emp_mapping = EmployeeProjectMapping(
                employee_id = employee_id,
                project_id = project_id
            )
            
            self.db.add(emp_mapping)
            self.db.commit()
            self.db.refresh(emp_mapping)
            
            return { "status": "success" }
        else:
            return { "status": "error" }
            