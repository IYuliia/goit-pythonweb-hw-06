from faker import Faker
from conf.db import SessionLocal
from models.models import Teacher, Group, Student, Subject, Grade
import random

db = SessionLocal()

subject_names = ["Математика", "Фізика", "Інформатика", "Біологія", "Хімія", "Історія", "Англійська мова"]
group_names = ["Group A", "Group B", "Group 1", "Group 2", "Group 3"]
teacher_names = ["Dr. Іваненко", "Prof. Петров", "Dr. Сидоренко", "Prof. Коваль", "Dr. Тарасова"]

fake = Faker()

teachers = []
for _ in range(5):
    teacher = Teacher(fullname=random.choice(teacher_names))
    db.add(teacher)
    teachers.append(teacher)
    print(f"Added teacher: {teacher.fullname}")
db.commit()

groups = []
for group_name in group_names:
    group = Group(name=group_name)
    db.add(group)
    groups.append(group)
    print(f"Added group: {group.name}")
db.commit()

subjects = []
for subject_name in subject_names:
    subject = Subject(name=subject_name, teacher_id=random.choice(teachers).id)
    db.add(subject)
    subjects.append(subject)
    teacher_name = next(teacher.fullname for teacher in teachers if teacher.id == subject.teacher_id)
    print(f"Added subject: {subject.name} with teacher {teacher_name}")
db.commit()

students = []
for _ in range(20):
    student = Student(fullname=fake.name(), group_id=random.choice(groups).id)
    db.add(student)
    students.append(student)
    print(f"Added student: {student.fullname}")
db.commit()

for student in students:
    for subject in subjects:
        grade = Grade(grade=random.randint(1, 10), student_id=student.id, subject_id=subject.id, date_of=fake.date_this_decade())
        db.add(grade)
        print(f"Added grade {grade.grade} for {student.fullname} in {subject.name} on {grade.date_of}")
db.commit()

db.close()
