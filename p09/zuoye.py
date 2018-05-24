#-*- coding:utf-8 -*-
account=input('请输入帐号：')
passwd=input('请输入密码：')
name=input('请输入姓名：')
money=20000
print('总金额为：%d'%money)
amount=int(input('请输入要取的钱数'))
balance=money-amount
print('帐号是：%s\n密码：%s\n姓名：%s\n总金额：%d\n取的钱数:%d\n余额：%d\n'%(account,passwd,name,money,amount,balance))
