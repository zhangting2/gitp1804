d=open('2ts.txt','w')
d.write('江雪\n千山鸟飞绝\n万径人踪灭\n孤舟蓑里翁\n独钓寒江雪\n')
d.close()

d=open('2ts.txt','r+')
#c=d.read()
content=d.readlines()
#print(content)
for i in content:
    u=i[:-1]
    print(u+'*-*'+'\n')
d.close()

d1=open('2ts.txt','a')
#d1.write(c)
#d.close()
d1.close()


d2=open('2ts.txt','r+')
while True:
    cent=d2.readline()
    if cent=='':
        break
    print(cent)
    a=d2.tell()
    print('光标位置是：%d'% a)
t=d2.seek(5,0)
print(t)
d2.close()
