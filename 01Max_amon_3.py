a=int(input("Enter 1st Number: "))
b=int(input("Enter 2nd Number: "))
c=int(input("Enter 3rd Number: "))
if(a>b):
    max=a
else:
    max=b
if(c>max):
    max=c
print("Max=",max)