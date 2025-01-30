class Student:
    def __init__(self): #Default Constructure
        pass
    
    def __init__(self,name,marks): #Parameterized Constructure
        self.name=name
        self.marks=marks

s1=Student("Shayan Ghosh",95)
print(s1.name)
print(s1.marks)