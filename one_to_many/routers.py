from fastapi import FastAPI

from main import Department, Employee, SessionLocal
from schema import DepartmentResponse,EmployeeRequest
from main import Base,engine


app=FastAPI()
Base.metadata.create_all(bind=engine)

@app.post('/departments')
def create_department(data:DepartmentResponse):

    db=SessionLocal()

    department=Department(name=data.name)

    db.add(department)
    db.commit()
    db.refresh(department)

    return department

@app.post("/employees")
def create_employees(data:EmployeeRequest):
    db=SessionLocal()

    department = (
    db.query(Department)
    .filter(Department.id == data.department_id)
    .first()
    )
    
    employee=Employee(name=data.name,department_id=data.department_id)
    db.add(employee)
    db.commit()
    db.refresh(employee)

    return {"employee":employee,"department_name":department.name}