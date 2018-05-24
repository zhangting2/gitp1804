def jia(x,y):
    return(x+y)
def jian(x,y):
    return(x-y)
def cheng(x,y):
    return(x*y)
def chu(x,y):
    return(x/y)
print('欢迎使用笨蛋计算机^-^')
a=int(input('请输入数字：'))
while True:
    b=input('请输入符号（+、-、*、/）：')
    c=int(input('请输入数字：'))
    if b=='+':
        a=jia(a,c)
        print(a)
    elif b=='-':
        a=jian(a,c)
        print(a)
    elif b=='*':
        a=cheng(a,c)
        print(a)
    elif b=='/':
        a=chu(a,c)
        print(a)
    else:
        print('你好像出错了，在仔细检查检查。')
        if a=='q' or b=='q' or c=='q':
            break
