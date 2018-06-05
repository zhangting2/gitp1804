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
xhh=JiangShi('普通僵尸','灰色','100','嘴巴')
print(xhh)
xhh.run()
xhh.yao()

