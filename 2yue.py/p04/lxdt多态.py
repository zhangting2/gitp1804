class Car(object):
    def __init__(self,name):
        self.name=name
    def Run(self):
        return('%s汽车飞奔中'% self.name)
class DaZhong(Car):
    def Run(self):
        return('%s汽车飞奔中'% self.name)
class BaoMa(Car):
    def Run(self):
        return('%s汽车飞奔中'% self.name)
class BenChi(Car):
    def Run(self):
        return('%s汽车飞奔中'% self.name)
class People(object):
    def __init__(self,name):
        self.name=name
#    def Kai(self):
 #       print('%s开%s车'% (self.name,self.name))
    def kai(self,n):
        print('%s开%s车去追刘美娜,%s'% (self.name,n.name,n.Run()))
benchi=BenChi('奔驰')
man=People('司机')
man.kai(benchi)
ff=BaoMa('法拉利')
ren=People('高富帅')
ren.kai(ff)
a=BaoMa('兰博基尼')
r=People('富二代')
r.kai(a)


