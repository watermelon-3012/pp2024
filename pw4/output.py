import numpy as np
from input import my_round

def cal_GPA(student,list_course):
    mark=[]
    credits=[]
    for course in list_course:
        mark.append(student.getMark(course.getID()))
        credits.append(course.getCredit())
    mark_np=np.array(mark)
    credits_np=np.array(credits)
    student.setGPA(my_round(np.average(mark_np,weights=credits_np))) 
    
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