class People:
    def eat(self):
        print('%s正在吃饭。。。'% (self.name))
    def word(self):
        print('%s正在工作'% (self.name))
    def introduce(self):
        print('我的名字是%s,我今年%d岁啦。'% (self.name,self.age))

xiaoming=People()
xiaoming.age =33
xiaoming.name='xiaoming'
xiaoming.eat()
xiaoming.word()
xiaoming.introduce()

xhh=People()
xhh.name='xhh'
xhh.age=19
xhh.eat()
xhh.word()
xhh.introduce()
