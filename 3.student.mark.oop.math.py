import math
import numpy as np
import curses

class Person:
    def __init__(self,name,dob):
        self.__name=name
        self.__dob=dob
    def getName(self):
        return self.__name
    def getDOB(self):
        return self.__dob
    def setName(self,name):
        self.__name=name
    def setDOB(self,dob):
        self.__dob=dob
        
class Student(Person):
    def __init__(self,id,name,dob):
        super().__init__(name,dob)
        self.__id=id
        self.__mark={}
        self.__gpa=0
    def __str__(self):
        return f"Student: {self.__id} - {self.__name} - DOB: {self.__dob}"
    def getID(self):
        return self.__id
    def setID(self,id):
        self.__id=id
    def setGPA(self,gpa):
        self.__gpa=gpa
    def getGPA(self):
        return self.__gpa
    def getMark(self):
        return self.__mark
    def getMark(self,course):
        return self.__mark[course]
    def setMark(self,course,mark):
        if course not in self.__mark:
            temp={course: mark}
            self.__mark|=temp
        else:
            self.__mark[course]=mark
    
class Course:
    def __init__(self,id,name,credit):
        self.__id=id
        self.__name=name
        self.__credit=credit
    def __str__(self):
        return f"Course: {self.__id} - {self.__name}"
    def getID(self):
        return self.__id
    def getName(self):
        return self.__name
    def getCredit(self):
        return self.__credit
    def setID(self,id):
        self.__id=id
    def setName(self,name):
        self.__name=name
    def setCredit(self,credit):
        self.__credit=credit

def info_stu(stdscr):
    info={}
    id=input_curses(stdscr,"Input ID of student: ")
    name=input_curses(stdscr,"Input student's name: ")
    dob=input_curses(stdscr,"Input student's DOB: ")
    info={"ID": id, "Name": name, "DOB":dob}
    return info

def info_course(stdscr):
    info={}
    id=input_curses(stdscr,"Input course's id: ")
    name=input_curses(stdscr,"Input couse's name: ")
    credit=int(input_curses(stdscr,"Input course's number of credits: "))
    info={"ID":id,"Name":name,"Credits":credit}
    return info

def input_score(stdscr,student,course):
    check=0
    while check==0:
        this_course=input_curses(stdscr,"Input ID of the course you want to input marks: ")
        for i in range(len(course)):
            if this_course==course[i].getID():
                check=1
                index=i
                break
        if check==0:
            stdscr.addstr("Course does not exist, input again: ")
    for i in range(len(student)):
        score=my_round(float(input_curses(stdscr,f"Input {this_course} score of {student[i].getName()} ({student[i].getID()}): ")))
        student[i].setMark(this_course,score)
    
def list_student(stdscr,student):
    stdscr.clear()
    for i in range(len(student)):
        stdscr.addstr(f"Student {i+1}: {student[i].getID()} - {student[i].getName()} - {student[i].getDOB()}\n")
    stdscr.addstr("\nPress any key to exit...")
    stdscr.refresh()
    stdscr.getch()
        
def list_course(stdscr,course):
    stdscr.clear()
    for i in range(len(course)):
        stdscr.addstr(f"Course {i+1}: {course[i].getID()} - {course[i].getName()}\n")
    stdscr.addstr("\nPress any key to exit...")
    stdscr.refresh()
    stdscr.getch()
        
def show_mark(stdscr,student,course):
    
    stdscr.clear()
    for this_student in student:
        stdscr.addstr(this_student.getMark(course))

def show_GPA_desc(stdscr,student):
    stdscr.clear()
    gpa=[]
    for this_student in student:
        gpa.append((this_student.getGPA(),this_student.getName(),this_student.getID()))
    dtype=[('gpa','f4'),('name','U50'),('id','U50')]
    gpa_np=np.array(gpa,dtype=dtype)
    gpa_np=np.sort(gpa_np,order='gpa')[::-1]
    stdscr.addstr("Students' GPA:\n")
    index=1
    for this_student in gpa_np:
        stdscr.addstr(f"- Student {index}: {this_student['name']} ({this_student['id']}) - GPA: {this_student['gpa']}\n")
        index+=1
    stdscr.addstr("\nPress any key to exit...")
    stdscr.refresh()
    stdscr.getch()

def input_curses(stdscr,prompt):
    stdscr.scrollok(True)
    row,col=stdscr.getyx()
    max_rows,max_cols=stdscr.getmaxyx()
    if (row+1>=max_rows):
        stdscr.scroll(1)
        row-=1
    stdscr.addstr(row+1,0,prompt[:max_cols-1])
    stdscr.refresh()
    curses.echo()
    input=stdscr.getstr().decode("utf-8")
    curses.noecho()
    return input

def my_round(n):
    second=(n*100)%10
    if (second<5):
        return math.floor(n*10)/10
    else:
        return math.floor(n*10+1)/10

def cal_GPA(student,list_course):
    mark=[]
    credits=[]
    for course in list_course:
        mark.append(student.getMark(course.getID()))
        credits.append(course.getCredit())
    mark_np=np.array(mark)
    credits_np=np.array(credits)
    student.setGPA(my_round(np.average(mark_np,weights=credits_np))) 

def main(stdscr):   
    stdscr.clear()
    stdscr.refresh()
    num_stu=int(input_curses(stdscr,"Input number of students: "))
    student=[]
    course=[]

    info={}
    for i in range (num_stu):
        info=info_stu(stdscr)
        student.append(Student(info["ID"],info["Name"],info["DOB"]))
        
    num_course=int(input_curses(stdscr,"Input number of courses: "))
    for i in range(num_course):
        info=info_course(stdscr)
        course.append(Course(info["ID"],info["Name"],info["Credits"]))

    for i in range(len(course)):
        input_score(stdscr,student,course)
        
    for this_student in student:
        cal_GPA(this_student,course)
        
    list_student(stdscr,student)
    
    list_course(stdscr,course)
    
    show_GPA_desc(stdscr,student)
    
    stdscr.refresh()
curses.wrapper(main)