from pony.orm import Database, Required, Set, db_session
from random import choice

db = Database()

class Student(db.Entity):
    name = Required(str)
    courses = Set('Course')

class Course(db.Entity):
    name = Required(str)
    students = Set(Student)

db.bind(provider='sqlite', filename=':memory:')
db.generate_mapping(create_tables=True)

with db_session:
    # Створення курсів, студентів та їх розподілення
    courses = [Course(name=f'Course {i}') for i in range(1, 6)]
    students = [Student(name=f'Student {i}') for i in range(1, 21)]
    for student in students:
        student.courses.add(choice(courses))

    # Додавання нового студента та реєстрація на курс
    new_student = Student(name='New Student')
    new_student.courses.add(choice(courses))

# Запити до БД
@db_session
def get_students_by_course(course_name):
    course = Course.get(name=course_name)
    students_on_course = [student.name for student in course.students]
    if course:
        print(f'Students on {course_name}: {', '.join(students_on_course)}')
        return students_on_course
    return []

@db_session
def get_courses_by_student(student_name):
    curr_student = Student.get(name=student_name)
    courses_for_student = [course.name for course in curr_student.courses]
    if curr_student:
        print(f'Student {student_name} is on {', '.join(courses_for_student)} course(s)')
        return courses_for_student
    return []

# Оновлення та видалення даних
@db_session
def update_student_name(old_name, new_name):
    curr_student = Student.get(name=old_name)
    if curr_student:
        curr_student.name = new_name
        print('User updated')

@db_session
def delete_student(student_name):
    curr_student = Student.get(name=student_name)
    if curr_student:
        curr_student.delete()
        print('User deleted')

# Приклади викликів функцій
get_courses_by_student('Student 2')
get_students_by_course('Course 1')

update_student_name('Student 2', 'Updated Student')
delete_student('Student 1')