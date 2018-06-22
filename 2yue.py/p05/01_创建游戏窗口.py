#-*- coding=utf-8 -*-
import pygame
def main():
    #创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)
    #把本地文件夹的图片，获取到代码中
    background = pygame.image.load('./images/background.png')
    feiji = pygame.image.load('./images/hero2.png')
    #定义好的位置和尺寸
    rect = pygame.Rect(160,350,100,124)
    clock = pygame.time.Clock()#获得游戏时钟控制器


    while True:
        #把图片加载到游戏窗口上
        screen.blit(background,(0,0))
        screen.blit(feiji,rect)
        #移动
        rect.x+=1
        rect.y+=1
        if rect.x > 400:
            rect.x =1
        if rect.y > 500:
            rect.y =1
        #刷新显示
        pygame.display.update()
        clock.tick(60)#让游戏时钟，1/60秒运行一次
if __name__=='__main__':
    main()
