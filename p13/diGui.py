def jiecheng(a):
    i=1
    while a>=1:
        i*=a
        a=a-1
    return i
j=jiecheng(10)
print(j)

def f(a):
    if a>=1:
        b=a*f(a-1)
    else:
        b=1
    return b
ret=f(10)
print(ret)
