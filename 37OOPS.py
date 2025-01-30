class Student:
    def __init__(self,name,marks,grade): #Constructure
        self.name=name #attributes
        self.marks=marks
        self.grade=grade
        print("Creating new student")
        print(self)
s1=Student("Shayan",80,'A')
print(s1)
print(s1.name)
print(s1.marks)
print(s1.grade)

s2=Student("Sumanta",95,"A+")
print(s2)
print(s2.name)
print(s2.marks)
print(s2.grade)