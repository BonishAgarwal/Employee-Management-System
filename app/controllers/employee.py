from app.models.models import Employee, EmployeeProjectMapping, Project#contains sqlalchemy models


class Employees:
    
    def __init__(self, db):
        self.db = db
    
    def add_employee(self, emp):
        new_employee = Employee(
            name = emp.name,
            age = emp.age,
            salary = emp.salary,
            role = emp.role
        )

        self.db.add(new_employee)
        self.db.commit()
        self.db.refresh(new_employee)
        
        return { "employee_id": new_employee.id }

    def get_all_employees(self):
        employees = self.db.query(Employee).all()
        
        return employees

    def get_employee_by_id(self, emp_id):
        employee = self.db.query(Employee).filter(Employee.id == emp_id).first()
        
        return employee

    def update_employee(self, emp_id, emp):
        employee = self.db.query(Employee).filter(Employee.id == emp_id).first()
        
        if employee:
            employee.name = emp.name
            employee.age = emp.age
            employee.salary = emp.salary
            employee.role = emp.role
            
            self.db.commit()
            self.db.refresh(employee)  # Refresh to get the updated data

        return employee

    def get_all_project_for_employee(self, emp_id):
        projects = self.db.query(Project).join(EmployeeProjectMapping, EmployeeProjectMapping.project_id == Project.id).filter(EmployeeProjectMapping.employee_id == emp_id).all()
        
        all_projects = [project.name for project in projects]
        
        return all_projects