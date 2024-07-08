n=int(input("Enter a Number"))
for i in range(2,n):
    if(n % i ==0):
        break
if(i+1==n):
    print("Prime")
else:
    print("Not Prime")