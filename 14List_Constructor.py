list1=list()
print("Enter The Values for the List")
print()
for i in range(5):
    list1.append(int(input("Enter Value ")))

key=int(input("Enter the Number to Search"))
if key in list1 :
    print(key," Found in the list")
else:
    print(key ," Not found")