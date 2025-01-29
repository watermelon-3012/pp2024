
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