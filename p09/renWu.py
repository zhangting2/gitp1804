a=1
while a<=3:
    if a == 1:
        print('签到')
    elif a ==2:
        print('吃饭')
        b=1
        while b<=3:
            print('睡觉%d次'% b)
            b=b+1
    else:
        print('结束')
    a=a+1
