students = []
def input_number_of_students():
    s = int(input("Enter number of students: "))
    return s

def input_students_info():
    id = input("Enter student id: ")
    name = input("Enter student name: ")
    DoB = input("Enter DoB of student: ")
    students.append((id, name, DoB))
    
courses = []
def input_number_of_courses():
    c = int(input("Enter number of courses: "))
    return c

def input_courses_info():
    id = input("Enter course id: ")
    name = input("Enter course name: ")
    courses.append((id, name))

marks = []
def input_marks():
    course_id = input("Enter a course by id: ")
    for student in students:
        mark = input(f"Enter mark for student {student[1]} in course {course_id}: ")
        marks.append((course_id, student[0], mark))
        
def list_courses():
    if courses:
        print("List of courses:")
        for course in courses:
            print(course)
    else:
        print("No courses available.")

def list_students():
    if students:
        print("List of students:")
        for student in students:
            print(student)
    else:
        print("No students available.")

def show_marks():
    course_id = input("Select a course by id: ")
    if marks:
        print(f"Marks for course {course_id}:")
        for mark in marks:
            if mark[0] == course_id:
                print(f"Student {mark[1]} got {mark[2]}")
    else:
        print("No marks available.")

num_students = input_number_of_students()
for _ in range(num_students):
    input_students_info()

num_courses = input_number_of_courses()
for _ in range(num_courses):
    input_courses_info()

input_marks()

list_courses()
list_students()
show_marks()