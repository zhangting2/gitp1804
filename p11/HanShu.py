'''
def hanSu(a,b):
    print('a=%d'% a)
    print('b=%d'% b)
    sum=a+b
    x=a*b
    less=a-b
    ex=a/b
    yu=a%b
    print(sum)
    print(x)
    print(less)
    print(ex)
    print(yu)

hanSu(a=20,b=3)
'''
def jia(x,y):
    return(x+y)
def jian(x,y):
    return(x-y)
def cheng(x,y):
    return(x*y)
def chu(x,y):
    return(x/y)
print('欢迎使用计算机')
a=int(input('请输入第一个数字：'))
while True:
    fuhao=input('请输入符号 + - * / ：')
    s=1
    while s<=3 and fuhao != '+' and fuhao!='-'and fuhao!='*'and fuhao!='/':
        fuhao=input('出错啦，请重输')
    s=s+1
            break
    b=int(input('请输入第二个数字：'))
    if a=='q' or fuhao=='q' or b=='q':
        break
    if fuhao=='+':
        a=jia(a,b)
        print(a)
    elif fuhao=='-':
        a=jian(a,b)
        print(a)
    elif fuhao=='*':
        a=cheng(a,b)
        print(a)
    elif fuhao=='/':
        a=chu(a,b)
        print(a)


