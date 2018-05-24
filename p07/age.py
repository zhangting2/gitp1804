#-*- coding:utf-8 -*-
while True
    age=int(input("请输入年龄"))
    if age<=10 and age>=1:
        print('幼年')
    elif age<=20 and age>10:
        print('青年')
    elif age<=30 and age>20:
        print('成年')
    elif age<=40 and age>30:
        print('中年')
    elif age<=60 and age>40:
        print('中老年')
    elif age<=80 and age>60:
        print('老年')
    else:
        print('古稀')

