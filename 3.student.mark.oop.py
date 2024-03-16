import numpy as np
from math import *
import tkinter as tk
from tkinter import ttk 

class Student:
    
    def __init__(self,name:str,id:str,dob:str):
        self.__name=name
        self.__id=id
        self.__dob=dob
        self._mark={}
        self.__gpa=0
    def getName(self):
        return self.__name
    
    def getId(self):
        return self.__id
    
    def getDob(self):
        return self.__dob
    
    def setGpa(self,gpa):
        self.__gpa=gpa
    
    def getGpa(self):
        return self.__gpa
class Course:
    def __init__(self,name,id,etc):
        self.__name=name
        self.__id=id
        self.__etc=etc
        
    def getName(self):
        return self.__name
    
    def getId(self):
        return self.__id
    
    def getEtc(self):
        return self.__etc
    
def inputS():
    a=int(input("enter number of students: "))
    students=[]
    for i in range (a):
        b=input("insert name: ")
        c=input("insert id: ")
        d=input("insert dob: ")
        student=Student(b,c,d)
        students.append(student)
    return students    
def inputC():
    a=int(input("insert number of course: "))
    courses=[]
    for i in range(a):
        b=input("name course: ")
        c=input("id: ")
        d=int(input("input etc: "))
        course=Course(b,c,d)
        courses.append(course)
        
    return courses

def input_mark(students,courses):
    for course in courses:
        for student in students:
            marks=float(input(f"input mark for {student.getName()} of course {course.getName()} :"))
            markss=floor(marks*10)/10
            student._mark[course.getId()]=markss

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
#gui 
window=tk.Tk()
window.title("super dupper doom")
window.geometry('340x440')

#ttk 
label=ttk.Label(window,text='student management ') 
label.pack()

inputButton=ttk.Button(window,text='input mark', command=inputMarkCmd)
inputButton.pack(ipadx=7,ipady=7)

countGpas=ttk.Button(window,text='count Gpa',command=countGpaCmd)
countGpas.pack(ipadx=7,ipady=7)

sortButton=ttk.Button(window, text='sort gpa', command=sortGpaCmd)      
sortButton.pack(ipadx=7,ipady=7)

showGButton=ttk.Button(window, text="show gpa",command=showGpaCmd)
showGButton.pack(ipadx=6,ipady=6)

showMButton=ttk.Button(window, text='show marks',command=showMarkCmd)
showMButton.pack(ipadx=6,ipady=6)


window.mainloop()
#endregion