class Student:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
        self.chengji={}
    def Addchengji(self,k,v):
        self.chengji[k]=v
    def Cj(a):
        for i in range(1,4):
            k=input('请输入科目：')
            v=input('请输入成绩：')
            a.Addchengji(k,v)
    def __str__(self):
        return '姓名:'+str(self.name)+'\n'+'性别:'+str(self.sex)+'\n'+'年龄:'+str(self.age)+'\n'+'成绩:'+str(self.chengji)

xiaoming=Student('小明','男',12)
xhh=Student('小灰灰','男',33)
xiaoming.Cj()
cj=print(xiaoming)
f=open('cj.txt','w')
f.write(str(xiaoming))
f.close()
