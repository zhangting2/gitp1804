class Potato:
    def __init__(self):
        self.status='生土豆'
        self.lever=0
        self.tiaoliao=[]
    def cook(self,t):
        self.lever+=t
        if self.lever>=15:
            self.status='炒糊啦，变黑啦，冒烟啦，赶快跑啊'
        elif self.lever>=11:
            self.status='火太大了,炒焦啦'
        elif self.lever>=10:
            self.status='美味正好出锅，真香'
        elif self.lever>=5:
            self.status='半生不熟中'
        else:
            self.status='生土豆'
    def Addtiaoliao(self,tiaoliao):
        self.tiaoliao.append(tiaoliao)
    def __str__(self):
        for i in self.tiaoliao:
            self.status+= i + ','
        return('当前土豆状态是：%s , 炒土豆一共使用了%d分钟时间'% (self.status,self.lever))
td1=Potato()
td1.cook(6)
print(td1)
td1.cook(4)
print(td1)
td1.Addtiaoliao('辣椒粉')
td1.Addtiaoliao('盐')
td1.Addtiaoliao('胡椒粉')
td1.Addtiaoliao('鸡精')
print(td1)


