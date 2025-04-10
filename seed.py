from conf.db import engine
from sqlalchemy.orm import Session
from models.models import Student, Group, Teacher, Subject, Grade, Base
from faker import Faker

fake = Faker()

Base.metadata.create_all(engine)

def create_groups(session):
    groups = []
    for _ in range(3):
        group_name = fake.word()
        group = Group(name=group_name)
        groups.append(group)
    session.add_all(groups)
    session.commit()

def create_teachers(session):
    teachers = []
    for _ in range(5):
        teacher_name = fake.name()
        teacher = Teacher(name=teacher_name)
        teachers.append(teacher)
    session.add_all(teachers)
    session.commit()

def create_subjects(session, teachers):
    subjects = []
    for _ in range(5):
        subject_name = fake.word()
        teacher = fake.random_choice(teachers)
        subject = Subject(name=subject_name, teacher_id=teacher.id)
        subjects.append(subject)
    session.add_all(subjects)
    session.commit()

def create_students(session, groups):
    students = []
    for _ in range(30):
        student_name = fake.name()
        group = fake.random_choice(groups)
        student = Student(name=student_name, group_id=group.id)
        students.append(student)
    session.add_all(students)
    session.commit()

def create_grades(session, students, subjects):
    for student in students:
        for subject in subjects:
            grade = Grade(student_id=student.id, course_id=subject.id, grade=fake.random_int(min=1, max=5), date=fake.date())
            session.add(grade)
    session.commit()

with Session(engine) as session:
    create_groups(session)
    create_teachers(session)
    teachers = session.query(Teacher).all()
    create_subjects(session, teachers)
    courses = session.query(Subject).all()
    groups = session.query(Group).all()
    create_students(session, groups)
    students = session.query(Student).all()
    create_grades(session, students, courses)

print("Database seeded successfully!")
