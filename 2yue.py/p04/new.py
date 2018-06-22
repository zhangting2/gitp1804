class Car(object):
    __instace=None   #用于保存实例化对象
    __init_flag=True    #表示init一次都没有执行
    def __init__(self,name):
        if Car.__init_flag==True:
            self.name=name
            Car.__init_flag=False  #标记已经执行一次，以后不要再执行

    def __new__(cls,*k):
        #print(id(cls))
        print('new')
        if cls.__instace==None:  #第一次创建实例对象
            cls.__instace=object.__new__(cls)
        return cls.__instace   #将对象的引用传递到init中
c1=Car('baoma')
print(c1.name)
c2=Car('benchi')
print(c2.name)
print(id(c1))
print(id(c2))
#print(a)
#print(id(Car))
