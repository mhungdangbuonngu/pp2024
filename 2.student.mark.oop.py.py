class Student:
    def __init__(self,id,name,dob):
        self.id=id
        self.name=name
        self.dob=dob
        self.marks={}

class Course:
    def __init__(self,id,name):
        self.id=id
        self.name=name

def input_student():
    num=int(input("enter number of student: "))
    students = []
    
    for i in range(num):
        id=input("input student id: ")
        name=input("input student name: ") 
        dob=input("enter student dob: ")
        student = Student(id,name,dob)
        students.append(student)
        
    return students

def input_course():
    num=int(input("input number of course: "))
    courses=[]
    
    for i in range(num):
        id=input("enter course id: ")
        name= input("enter course name: ")
        course = Course(id,name)
        courses.append(course)
        
    return courses

def input_marks(students,courses):
    id=input("input course id that want to enter mark: ")
    
    for student in students:
        marks=float(input(f"enter mark for {student.name}: "))
        student.marks[id]=marks
            
def list_student(students):
    for student in students:
        print(f"Name: {student.name}, ID: {student.id},dob: { student.dob}.")

def list_course(courses):
    for course in courses:
        print(f"course's name: {course.name}, course's ID: {course.id}")
        
def student_marks(students):
    id=input("enter id: ")
    
    for student in students:
        if id in student.marks:
            print(f"name:{student.name}, mark: {student.marks[id]}")

student_list=input_student()
course_list=input_course()
input_marks(student_list,course_list)
list_student(student_list)
list_course(course_list)
student_marks(student_list)            

                     