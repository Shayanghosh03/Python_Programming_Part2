class Student:
    def __init__(self,name,math,physics,chemistry):
        self.name=name
        self.math=math
        self.physics=physics
        self.chemistry=chemistry
    def ave_marks(self):
        return ((self.math+self.physics+self.chemistry)/3)
s1=Student("Shayan Ghosh",90,87,95)
print(s1.name)
print(s1.math)
print(s1.physics)
print(s1.chemistry)
print(s1.ave_marks())