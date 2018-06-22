class JiangShi:
    def __init__(self,name,color,ph,wuqi):
        self.name=name
        self.color=color
        self.ph=ph
        self.wuqi=wuqi
    def __str__(self):
        s=self.color+"的"+self.name+'  血量是'+self.ph+'   武器是'+self.wuqi
        return s
    def run(self):
        print('%s正在缓慢行进中'% self.name)
    def yao(self):
        print('%s正在缓慢撕咬中'% self.name)
    def pao(self):
        print('%s正在奔跑中'% self.name)
    def Kh(self):
        print('%s 进入狂化模式，持续奔跑中'% self.name )
def lj(item):
    item.run()
    item.yao()
xhh=JiangShi('普通僵尸','灰色','100','嘴巴')
print(xhh)
lj(xhh)
print('___________________________________________')
print('\n')
xhh.run()
xb=JiangShi('铁桶僵尸','黑色','90','铁桶')
print(xb)
lj(xb)
xb.Kh()

print('>'*43)

class Xrk:
    def __init__(self,name,color,ph):
        self.name=name
        self.color=color
        self.ph=ph
    def __str__(self):
        s = self.color+'的'+self.name+"  血量为："+self.ph
        return s
    def sun(self):
        print('%s 正在努力里放阳光中...'% self.name)
yg=Xrk('向日葵','金黄色','100')
print(yg)
yg.sun()
