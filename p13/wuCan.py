
def test():
    print('大家好')
def test1(a):
    print('*'*30)
    print(a)
b=1
def test2(*a):
    global b
    for i in a:
        b=i*b
    print(b)
test2(1,2,3,4,5,6)
test2(23,44,45)

'''
a=2
b=[3,6,'t','q']
dic={'a','n','gd',5}
test()
test1(a)
test2(dic,b)
'''

