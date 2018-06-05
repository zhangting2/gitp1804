class species:
    def __init__(self,name,color,xieliang):
        self.name=name
        self.color=color
        self.xieliang=xieliang
    def sun(self):
        print('%s放阳光...颜色是%s'% (self.name,self.color))
        print('\n')
    def pea(self):
        print('%s持续发炮中...'% self.name)
        print('\n')
    def potato(self):
        print('%s持续变没中...'% self.name)
        print('\n')
    def mines(self):
        print('%s在等待僵尸，准备最终光荣牺牲'% self.name)
        print('\n')
    def shirenhua(self):
        print('%s在等待僵尸，吃掉僵尸'% self.name)
        print('\n')
    def jiangshi(self):
        print('%s在持续摇头中'% self.name)
        print('%s在持续行进中' % self.name)
        print('\n')
    def dead(self):
        print('%s死亡'% self.name)
        print('\n')
    def __str__(self):
        s='名字：'+self.name+'  颜色：'+self.color
        return s
xrk=species('向日葵','金黄色','满血')
#xrk.sun()
print(xrk)
xrk.sun()
wandou=species('豌豆射手','绿色','满血')
print(wandou)
wandou.pea()
dou=species('寒冰射手','蓝色','满血')
print(dou)
dou.pea()
tu=species('坚果','暗黄色','满血')
print(tu)
tu.potato()
di=species('地雷','土黄色','满血')
print(di)
di.mines()
shi=species('食人花','紫色','满血')
print(shi)
shi.shirenhua()
jiang=species('僵尸','黑色','满血')
print(jiang)
jiang.jiangshi()
jiang.dead()
