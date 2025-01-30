class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def avg_marks(self): #Methos
        sum=0
        c=0
        for item in self.marks:
            sum+=item
            c+=1
        return (sum/c)
s1=Student("Shayan Ghsoh",[90,56,89])
print(s1.name)
print(s1.marks)
print(s1.name,"Your average marks is",s1.avg_marks())

s1.name="Sumanta Ghosh"
print(s1.name,"Your average marks is",s1.avg_marks())