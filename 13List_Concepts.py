list1=[10,20,30]
print(list1)
print("list1[2]=",list1[2])
print("list1[-1]=",list1[-1])
print("list1[-3]=",list1[-3])
list1.append(40)
print("After append 40")
print(list1)
list1.extend([50,60,70])
print("After extend [50,60,70]")
print(list1)
list1[2]="Thirty"
print("After Modifing 3rd Position")
print(list1)