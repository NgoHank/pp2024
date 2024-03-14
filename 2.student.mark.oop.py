class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB

    def __repr__(self):
        return f"Student({self.id}, {self.name}, {self.DoB})"


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Course({self.id}, {self.name})"


class Mark:
    def __init__(self, course_id, student_id, mark):
        self.course_id = course_id
        self.student_id = student_id
        self.mark = mark

    def __repr__(self):
        return f"Mark({self.course_id}, {self.student_id}, {self.mark})"


class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_number_of_students(self):
        num_students = int(input("Enter number of students: "))
        return num_students

    def input_students_info(self):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        DoB = input("Enter DoB of student: ")
        self.students.append(Student(id, name, DoB))

    def input_number_of_courses(self):
        num_courses = int(input("Enter number of courses: "))
        return num_courses

    def input_courses_info(self):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        self.courses.append(Course(id, name))

    def input_marks(self):
        course_id = input("Enter a course by id: ")
        for student in self.students:
           mark = input(f"Enter mark for student {student.name} in course {course_id}: ")
           self.marks.append(Mark(course_id, student.id, mark))

    def list_courses(self):
        if self.courses:
            print("List of courses:")
            for course in self.courses:
                print(course)
        else:
            print("No courses available.")

    def list_students(self):
        if self.students:
            print("List of students:")
            for student in self.students:
                print(student)
        else:
            print("No students available.")

    def show_marks(self):
        course_id = input("Select a course by id: ")
        if self.marks:
            print(f"Marks for course {course_id}:")
            for mark in self.marks:
                if mark.course_id == course_id:
                    print(f"Student {self.get_student_name(mark.student_id)} got {mark.mark}")
        else:
            print("No marks available.")

    def get_student_name(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student.name
        return ""


school = School()
num_students = school.input_number_of_students()
for _ in range(num_students):
    school.input_students_info()

num_courses = school.input_number_of_courses()
for _ in range(num_courses):
    school.input_courses_info()

school.input_marks()
school.list_courses()
school.list_students()
school.show_marks()