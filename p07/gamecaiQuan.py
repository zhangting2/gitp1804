#-*- coding:utf-8 -*-

shitou='石头'
bu='布'
jiandao='剪刀'

import random
userInput='o'
while userInput=='o':
    pc=random.randint(1,3)
   # user=int(input('请问用户你要出什么'))
    user=input("我出：")
    if user=='t':
        userInput='t'
    '''
    if user==1:
        print('我出的是：石头')
    elif user==2:
        print('我出的是：布')
    elif user==3:
        print('我出的是：剪刀')
    else:
        print('出错了')
        '''
    if pc==1:
        pcStr=shitou
        print('电脑出的是：石头')
    elif pc==2:
        pcStr=bu
        print('电脑出的是：布')
    else:
        pcStr=jiandao
        print('电脑出的是：剪刀')
    #if user > 0 and user <=3:
        if (user==shitou and pcStr==jiandao) or (user==bu and pcStr==shitou) or (user==jiandao and pcStr==bu):
            print('你赢啦,你厉害')
        elif user==pcStr:
            print('平局，再来')
       # elif (user!=shitou or user!=bu or user!=jiandao):
        #    print('重来，你出错了，不算')
        else:
            print('不好意思，我赢啦')
