import curses
import math

def my_round(n):
    second=(n*100)%10
    if (second<5):
        return math.floor(n*10)/10
    else:
        return math.floor(n*10+1)/10
    
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
    