def num_stu():
    n=int(input("Input number of students: "))
    return n
def info_stu(n):
    info={}
    for i in range(0,n):
        print("- Student",i+1,":")
        id=input("Input ID of student: ")
        name=input("Input student's name: ")
        dob=input("Input student's DOB: ")
        info[i]={"ID": id, "Name": name, "DOB":dob}
    return info
def num_course():
    n=int(input("Input number of courses: "))
    return n
def info_course(n):
    info={}
    for i in range(0,n):
        print("- Course",i+1,":")
        id=input("Input course's id: ")
        name=input("Input couse's name: ")
        info[i]={"ID":id,"Name":name}
    return info
    
numstu=num_stu()
infostu=info_stu(numstu)
for i in range(0,numstu):
    print(infostu[i],"\n")
numcourse=num_course()
infocourse=info_course(numcourse)
for i in range(0,numcourse):
    print(infocourse[i],"\n")