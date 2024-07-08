odd_squre=[x**2 for x in range(1,11) if  x%2==1]
print(odd_squre)

# For understanding, above generation is same as.
odd_squre=[]
for x in range(1,11):
    if x % 2 ==1:
        odd_squre.append(x**2)
print(odd_squre)

output=[]
for x in range(1,20):
    if x%2==0 or x%3==0:
       output.append(x)
print(output)

print()

list1=[i for i in range(1,21) if(i%2==0) or (i%3==0)]
print(list1)

print()

list=[1,20,30,40,30,40,5,6,48,95]
count=0
x=int(input("Enter a Value: "))
count=list.count(x)
if(count!=0):
    print(x,"Found",count,"times")
else:
    print(x,"not found in the list")

print()

list=[]

list1=[1,2,3,4,5,6,7,8,9,10]
elist=list()
olist=[]
for x in list1:
    if(x%2==0):
        elist.append(x)
    else:
        olist.append(x)
print(list1)
print(elist)
print(olist)