import sys
class People:
    def __init__(self,name):
        self.name=name

xhh=People('家具')
xhh1=xhh
xhh2=xhh
print(sys.getrefcount(xhh))
print(isinstance(xhh,People))
