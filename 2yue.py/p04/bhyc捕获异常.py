#encoding=utf-8
'''
try:
    print(1)
    #print(nnn)
    print('%d'%'name')
except (NameError,SyntaxError,TypeError):
    print('有错')
else:
    print('没问题')
'''
try:
    a=input('输入文件名：')
    f=open(a,'r')
    b=f.read()
    print(b)
    f.close()
except Exception as result:
    print('捕获到啦异常')
    print('异常信息为：',result)
finally:
    f.close()
else:
    print('无异常')
print(f.closed)
