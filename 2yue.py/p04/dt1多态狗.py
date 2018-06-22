class Dog(object):
    def game(self):
        return('狗在玩耍')
class XiaoTianDog(Dog):
    def game(self):
        #super().game()
        return('哮天全在玩')
class Person(object):
    def play_dog(self,dog):
        print('人狗殊途，人和',dog.game())
d=Dog()
xtq=XiaoTianDog()
p=Person()
p.play_dog(xtq)

