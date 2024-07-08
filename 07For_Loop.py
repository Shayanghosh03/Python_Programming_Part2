for number in [1, 2, 3, 5, 6, 10, 11, 12]: #List Method
    print(number,end="")
print()
list1=[]
for i in range(10,0,-1):
    list1.append(i**3)

print(list1)

if 124 in list1:
    print("Value Found")
else:
    print("Value Not Found")