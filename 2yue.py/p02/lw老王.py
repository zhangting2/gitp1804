class Qiang:
    def __init__(self,name):
        self.name = name
        self.danjia = None
    def __str__(self):
        if self.danjia:
            return "枪当前有弹夹"
        else:
            return "枪当前没有弹夹"
    def lianjiedanjia(self,danjia):
        if not self.danjia:
            self.danjia = danjia
    def she(self,diren):
        zidan = self.danjia.chuzidan()
        if zidan:
            zidan.shanghai(diren)
    else:
        print("没子弹了,没有伤害")

class People:
        def __init__(self,name):
        self.name = name
        self.xue = 100
        self.qiang = None
    def andanjia(self,qiang,danjia):
        qiang.lianjiedanjia(danjia)
    def naqiang(self,qiang):
        self.qiang = qiang
    def anzidan(self,danjia,zidan):
        danjia.baocunzidan(zidan)
    def kaiqiang(self,diren):
        self.qiang.she(diren)
    def diaoxue(self,shashangli):
        self.xue -= shashangli
                                                                                                                                       def __str__(self):
                                                                                                                                                    return self.name+"剩余血量为:" + str(self.xue)
                                                                                                                                                    def dun(self):
                                                                                                                                                                 print("%s蹲下躲过了攻击." % self.name)
                                                                                                                                                                           def miao(self):
                                                                                                                                                                                        print("%s拿起 %s 瞄准了敌人" % (self.name,self.qiang))
                                                                                                                                                                                             def death(self):
                                                                                                                                                                                                          print("%s 血槽已空,吾已战死沙场." % self.name)
                                                                                                                                                                                                               def bisha(self):
                                                                                                                                                                                                                            print("%s 能量已满,开启必杀,天星爆." % self.name)

