class House:
    def __init__(self,area,addr):
        self.area=area
        self.addr=addr
        self.jj=[]
    def __str__(self):
        return ('房子的空间为：%s,地址为：%s,其中包含的家具有：%s'% (self.area,self.addr,self.jj))
    def add_jj(self,item):
        if self.area>item.size:
            self.area -=item.size
            self.jj.append(item.type1)
        else:
            print('房子太小，容纳不了这尊大佛')
class Light:
    def __init__(self,name,color,size,form):
        self.name=name
        self.color=color
        self.size=size
        self.form=form
    def __str__(self):
        return ('%s已经准备好啦，他的颜色是%s'% (self.name,self.color))



class Bed:
    def __init__(self,size,type1):
        self.size=size
        self.type1=type1
    def __str__(self):
        return ('床的类型是%s,床的大小是%s'% (self.type1,self.size))
class People:
    def __init__(self,name):
        self.name=name
    def get_Rates(self,rates):
        if rates=='父亲':
            return 100000
        elif rates=='朋友':
            return 200000
        elif rates=='媳妇':
            return 300000
        elif rates=='亲戚':
            return 10000000
        else:
            return 0


house1=House(200,'八大胡同')
print(house1)
baby_bed=Bed(100,'婴儿床')
print(baby_bed)
print(house1)
house1.add_jj(baby_bed)
print(house1)
big_bed=Bed(200,'巨床')
house1.add_jj(big_bed)
print(house1)
LED=Light('LED','白色','灯泡','椭圆')
print(LED)
while True:
    switch=input('请输入开灯还是关灯：')
    if switch=='开灯':
        print('您已执行操作')
    if switch=='关灯':
        print('您已关灯')
        break
    else:
        print('请节约用电')
while True:
    rates=input('想知道我张三的房价，先报出身份：')
    if rates=='q':
        print('无可奉告')
        break
    print('张三的房价是：%d'% get_Rates(rates))
