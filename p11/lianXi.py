a=1
while a<=9:
    b=1
    while b<=a:
        print('%d*%d=%d'%(b,a,a*b),end='\t')
        b=b+1
    print('')
    a=a+1
