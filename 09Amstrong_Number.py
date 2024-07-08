n=int(input("Enter a Number: "))
temp=n
s=0
while temp!=0 :
    r=temp % 10
    s=s+r**3
    temp=temp//10
if(s==n):
    print("Armstrong")
else :
    print("Not a Armstrong")

            
            