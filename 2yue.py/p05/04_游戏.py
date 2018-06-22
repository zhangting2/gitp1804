#-*- coding=utf-8 -*-
import pygame

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
            i.display()
            i.move()

    def fire(self):
        self.bullet_list.append(Bullet('./images/bullet.png',self.screen,self.rect.x,self.rect.y))
class Bullet(object):
    def __init__(self,img_path,screen,x,y):
        self.screen=screen
        self.x=x+40     # 160
        self.y=y-40     # 350
        self.img_path=img_path
        self.bullet=pygame.image.load(self.img_path)
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))
    def move(self):
        self.y-=10
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
    hero.fire()
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
        hero.rect.x += move_step
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        hero.rect.x -= move_step
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        hero.rect.y -= move_step
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        hero.rect.y += move_step
def main():
    #创建游戏窗口
    screen = pygame.display.set_mode((600,700),0,32)
    #把本地文件夹的图片，获取到代码中
    background = pygame.image.load('./images/background.png')
    #初始化飞机
    hero=HeroPlane('./images/hero2.png',screen)
    clock = pygame.time.Clock() #获得游戏时钟控制器
    move_step=20  #移动的步长


    while True:
        #把图片加载到游戏窗口上
        screen.blit(background,(0,0))
        hero.display()
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
