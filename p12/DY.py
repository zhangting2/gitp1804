'''
def hh():
    print('*'*22)

def xx():
    print('$'*22)
    print('你真帅')

a=3
b=4
c=8
d=a+b+c
def ss():
    print(d)
    return d
ss()
'''
'''
#定义函数
def ss(a,b,c):
    #返回函数值
    return a+b+c
#定义函数
def average(x,y,z):
    #调用ss函数
    s=ss(x,y,z)
    #用调用的函数进行再次计算，然后返回函数值
    return s/3
#调用ss函数，并打印
s=ss(3,4,5)
print(s)
#调用average函数，并打印
b=average(2,2,2)
print(b)
''

'
