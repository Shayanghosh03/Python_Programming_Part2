class Student:
    college_name="AIEM" #Class Attributes
    name="Anonymous"
    def __init__(self,name):
        self.name=name #Object Attributes

s1=Student("Shayan")
s2=Student("Sumanta")

print(s1.name)
print(s2.name)

print(Student.college_name)
print(Student.name)