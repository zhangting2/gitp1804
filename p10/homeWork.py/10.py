a=46
for i in range(1,101,10):
    i=int(input('请输入1--100内的数字'))
    if i==46:
        print('恭喜你，猜中了，请为大家表演个节目')
        break
    elif i<46:
        print('抱歉，猜小啦')
    else:
        print('猜大了')
if a != i:
    print('你真笨')



