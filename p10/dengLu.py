user=123
for i in range(1,5):
    passwd=input('请输入 密码')
    if user==passwd:
        print('登录成功')
        break
    else:
        print('登录失败')

