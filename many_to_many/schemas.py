from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str

class CourseCreate(BaseModel):
    name: str

class EnrollStudent(BaseModel):
    student_id: int
    course_id: int