f=open('1.txt','w')
f.write('加油\n')
f.close()

f=open('1.txt','r')
content=f.read()
print(content)
f.close()

f=open('1.txt','a')
f.write('再见\n')
f.close()

