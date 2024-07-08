n=int(input("Enter a Number: "))
temp=n
b=0
while temp!=0:
    r=temp%10
    b=b*10+r
    temp=temp//10
if(b==n):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number") 