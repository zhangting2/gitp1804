class MyError(Exception):
    def __init__(self,str_error):
        self.name=str_error
def get_pwd():
    pwd=input('请输入密码:')
    if len(pwd)<6 or len(pwd)>6:
        raise MyError('密码没有等于6位不符合要求')
try:
    get_pwd()
except Exception as re:
    print('异常为:内容是%s：'% re)
