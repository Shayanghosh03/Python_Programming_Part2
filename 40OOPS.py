class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("Welcome Student")

    def getmarks(self):
        return self.marks
s1=Student("Shayan",80)
s1.welcome()
print(s1.name)
print(s1.getmarks())