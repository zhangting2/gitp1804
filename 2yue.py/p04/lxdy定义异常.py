zhanghu='zz'
pwd='666666'

class HuError(Exception):
    def __init__(self,hu_error):
        self.name=hu_error
class MiMaError(Exception):
    def __init__(self,Mi_error):
        self.mi=Mi_error
def get_hu():
    while True:
        hu=input('请输入用户名：')
        if hu==zhanghu:
            print('用户名正确')
            break
        else:
            raise HuError('用户名错误，请重新输入')
def get_pwd():
    a=0
    while a<3:
        pwdd=input('请输入密码：')
        if pwdd==pwd:
            print('密码正确')
            break
        else:
            raise MiMaError('密码错误，请重新输入')
        a+=1
try:
    get_hu()
    get_pwd()
except Exception as re:
    print('异常为:%s'% re)
