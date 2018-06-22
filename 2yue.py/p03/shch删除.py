class People:
    def __init__(self,name):
        self.name=name
    def set_name(self):
        f=open('name.txt','r')
        c=f.read()
        if c!='':
            return c
        else:
            print('请设置内容')
        f.close()
    def get_name(self):
        f=open('name.txt','w')
        f.write(self.name)
        f.close()

    def __del__(self):
        print(xhh.get_name())
        print('--------已销毁--------')
xhh=People('小南')
xhh.set_name()
