class People:
    def __init__(self,name,age):
        self.__name=name
        self.age=age
    def get_name(self):
        return self.__name
    def set_name(self,n):
        self.__name=n
        return self.__name
    def __send_msg(self):
        print('发送成功')
    def get_msg(self,n):
        if n==0:
            print('白冰')
        else:
            self.__send_msg()
xiaohua=People('笑话','6000')
#print(xiaohua.get_name())
#print(xiaohua.set_name('开心'))
#xiaohua.__send_msg()
#xiaohua.get_msg('jj')
#a=xiaohua.get_name()
#print(a)
