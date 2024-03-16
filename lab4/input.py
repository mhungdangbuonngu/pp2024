from math import *
from domain import StudentClass,CourseClass

def inputS():
    a=int(input("enter number of students: "))
    students=[]
    for i in range (a):
        b=input("insert name: ")
        c=input("insert id: ")
        d=input("insert dob: ")
        student=StudentClass.Student(b,c,d)
        students.append(student)
    return students    
def inputC():
    a=int(input("insert number of course: "))
    courses=[]
    for i in range(a):
        b=input("name course: ")
        c=input("id: ")
        d=int(input("input etc: "))
        course=CourseClass.Course(b,c,d)
        courses.append(course)
        
    return courses

def input_mark(students,courses):
    for course in courses:
        for student in students:
            marks=float(input(f"input mark for {student.getName()} of course {course.getName()} :"))
            markss=floor(marks*10)/10
            student._mark[course.getId()]=markss