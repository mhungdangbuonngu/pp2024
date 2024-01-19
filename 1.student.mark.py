def input_student():
    num_student=int(input("enter number of student:"))
    students=[]

    for i in range (num_student):
        student_id=input("enter student ID:")
        name= input("enter name: ")
        dob= input("enter dob:")
        student_info={'name': name,'id':student_id,'dob': dob,'marks': {}}
        students.append(student_info)
    
    return students

def input_course():
    num_course=int(input("enter number of course:"))
    courses = []

    for i in range(num_course):
        course_id=input("enter course id: ")
        course_name=input("enter course name: ")
        course_info={'id': course_id,'name':course_name}
        courses.append(course_info)
    
    return courses

def input_marks(students,courses):
    course_id=input("enter the course id that want to input marks: ")

    for student in students:
        marks=input(f"enter marks for {student['name']}: ")
        student['marks'][course_id]=marks

def list_student(students):
    print("\nlist of student: ")
    for student in students:
        print(f"name: {student['name']},ID: {student['id']},DOB: {student['dob']}")         

def list_course(courses):
    print("\nlist of course: ")
    for course in courses:
        print(f"{course['name']},{course['id']}") 
   
def student_marks(students):
    id = input("enter course id: ")
    for student in students:
        if id in student['marks']:
            print(f"\n{student['name']} , {student['id']} , {student['marks'][id]}")

student_list=input_student()
course_list=input_course()
list_student(student_list)
list_course(course_list)
input_marks(student_list,course_list)
student_marks(student_list)