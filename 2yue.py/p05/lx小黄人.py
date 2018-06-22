import pygame
class XHR(object,lujing,screen):
    self.lujing=lujing
    self.screen=screen
    self.x=60
    self.y=100
    self.w=222
    self.h=250
    self.tupian = pygame.image.load(self.lujing)
    self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
    def display(self):
        self.screen.blit(self.tupian,self.rect)




def main():
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((1480,1852),0,32)
    background = pygame.image.load('./images/background.png')
    screen.blit(background,(0,0))
    a=1
    while a<=4:
        b='./images/xhr%d.jpg'% a
        aa=XHR(b,screen)
        a=a+1
        aa.display()
        clock.tick(1)
        pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('游戏退出')
                pygame.quit()
                exit()
    pygame.display.update()
if __name__=='__main__':
    main()

