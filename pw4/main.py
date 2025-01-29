import input
import output
from domains import Person, Student, Course
import curses

def main(stdscr):   
    stdscr.clear()
    stdscr.refresh()
    num_stu=int(input.input_curses(stdscr,"Input number of students: "))
    student=[]
    course=[]

    info={}
    for i in range (num_stu):
        info=input.info_stu(stdscr)
        student.append(Student(info["ID"],info["Name"],info["DOB"]))
        
    num_course=int(input.input_curses(stdscr,"Input number of courses: "))
    for i in range(num_course):
        info=input.info_course(stdscr)
        course.append(Course(info["ID"],info["Name"],info["Credits"]))

    for i in range(len(course)):
        input.input_score(stdscr,student,course)
        
    for this_student in student:
        output.cal_GPA(this_student,course)
        
    output.list_student(stdscr,student)
    
    output.list_course(stdscr,course)
    
    output.show_GPA_desc(stdscr,student)
    
    stdscr.refresh()
curses.wrapper(main)