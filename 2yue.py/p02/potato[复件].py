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
        self.s='调料是'
        for i in self.tiaoliao:
            self.s+= i + ','
        return('当前土豆状态是：%s , %s炒土豆一共使用了%d分钟时间'% (self.status,self.s,self.lever))
td2=Potato()
while True:
    t=int(input('请输入时间:  退出为00 :'))
    td2.cook(t)
    print(td2)
    if t==00:
        break
while True:
    l=input('请输入调料：')
    if l=='00':
        break
    td2.Addtiaoliao(l)
    td2.cook(t)
    print(td2)
print(td2)



'''
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
'''

