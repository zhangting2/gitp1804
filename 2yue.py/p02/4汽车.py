class Car:
    def __init__(self,name,lunzi,color):
        self.name=name
        self.lunzi=lunzi
        self.color=color
    def run(self):
        print('%s的%s %d轮跑'% (self.color,self.name,self.lunzi))
    def call(self):
        print('%s的发动机已经急不可耐的吼叫'% self.name)
    def zhuiwei(self):
        print('%s 选中目标，准备追尾'% self.name)
    def __str__(self):
        s='车的名字是：'+self.name+'车的颜色是：'+self.color
        return s
baoma=Car('宝马',4,'红色')
print('汽车名称',baoma)
baoma.run()
baoma.call()
fute=Car('福特',4,'白色')
fute.run()
fute.zhuiwei()
aodi=Car('奥迪',4,'黑色')
aodi.run()
aodi.call()
aa=Car('李舒静',2,'黑色')
aa.run()
aa.call()
aa.zhuiwei()
