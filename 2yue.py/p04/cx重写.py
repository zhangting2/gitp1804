class Father(object):
    def __init__(self,name):
        self.xing=name
    def kaiche(self):
        print('司机')
class Son(Father):
    def __init__(self,name):
        #Father.__init__(self,name)
        #super(Son,self).__init__(name)
        super().__init__(name)
    def kaiche(self):
        super().kaiche()
dd=Son('小灰灰')
print(dd.xing)
dd.kaiche()
