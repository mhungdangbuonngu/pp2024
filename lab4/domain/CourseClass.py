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