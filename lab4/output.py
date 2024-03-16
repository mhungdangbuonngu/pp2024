from math import *
from input import *
import numpy as np

def countGpa(students,courses):
    for student in students:
        mark=0
        etcs=0
        for course in courses:
            mark += student._mark[course.getId()]*course.getEtc()
            etcs += course.getEtc()
        gpa=floor((mark/etcs)*10)/10
        student.setGpa(gpa)
    
    return students    

def showGpa(students):
    for student in students:
        print(f"gpa for {student.getName()} is: {student.getGpa()}")            
def showMark(students,courses):
    for student in students:
        for course in courses:
            print(f"{student.getName()}'s mark for {course.getName()} is: {student._mark[course.getId()]} ")

def sortGpa(students):
    dtype=[('name','U50'),('id','U20'),('dob','U20'),('mark',object),('gpa',float)]
    student_array = np.array([(student.getName(), student.getId(), student.getDob(), student._mark, student.getGpa()) for student in students], dtype=dtype)
    sorted_array = np.argsort(student_array['gpa'])[::-1]
    print(f"order: ")
    for i, index in enumerate(sorted_array, start=1):
        student = student_array[index]
        print(f"{i}. {student['name']}: {student['gpa']}")
#region bottom function
list_student=inputS()
list_course=inputC()
def inputMarkCmd():
    input_mark(list_student,list_course)
def countGpaCmd():
    countGpa(list_student,list_course)
def sortGpaCmd():
    sortGpa(list_student)
def showMarkCmd():
    showMark(list_student,list_course)
def showGpaCmd():
    showGpa(list_student)     