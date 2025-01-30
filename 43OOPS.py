class Student: #Class
    def __init__(self):  #Constructure
        pass

    def __init__(self,name,marks): #parametarice Constructure
        self.name=name
        self.marks=marks
    
    @staticmethod #decorator
    def hello(): #Static Method
        print("Hello")

    def avg_marks(self): #Method
        sum=0
        c=0
        for item in self.marks:
            sum+=item
            c+=1
        return (sum/c)
    
s1=Student("Shayan Ghosh",[98,93,85]) #Object
print(s1.name)
print(s1.marks)
print(s1.avg_marks())
s1.hello()