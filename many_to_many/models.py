# One student can have many courses.
# One course can have many students.
# This requires a junction/association table


from sqlalchemy import Column, ForeignKey, Integer, String, Table, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine("sqlite:///school.db", connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# assosiation table
student_course = Table(
    "student_course",
    Base.metadata,
    # "Register the student_course table in the same metadata collection as my ORM models.( Base.metadata)"
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
)


# student table
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # secondary is used to define tehassosiation table
    courses = relationship(
        "Course", secondary=student_course, back_populates="students"
    )


# course table
class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship(
        "Student", secondary=student_course, back_populates="courses"
    )


# one time for only the table creation
# Base.metadata.create_all(bind=engine)
