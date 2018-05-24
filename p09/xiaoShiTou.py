'''
石头=1
剪刀=2
布=3
'''
while True:
    import random
    pc=random.randint(1,3)
    user=int(input('请出小拳拳：'))
    if user==1:
        print('我出的是石头')
    elif user==2:
        print('我出的是剪刀')
    elif user==3:
        print('我出的是布')
    else:
        print('不好意思，出错了')
    if pc==1:
        print('电脑出的是：石头')
    elif pc==2:
        print('电脑出的是：剪刀')
    else:
        print('电脑出的是：布')
    if (user==1 and pc==2) or (user==2 and pc==3) or (user==3 and pc==1):
        print('你赢啦，真棒')
    elif user==pc:
        print('平局，不服，再来')
    elif (user>3 or user<=0):
        print('重来，你出错啦')
    else:
        print('我赢啦，今个老百姓，真呀真高兴')

