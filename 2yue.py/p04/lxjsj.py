class JiSuanQi(object):
    __danli=None
    __name=True
    def __init__(self,name):
        if JiSuanQi.__name==True:
            self.name=name
            JiSuanQi.__name=False
    def __new__(cls,k):
        if cls.__danli==None:
            cls.__danli=object.__new__(cls)
        return cls.__danli
    def JiSuan(self):
        a=float(input('请输入数字：'))
        while True:
            b=input('请输入符号- + × /:')
            c=float(input('请输入数字：'))
            if b=='+':
                a=a+c
                print('结果为%2f'% a)
            elif b=='-':
                a=a-c
                print('结果为%2f'% a)
            elif b=='*':
                a=a*c
                print('结果为%2f'% a)
            elif b=='/':
                a=a/c
                print('结果为%2f'% a)
            #elif b!='+'or b!='-'or b!='*'or b!='/':
            else:
                print('出错了，请再次输入')
                b=input('请输入符号- + × /:')
                c=float(input('请输入数字：'))
            d=int(input('选择1.继续操作 2.退出  '))
            if d==2 :
                break

try:
    a=JiSuanQi('计算器')
    print(a.name)
    a.JiSuan()
except Exception as result:
        print('异常为：%s'% result)





