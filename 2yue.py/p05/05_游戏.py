#-*- coding=utf-8 -*-
import pygame
import random
class DiRen(object):
    def __init__(self,img_path,screen):
        self.screen = screen
        self.x=0
        self.y=0
        self.w=10
        self.h=12
        self.img_path = img_path
        self.diji = pygame.image.load(self.img_path)  #飞机图片
        #定义好的位置和尺寸
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        #列表保存发出的子弹
        self.bullet_list=[]
        self.fangxiang='right'
    def display(self):
        self.screen.blit(self.diji,self.rect)  #设置飞机
        self.move()
        num=random.randint(1,60)
        if num == 5 :
            self.fire()
        for i in self.bullet_list:
            if i.panduan():
                self.bullet_list.remove(i)
            i.display()
            i.move()
    def move(self):
        if self.fangxiang=='right':
            self.rect.x+=2
        else:
            self.rect.x-=2
        if self.rect.x>400-self.rect.width:
            self.fangxiang='left'
        elif self.rect.x <= 0:
            self.fangxiang='right'

    def fire(self):
        self.bullet_list.append(DiJiBullet('./images/bullet1.png',self.screen,self.rect.x,self.rect.y))


class HeroPlane(object):
    def __init__(self,img_path,screen):
        self.screen = screen
        self.x=160
        self.y=350
        self.w=100
        self.h=124
        self.img_path = img_path
        self.feiji = pygame.image.load(self.img_path)  #飞机图片
        #定义好的位置和尺寸
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.bullet_list=[]
    def display(self):
        self.screen.blit(self.feiji,self.rect)  #设置飞机
        for i in self.bullet_list:
            if i.panduan():
                self.bullet_list.remove(i)
            i.display()
            i.move()

    def fire(self):
        self.bullet_list.append(Bullet('./images/bullet.png',self.screen,self.rect.x,self.rect.y))

class DiJiBullet(object):
    def __init__(self,img_path,screen,x,y):
        self.screen=screen
        self.x=x+40     # 160
        self.y=y+40     # 350
        self.img_path=img_path
        self.bullet=pygame.image.load(self.img_path)
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))
    def move(self):
        self.y+=10
    def panduan(self):
        ''' 判断子弹是否飞出屏幕外'''
        if self.y > 500:
            return True  #表示子弹飞出啦屏幕
        else:
            return False

class Bullet(object):
    def __init__(self,img_path,screen,x,y):
        self.screen=screen
        self.x=x+40     # 160
        self.y=y+20     # 350
        self.img_path=img_path
        self.bullet=pygame.image.load(self.img_path)
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))
    def move(self):
        self.y-=10
    def panduan(self):
        ''' 判断子弹是否飞出屏幕外'''
        if self.y < 0:
            return True  #表示子弹飞出啦屏幕
        else:
            return False


def key_control(hero,move_step):
     #游戏事件的监听 控制
    for event in pygame.event.get():
        #print('event.type = ',event.type)
        #print('event = ',event)
        if event.type == pygame.QUIT:
            print('游戏退出')
            pygame.quit()
            exit()  #退出程序
        elif event.type==pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE:
                hero.fire()
        elif event.type == pygame.KEYUP:
            pass
    #hero.fire()
        #elif event.type == pygame.KEYDOWN:
         #   if event.key == pygame.K_UP:
          #      rect.y -=move_step
           # elif event.key == pygame.K_DOWN:
            #    rect.y +=move_step
            #elif event.key == pygame.K_LEFT:
             #   rect.x -=move_step
            #elif event.key == pygame.K_RIGHT:
             #   rect.x +=move_step
            #pass
        #elif event.type == pygame.KEYUP:
         #   pass
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        if hero.rect.x < 400-hero.rect.width:
            hero.rect.x += move_step
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        if hero.rect.x > 0:    #400-hero.rect.width:
            hero.rect.x -= move_step
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        if hero.rect.y > 0: # hero.rect.height:
            hero.rect.y -= move_step
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        if hero.rect.y < 500-hero.rect.height:
            hero.rect.y += move_step
def main():
    #创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)
    #把本地文件夹的图片，获取到代码中
    background = pygame.image.load('./images/background.png')
    #初始化飞机
    hero=HeroPlane('./images/hero2.png',screen)
    clock = pygame.time.Clock() #获得游戏时钟控制器
    move_step=15  #移动的步长
    di_ji=DiRen('./images/enemy1.png',screen)

    while True:
        #把图片加载到游戏窗口上
        screen.blit(background,(0,0))
        hero.display()
        di_ji.display()
        key_control(hero,move_step)
        #移动
        #rect.x+=1
        #rect.y+=1
        #if rect.x > 400:
         #   rect.x =1
        #if rect.y > 500:
         #   rect.y =1
        pygame.display.update()
        clock.tick(60)#让游戏时钟，1/60秒运行一次
if __name__=='__main__':
    main()
