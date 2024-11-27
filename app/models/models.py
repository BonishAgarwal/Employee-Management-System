from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    salary = Column(Integer)
    role = Column(String)

    projects = relationship('EmployeeProjectMapping', back_populates='employee')
    tasks = relationship('Task', back_populates='employee')

class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    employees = relationship('EmployeeProjectMapping', back_populates='project')
    tasks = relationship('Task', back_populates='project')

class EmployeeProjectMapping(Base):
    __tablename__ = 'employee_projects'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    employee_id = Column(Integer, ForeignKey('employees.id'))
    
    #Establish relationship
    project = relationship('Project', back_populates='employees')
    employee = relationship('Employee', back_populates='projects')

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    status = Column(String, default="ToDo")
    
    project_id = Column(Integer, ForeignKey('projects.id'))
    employee_id = Column(Integer, ForeignKey('employees.id'))
    
    employee = relationship('Employee', back_populates='tasks')
    project = relationship('Project', back_populates='tasks')

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)

