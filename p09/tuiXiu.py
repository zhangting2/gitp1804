sex=input('请输入性别：')
age=int(input('请输入年龄：'))
fraction=float(input('请输入分数'))
if sex == '男':
    if age >= 60:
        print('该会家养老啦')
    else:
        print('继续奋斗，你还年轻')
        if fraction>=80:
            print('及格')
        else:
            print('不及格')
else:
    if age >= 55:
        print('回家跳广场无')
    else:
        print('继续工作')
        if fraction >= 80:
            print('你成绩好')
        else:
            print('你输了')


