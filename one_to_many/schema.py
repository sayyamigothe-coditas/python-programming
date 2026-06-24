
from pydantic import BaseModel


class EmployeeResponse(BaseModel):
    
    name:str
    department_id:int
    department:DepartmentResponse

class EmployeeRequest(BaseModel):
    
    name:str
    department_id:int


class DepartmentResponse(BaseModel):
    name:str
