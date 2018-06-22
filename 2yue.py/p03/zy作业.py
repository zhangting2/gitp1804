class Class:
    def __init__(self,teacher,classnumber):
        self.student=[]
        self.teacher=teacher
        self.classnumber=classnumber
    def __str__(self):
        return ('班级编号是:%d\n 班主任是：%s \n'% (self.classnumber,self.teacher))

class Student:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        self.chengji={}
    def add_per(self,k,v):
        self.dper[k]=v
        return self.dper
    def __str__(self):




class Chengji:
    def __init__(self,yuwen,shuxue,english):


