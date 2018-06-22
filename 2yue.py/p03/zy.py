#!/usr/bin/env python
# coding=utf-8
import time
class BanJi:
    student = []
    br = '习大大'
    bh = 1804
'''
def __init__(self,br,bh):
self.br = br
self.bh = bh
'''
    def __get_Bc(self):
    print ('班级详情信息')
    print (self.bh)
    print ('班主任：%s'%(self.br))
    for i in self.student:
    b1 = '姓名：%s 性别：%s 年龄：%d'%(i['姓名:'],i['性别:'],i['年龄:'])
    print (b1)

    def __str__(self):
    return str(self.__get_Bc())
#_____________________________________
class Student(BanJi):
    grade = []
    def __init__(self,name,sex,age):

    self.name = name
    self.sex = sex
    self.age = age
    self.dic1 = {}
    def add_Grade(self):
    print (self.grade)
    def Cx(self,n): #学生成绩查询
    self.name = n
    for i in self.grade:
    if self.name == i['姓名']:
    print ('成绩详情信息')
    print (i['英语'])
    print ('姓名：%s\n成绩＊＊＊\n语文:%d\n数学:%d\n英语:%d'%(i['姓名'],i['语文'],i['数学'],i['英语']))
    def C_stu(self): #把学生信息追加到Student
    self.dic1 = {'姓名:':self.name,'性别:':self.sex,'年龄:':self.age}
    self.student.append(self.dic1)
#_____________________________________
class Grade(Student):
    def __init__(self,name,yw,sx,yy):
    self.yw= yw
    self.sx= sx
    self.yy= yy
    self.cname = None
    self.name = name
    self.dic = {}
    def __get_Cx(self):
    for i in self.grade:
        a = i[self.cname]
        b = i['姓名']
        print ( '姓名:%s %s : %d'%(b,self.cname,a)) #此时的显示的是成绩单

    def Jgrade(self):
    self.dic = {'姓名':self.name,'语文':self.yw,'数学':self.sx,'英语':self.yy}
    self.grade.append(self.dic)

    def set_Cx(self,n): #此时输入的ｎ是要查询什么程序的科目
    self.cname = n
    self.__get_Cx()
    def Cq (self): #查询全部成绩的方法
    print (' ------学生成绩单------')
    for i in self.grade:
    print ('姓名：%s　　语文:%d　　数学:%d　　英语:%d'%(i['姓名'],i['语文'],i['数学'],i['英语']))

    def __str__(self):
    return str(self.Cq())
#对象_______________________________________
小王= Student('小王','男',18)
小王.C_stu()
小王= G
