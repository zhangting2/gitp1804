class Father(object):
    def __init__(self):
        self.xing='张'
        self.__height='155'
    def kaiche(self):
        print('司机')
    def __dubo(self):
        print('赌博')
    def get_dubo(self):
        return self.__dubo()
class Son(Father):
    def kaiche(self):
        print('好司机')


dd=Son()
dd.xing='纳兰'
print(dd.xing)
dd.height='180'
print(dd.height)
dd.get_dubo()
dd.kaiche()
