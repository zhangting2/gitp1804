name_list=[]
while True:
    name=input('请输入名字：')
    name_list.append(name)
    if name=='q':
        break
print(name_list)
print('第三个下标字符为:%s '% name_list[3])
print('第五个下标字符为:%s '% name_list[5])
print('第八个下标字符为:%s '% name_list[8])
print('第十个下标字符为:%s '% name_list[10])
name_list.sort()
print(name_list)
name_list.reverse()
print(name_list)
name_list.pop()
print(name_list)
del name_list[8]
print(name_list)
n=[1,2,3,4,5,6,7,8]
name_list.extend(n)
print(name_list)
print('小明所处位置：%d' % name_list.index('小明'))


