list=['s',2,6,3,'zz']
a=111
def test1():
    global a
    a+=1
    list[2]='hao'
    list.append('0000')
    print(list)
    print(a)
def test2():
    print(a)
test2()
test1()
