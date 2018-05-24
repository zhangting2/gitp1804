'''
shuzi=1
while shuzi<=15:
    print('*'*shuzi)
    shuzi=shuzi+1
'''
a=1
while a<=9:
    b=1
    while b<=a:
        print('%d*%d=%d'%(b,a,a*b),end='\t')
        b=b+1
    print('')
    a=a+1
