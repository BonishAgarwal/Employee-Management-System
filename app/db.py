from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

import app.models.models

# Replace the below values with your PostgreSQL credentials
DATABASE_URL = "postgresql://postgres:@localhost/employee_management_system"

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a session
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables in the database
def create_db():
    Base.metadata.create_all(engine)

# Dependency to get the DB session
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()