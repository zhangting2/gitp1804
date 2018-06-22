class Car:
    def __init__(self,name,lunzi,color):
        self.name=name
        self.lunzi=lunzi
        self.color=color
        self.time='新车'
        self.num=0
        self.weixiu=[]
    def year(self,y):
        self.num+=y
        if self.num >= 10:
            print('对不起，您的宝贝%s该退休了'% self.naem)
        elif self.num>=5:
            self.time=print('您的%s只需经过维修，风采不减当年'% self.name)
        elif self.num>=3:
            print('%s经过保养会行驶的更加平稳，漂移都不怕'% self.name)
        else:
            print('%仍跟刚买时一样，爱惜的很好')
    def Weixiu(self,weixiu):
        self.weixiu.append(weixiu)
    def __str__(self):
        self.t=''
        for i in self.weixiu:
            self.t=i+','
        self.t=self.t.strip(',')
        return('%s的状态是:%s,年限是：%s年，维修部件:%s'% (self.name,self.time,self.num,self.t))
    def run(self):
        print('%s的%s %d轮跑'% (self.color,self.name,self.lunzi))
    def call(self):
        print('%s的发动机已经急不可耐的吼叫'% self.name)
    def zhuiwei(self):
        print('%s 选中目标，准备追尾'% self.name)
#    def __str__(self):
 #       s='车的名字是：'+self.name+'车的颜色是：'+self.color
  #      return s
def quan(item):
    item.run()
    item.call()
    item.zhuiwei()
print('>'*44)
baoma=Car('宝马',4,'红色')
print('汽车名称',baoma)
quan(baoma)
print(baoma.t)
baoma.year(6)
print(baoma.t)
print(baoma)
print('\n')
'''
fute=Car('福特',4,'白色')
fute.run()
fute.zhuiwei()
print('\n')
aodi=Car('奥迪',4,'黑色')
aodi.run()
aodi.call()
print('\n')
aa=Car('李舒静',2,'黑色')
quan(aa)
'''
