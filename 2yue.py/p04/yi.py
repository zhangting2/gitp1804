__all__=['add','jian']
def jian(a,b):
    return a-b

def add(a,b):
    return a+b

print(__name__)
if __name__=='__main__':
    s=add(1,5)
    print('测试结果:%d ' % s)
