x=4
for i in range(4,0,-1):
    k=x
    for j in range(1,i+1):
        print(k,end=" ")
        k=k-1
    x=x-1
    print()