tul=(1,2,3)
for i in tul:
    print(i)
while True:
    print(tul[0])
    print(tul[1])
    print(tul[2])
    break

def tul(*a):
    for i in a:
        for c in i:
            print(c)
q=(1,2,3)
w=(4,5,6)
e=(7,8,9)
tul(q,w,e)
'''
while True:
    tul(q,w,e)
    print(tul)
    break
'''

liebiao=[{'name':'邵广超','age':22,'sex':'男'},
         {'name':'小布什','age':18,'sex':'女'},
         {'name':'金正恩','age':23,'sex':'女'}]
for i in liebiao:
    if name==i['name']:
        print('*'*30)
        print('姓名：%s'% i['name'])
        print('年龄：%d'% i['age'])
        print('性别：%s'% i['sex'])
