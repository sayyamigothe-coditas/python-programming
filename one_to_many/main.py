from fastapi import FastAPI
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# first create an engine
engine = create_engine("sqlite:///users.db", connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# one department has many employees
# one to many relationship
class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    employees = relationship("Employee", back_populates="department")


class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    #back populates is used so the cahnges in one table should be visible also in another table
    department = relationship("Department", back_populates="employees")








