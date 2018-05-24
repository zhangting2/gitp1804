'''
dic={'name':'zhangsan','school':'beida','high':1.7,'sex':'nan','phone':13527}#创建一个字典
print(dic['name'])#根据key找value
dic.get('name')#同上，唯一区别：没有‘name’会报错
k_list=dic.keys()#给dic.keys设个变量
print(dic.keys())#直接输出dic的key
print(k_list)#同上，输出变量
v_list=dic.values()#给dic.value设个变量
print(dic.values())#直接输出dic的value
print(v_list)#同上， 输出变量
kv_list=dic.items()#
print(dic.items())
print(kv_list)
'''
list1=[{"北京":{"面积":"1000平","人口":"200w"},"上海":{"面积":"600平","人口":"150w"}}]
for i in list1:
    for a,b in i.items():
        for c,d in b.items():
            print(a,c,d)
list2=[{"北京":{"面积":"1000平","人口":"200w"},"上海":{"面积":"600平","人口":"150w"},'成都':{'面积':'160平米','人口':'50w'}}]
for i in list2:
    for a,b in i.items():
        for c,d in b.items():
            print(a,c,d)

