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