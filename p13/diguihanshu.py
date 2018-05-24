def diguihanshu(n):
    if n >= 1:
        s = n*diguihanshu(n-1)
    else:
        s = 1
        return(s)
    return(s)
print(diguihanshu(10))

