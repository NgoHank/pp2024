# 1.student.mark.py

students = []
courses = []
marks = []

def input_number_of_students():
    num = int(input("Enter number of students: "))
    return num

def input_student_info():
    id = input("Enter student id: ")
    name = input("Enter student name: ")
    dob = input("Enter student DoB: ")
    students.append((id, name, dob))

def input_number_of_courses():
    num = int(input("Enter number of courses: "))
    return num

def input_course_info():
    id = input("Enter course id: ")
    name = input("Enter course name: ")
    courses.append((id, name))

def input_marks():
    course_id = input("Select a course by id: ")
    for student in students:
        mark = input(f"Enter mark for student {student[1]} in course {course_id}: ")
        marks.append((course_id, student[0], mark))

def list_courses():
    for course in courses:
        print(course)

def list_students():
    for student in students:
        print(student)

def show_marks():
    course_id = input("Select a course by id: ")
    for mark in marks:
        if mark[0] == course_id:
            print(f"Student {mark[1]} got {mark[2]} in course {course_id}")

# Test the functions
num_students = input_number_of_students()
for _ in range(num_students):
    input_student_info()

num_courses = input_number_of_courses()
for _ in range(num_courses):
    input_course_info()

input_marks()

list_courses()
list_students()
show_marks()
