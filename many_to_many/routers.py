from fastapi import FastAPI

from models import Course, SessionLocal, Student
from schemas import CourseCreate, EnrollStudent, StudentCreate


app = FastAPI()


@app.post("/students")
def create_student(data: StudentCreate):

    db = SessionLocal()

    student = Student(name=data.name)
    db.add(student)
    db.commit()
    db.refresh(student)

    return student

@app.post("/course")
def create_course(data:CourseCreate):
    db=SessionLocal()

    course=Course(name=data.name)

    db.add(course)
    db.commit()
    db.refresh(course)

    return course


#enroll student into course
@app.post("/enroll")
def enroll_student(data:EnrollStudent):

    db=SessionLocal()

    student=db.query(Student).filter(Student.id==data.student_id).first()

    course=db.query(Course).filter(Course.id==data.course_id).first()

#automatically inserts into: student_course
    student.courses.append(course)

    db.commit()

    return{ "mesaage":"student enrolled succesfully"}


#get students with courses
@app.get("/students/{student_id}")
def get_students(student_id:int):
    db=SessionLocal()

    student=db.query(Student).filter(Student.id==student_id).first()

    return{
        "id":student.id,
        "name":student.name,
        "courses":[
            course.name
            for course in student.courses
        ]

    }