class Student:
    def __init__(self,id,name,dob):
        self.__id=id
        self.__name=name
        self.__dob=dob
    def __str__(self):
        return f"Student: {self.__id} - {self.__name} - DOB: {self.__dob}"
    def getID(self):
        return self.__id
    def getName(self):
        return self.__name
    def getDOB(self):
        return self.__dob
    def setID(self,id):
        self.__id=id
    def setName(self,name):
        self.__name=name
    def setDOB(self,dob):
        self.__dob=dob
    
class Course:
    def __init__(self,id,name):
        self.__id=id
        self.__name=name
    def __str__(self):
        return f"Course: {self.__id} - {self.__name}"
    def getID(self):
        return self.__id
    def getName(self):
        return self.__name
    def setID(self,id):
        self.__id=id
    def setName(self,name):
        self.__name=name

class StudentMark:
    def __init__(self,id_stu,id_course,mark):
        self.__id_stu=id_stu
        self.__id_course=id_course
        self.__mark=mark
    def __str__(self):
        return f"{self.__id_stu} - {self.__id_course} Score: {self.__mark}"

def info_stu():
    info={}
    print()
    id=input("Input ID of student: ")
    name=input("Input student's name: ")
    dob=input("Input student's DOB: ")
    info={"ID": id, "Name": name, "DOB":dob}
    return info

def info_course():
    info={}
    print()
    id=input("Input course's id: ")
    name=input("Input couse's name: ")
    info={"ID":id,"Name":name}
    return info

def input_score(infostu,infocourse):
    course=input("Input name or ID of the course you want to input marks: ")
    for i in range(0,len(infocourse)):
        if course==infocourse[i].getName() or course==infocourse[i].getID():
            check=1
            index=i
            break
        else:
            check=0
    if check==1:
        info={}
        for i in range(0,len(infostu)):
            score=float(input(f"Input {course} score of {infostu[i].getName()} ({infostu[i].getID()}): "))
            info[i]=StudentMark(infostu[i].getID(),infocourse[index].getID(),score)
        return info
    else:
        print("Course does not exist")
        return 0
    
def list_student(student):
    for i in range(len(student)):
        print(f"Student {i+1}: {student[i].getID()} - {student[i].getName()} - {student[i].getDOB()}")
        
def list_course(course):
    for i in range(len(course)):
        print(f"Course {i+1}: {course[i].getID()} - {course[i].getName()}")
        
def show_mark(mark):
    for i in range(len(mark)):
        print(mark[i])
        
num_stu=int(input("Input number of students: "))
student=[]
course=[]
mark=[]

info={}
for i in range (num_stu):
    info=info_stu()
    student.append(Student(info["ID"],info["Name"],info["DOB"]))
print()
num_course=int(input("Input number of courses: "))
for i in range(num_course):
    info=info_course()
    course.append(Course(info["ID"],info["Name"]))
print()
mark=input_score(student,course)
print()
list_student(student)
print()
list_course(course)
print()
show_mark(mark)
    