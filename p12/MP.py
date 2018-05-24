def MP():
    print('*'*35)
    print('欢迎使用【名片管理系统】V1.0')
    print('1. 新建名片')
    print('2. 显示全部')
    print('3. 查询名片')
    print('4. 删除名片')
    print('5. 退出系统')
    print('*'*35)
MP()
MPM[]
def one():
    print('新建名片')
    name=input('请输入名字：')
    com=input('请输入公司：')
    zhiwu=input('请输入职务：')
    phone=input('请输入电话：')
    email=input('请输入电子邮箱：')
    dic={'name':name,'com':com,'zhiwu':zhiwu,'phone':phone,'email':email}
    MPM.append(dic)
    print(MPM)
def two():
    print('要显示全部吗')
def three():
    print('要显示一个名片吗')
def four():
    print('要删除名片吗')
def five():
    print('要退出吗')

u=int(input('请输入要操作的数字：'))
while True:
    if u==1:
        one()
    elif u==2:
        two()
    elif u==3:
        three()
    elif u==4:
        four()
    elif u==5:
        five()
