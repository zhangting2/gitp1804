def copy_1(file_name):  #定义一个备份文件
#file_name=input('请输入要复制的文件名：')
    f = open(file_name,'r')   #打开要复制的文件，并选读取

    position=file_name.rfind('.')  #找到点的位置 从后找
    copy_1=file_name[:position]+'[复件]'+file_name[position:]   #新文件名
    f1=open(copy_1,'w')  #打开一个新文件，并选写入
    while True:
        content=f.read(1024)    #读取全部文件赋值一个变量
        if len(content)==0:
            break
        f1.write(content)    #把原文件内容写到新文件里
    f.close()     #关闭源文件
    f1.close()       #关闭新文件
n=input('请输入要复制的文件名：')
copy_1(n)
