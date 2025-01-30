str1=input("Enter a String: ")
print("Original String: ",str1)
str="aeioua"
for i in range(len(str1)):
    if(str1[i] in str):
        for j in range(len(str)):
            if(str1[i]==str[j]):
                print(str[j+1],end="")
                break
    else:
        print(str1[i],end="")