from sqlalchemy import func
from conf.db import SessionLocal
from models.models import Teacher, Group, Student
from my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10

def test_queries():
    print("\n1. Топ 5 студентів із найбільшим середнім балом:")
    print(select_1())

    print("\n2. Найкращий студент з математики:")
    print(select_2("Математика"))

    print("\n3. Середній бал у групах з фізики:")
    print(select_3("Фізика"))

    print("\n4. Середній бал на потоці:")
    print(select_4())

    # Get a random teacher
    db = SessionLocal()
    teacher_result = db.query(Teacher.fullname).order_by(func.random()).first()
    db.close()

    if teacher_result:
        teacher_name = teacher_result[0]
        print(f"\n5. Курси викладача {teacher_name}:")
        print(select_5(teacher_name))
    else:
        print("\n5. Не знайдено жодного викладача.")

    # Get a random group
    db = SessionLocal()
    group_result = db.query(Group.name).order_by(func.random()).first()
    db.close()

    if group_result:
        group_name = group_result[0]
        print(f"\n6. Студенти групи {group_name}:")
        print(select_6(group_name))

        print(f"\n7. Оцінки студентів групи {group_name} з математики:")
        print(select_7(group_name, "Математика"))
    else:
        print("\n6. Не знайдено жодної групи.")

    # Print the average grade for the random teacher
    print(f"\n8. Середній бал викладача {teacher_name if teacher_result else 'невідомий'}:")
    print(select_8(teacher_name if teacher_result else ''))

    # Get a random student
    db = SessionLocal()
    student_result = db.query(Student.fullname).order_by(func.random()).first()
    db.close()

    if student_result:
        student_name = student_result[0]
        print(f"\n9. Курси студента {student_name}:")
        print(select_9(student_name))

        print(f"\n10. Курси студента {student_name} від викладача {teacher_name if teacher_result else 'невідомий'}:")
        print(select_10(student_name, teacher_name if teacher_result else ''))
    else:
        print("\n9. Не знайдено жодного студента.")


if __name__ == "__main__":
    test_queries()
