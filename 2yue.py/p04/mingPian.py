list_Ming=[]
class MP(object):

    def mingPian(self):
        print('*'*30)
        print('欢迎使用【名片管理系统】V1.0')
        print('1.新建名片')
        print('2.显示全部')
        print('3.查询名片')
        print('4.删除名片')
        print('5.退出系统')
        print('*'*30)

    def new(self):
        print('*'*30)
        print('开始新建名片')
        name=input('请输入姓名：')
        com=input('请输入公司:')
        zhiwu=input('请输入职务：')
        phone=input('请输入电话号码：')
        email=input('请输入电子邮箱：')
        dic={'name':name,
             'com':com,
             'zhiwu':zhiwu,
             'phone':phone,
             'email':email}
        list_Ming.append(dic)
        print(list_Ming)
        print('成功添加%s的名片'%dic['name'])
    def sall(self):
        print('*'*30)
        print('功能：查询全部名片')
        if len(list_Ming) == 0:
            print("提示：没有任何名片记录")
        for dic in list_Ming:
            print(dic)
    def sOne(self):
        print('*'*30)
        print('查询一个名片')
        s=input('请输入要查询的名字？')
        for i in list_Ming:
            if s== i['name']:
                print('*'*33)
                print('姓名：%s'% i['name'])
                print('公司：%s'% i['com'])
                print('职务：%s'% i['zhiwu'])
                print('电话：%s'% i['phone'])
                print('电子邮箱：%s'% i['email'])
    def delM(self):
        print('*'*30)
        i=input('确定要删除名片吗？确定请输yes  ')
        if i=='yes':
            print('')
        else:
            print('^-^强制删除')
        d=int(input('你要删除第几个名片'))
        d=d-1
        del list_Ming[d]
        print('您已成功删除,请查看',list_Ming)
    def exit(self):
        print('成功退出系统')

    #mingPian()
    def fangfa(self):
        while True:
            shu=int(input('请输入你要操作的数字：'))
            if shu==1:
                self.new()
            elif shu==2:
                self.sall()
            elif shu==3:
                self.sOne()
            elif shu==4:
                self.delM()
            elif shu==6:
                self.mingPian()
            else:
                exit()
                break
mm=MP()
mm.fangfa()

