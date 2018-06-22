class js(object):
    __danli=True
    __name=True
    def __init__(self,name):
        if js.__name==True:
            self.name=name
            js.__name=False

    def __new__(cls,k):
        if js.__danli==True:
            cls.a=object.__new__(cls)
        return cls.a
    def jia(self,x,y):
        return x+y
    def jian(self,x,y):
        return x-y
    def cheng(self,x,y):
        return x*y
    def chu(self,x,y):
        return x/y
class jisuan(js):
    def suan(self,a,b,fuhao):
        if fuhao=='+':
            return super().add(a,b)
        elif fuhao=='-':
            return super().jian(a,b)
        elif fuhao=='*':
            return super().cheng(a,b)
        elif fuhao=='/':
            return super().chu(a,b)
shu=jisuan('计算机')
try:
    a=float(input('请输入数字：'))
    c=input('请输入符号 + - * / ：')
    b=float(input('请输入数字：'))

    s=shu.suan(a,b,c)
    print(s)
except Exception as err:
    print('计算有错：%s'% err)

