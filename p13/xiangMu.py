import XMKuangJia
import naiCha
import time
XMKuangJia.service()

#_____________________________________________________________________________________________

cd_list=[]#定义一个空的列表
#---------------------------------------------------------------------------------------------------
def add_cd():#根据菜单内容 a 设置添加菜系方式
    cai_name=input('请输入菜品名称：')
    cai_price=input('请输入价格：')
    cai_class=input('请输入菜品类型：')
    cai_taste=input('请输入菜品味道：')
    cd_dic={}#把输入的内容保存到字典里，一次仅一个菜
    cd_dic['cai_name']=cai_name
    cd_dic['cai_price']=cai_price
    cd_dic['cai_class']=cai_class
    cd_dic['cai_taste']=cai_taste
    cd_list.append(cd_dic)#把菜单字典追加到设置的空列表中
#___________________________________________________________________________________________________

def find_all():#根据菜单内容 b 查找全部已添加菜的菜单
    if len(cd_list)>0:
        s=1
        for i in cd_list:
            print('%d.菜单 菜的菜名是：%s,价格是：%s,类型是：%s,口味是：%s'% (s,i['cai_name'],i['cai_price'],i['cai_class'],i['cai_taste']))
            s +=1
    else:
        print('没有菜单，请输入a ,添加菜单')
#___________________________________________________________________________________________________

js_list=[]#设置个空列表
def diancan(n):#定义点餐
    dic=cd_list[n-1]
    js_list.append(dic)
    return dic
#------------------------------------------------------
def bill():#定义结帐
    s=0
    if len(js_list)>0:
        for i in js_list:
            s +=int(i['cai_price'])
    return s
    print(s)
#----------------------------------------------------------------------------------------------------
def menu():#定义第二类，智能点餐菜单
    print('')
    print('主食：p1 面食，米饭')
    print('')
    print('厨师推荐———>p2 桑拿鱼头：￥68')
    print('')
    print('招牌特色菜\n\np3 一锅鲜：￥55\np4 口味鱼：￥48\np5 香辣虾：￥58\np6 水煮牛肉：￥58')
    print('')
    print('精美特色\n\np7 红烧肉：￥38\np8 爆炒田鸡：￥42\np9 爆炒腊肉：￥42\np0 霸王别姬：￥66')
    print('')
def artificial():#定义人数和点餐并支付
    print('*'*30)
    print('欢迎大家来我们客满堂餐厅用餐')
    r=int(input('请问几位：'))
    if r==1:
        print('这边请,请坐单人桌')
    elif r==2:
        print('这边请，双人桌')
    elif r>=3 and r<=6:
        print('这边请')
    elif r>6:
        print('各位请上二楼包厢，这边请')
    print('')
    print('这是我们这里的菜单，看看吃什么')
    #print('%s \n'% menu())
    menu()
    chi=input('请问吃点什么：')
    price=int(input('所选菜系单价：'))
    q=int(input('请问要几份：'))
    yuan_sum=price*q
    print(yuan_sum)
    f=int(input('支付钱数：'))
    y=f-yuan_sum
    if y>0:
        print('找零'+str(y))
        print('支付成功，请愉快用餐')
    else:
        print('欢迎下次光临')
    print('欢迎下次光临')
#________________________________________________________________________________________
def takeaway():
    menu()
    g=input('您好，这里是客满堂餐厅，请问要点什么')
    p=input('好的，请问送到哪里')
    print('我们会在三十分钟内准时送达，到后会给您信息，请注意查收')

#____________________________________________________________
def ziZhu():
    print('自助餐，每位60元，不限时间，尽情享用，只要你能吃，我们供你吃\n注意：吃撑概不负责')
    p=int(input('请问有几位？'))
    u=60
    h=p*u
    print('您花费总金额为：%s元'% h)
    t=int(input('请输入支付金额：'))
    while t < h:
        print('小本生意，请多照顾')
        t=int(input('请再次支付：'))
    y=t-h
    if y>0:
        print('找零 %d元，您请进，祝您用餐愉快'% y)
        time.sleep(2)
    elif y==0:
        print('支付成功，请进，祝您用餐愉快')
        time.sleep(2)
#_____________________________________________________________________
def BBQ():
    print('欢迎来到客满堂餐厅')
    print('自助烧烤，各种材料已准备好，万事具备，只差您来')
    print('出租烧烤架 120元  ')
    print('优质炭     100元  ')
    print('烤翅       60元  ')
    print('羊肉串     60元  ')
    print('鱿鱼       60元  ')
    print('土豆、青菜、豆皮、香菇、玉米、蜂蜜、烤酱、各种必备调料 100元  ')
    s=500
    print('您花费总金额为：%s元'% s)
    t=int(input('请输入支付金额：'))
    while t < s:
        print('小本生意，请多照顾')
        t=int(input('请再次支付：'))
    y=t-s
    if y>0:
        print('找零 %d元，请让我们专人带您们去烧烤地点，也可自选地点，祝您这一天玩的开心^-^'% y)
        time.sleep(2)
    elif y==0:
        print('支付成功，请让我们专人带您们去烧烤地点，也可自选地点，祝您这一天玩的开心^-^')
        time.sleep(2)
#______________________________________________________________________________________________________

a=int(input('请选择您要的操作：'))#输入您要的操作
if a==1:#判断输入操作应对应的选项
    while True:#循环输入1 的选项的操作内容
        #c_menu()#调用输入的菜单
        XMKuangJia.c_menu()
        n=input('请输入您要的操作：')#输入对应操作
        if n=='a':
            add_cd()#调用菜单栏，自己输入菜
        elif n=='b':
            find_all()#调用查找全部菜单
        elif n=='c':
            x=int(input('请输入你要点餐的编号：'))
            f=diancan(x)#调用点餐函数
            print('您选择的菜名是：%s,价格是：%s'%(f['cai_name'],f['cai_price']))
        elif n=='d':
            s=bill()#调用结帐函数
            print('您本次消费的金额是：%s ' % s)
            if s > 100 :#判断消费满100抽一次奖，不满没奖
                print('恭喜您，消费满100,有次抽奖的机会')
                import random
                u=random.randint(1,10)
                if u==1:
                    print('恭喜，抽中一等奖，运气太好了，这餐免单')
                    time.sleep(2)
                    break
                elif u==2:
                    print('恭喜，抽中二等奖，80元优惠券,请下次用餐时使用')
                    #s=s-80
                #return s
                elif u==3:
                    print('恭喜，抽中三等奖，奖品一个收纳箱')
                else:
                    print('恭喜，特等奖，茶杯一个')
                    t=int(input('请输入支付金额'))
                    if t==000:
                        naiCha.fuo()
                        print('开个玩笑')
                    else:
                        print('')
                while t<s:
                    print('小本生意，请多照顾')
                    t=int(input('请再次支付：'))
                y=t-s#算余额
                if y>0:#判断支付钱数是否足够，进行计算
                    print('找零 %d元，您慢走，欢迎下次再来'% y)
                    break
                elif y==0:
                    print('支付成功，欢迎下次光临')
                    break
                #return y
        elif n=='e':
            break
elif a==2:
    artificial()
elif a==3:
    takeaway()
elif a==4:
    ziZhu()
elif a==5:
    BBQ()
elif a==6:
    print('很遗憾，感谢您进入我们餐厅,再见^-^')
    time.sleep(2)
