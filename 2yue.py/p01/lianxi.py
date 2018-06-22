f=open('hao.txt','w')
f.write('哈\n')
f.close()

f=open('hao.txt','a+')
f.write('hehehe\n')
f.close()
t=open('nihao.txt','w+')
t.write('静夜思\n')
t.write('床前明月光\n')
t.write('疑是地上霜\n举头望明月\n低头思故乡\n')
t.close()
t=open('nihao.txt','r+')
n=t.read()
print(n)
t.close()

f=open('hao.txt','a+')
f.write(n)
f.close()





