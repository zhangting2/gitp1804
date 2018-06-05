class People:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def jump(self):
        print('我%s又来了，快吃我%s一脚'%(self.name,self.name))
    def zhiquan(self):
        print('快吃我%s一拳'% (self.name))
    def __str__(self):
        s='名字:'+self.name+'  衣服颜色：'+self.color
        return s
def Jueji(item):
    item.jump()
    item.zhiquan()
quanhuang=People('拳皇','红色')
print(quanhuang)
#quanhuang.jump()
Jueji(quanhuang)
xhh=People('大牛','黑色')
print(xhh)
xhh.zhiquan()
o=People('小猪','白色')
print(o)
o.zhiquan()
u=People('小阳','蓝色')
print(u)
u.jump()
p=People('小白','灰色')
print(p)
p.jump()
