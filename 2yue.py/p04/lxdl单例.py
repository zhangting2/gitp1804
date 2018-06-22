class girlfriend(object):
    __danli=None
    __init_name=False
    def __init__(self,name):
        if self.__init_name==False:
            self.name=name
            self.__init_name=True
    def __new__(cls,*k):
        if cls.__danli==None:
            cls.__danli=object.__new__(cls)
        return cls.__danli
n1=girlfriend('hh')
print(n1.name)
n2=girlfriend('oo')
print(n2.name)

