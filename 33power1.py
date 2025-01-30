def fun(b,e):
    if(e>0):
        return b*fun(b,e-1)
    else:
        return 1
power=fun(2,3)
print(power)