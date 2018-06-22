class Animal:
    def __init__(self):
        self.__leg=4
        self.wei=1
    def __eat(self):
        print('吃')
    def get_eat(self):
        return self.__eat()
    def get_leg(self):
        return self.__leg
    def drink(self):
        print('喝')
class Dog(Animal):
    def jiao(self):
        print('汪汪')
class teadog():
    def xiao(self):
        print('可爱')
#xg=Animal()
xh=Dog()
#print(str(xh.leg))
#xh.jiao()
#xh.eat()
#xh.xiao()
xh.get_eat()
#xh.__leg
a=xh.get_leg()
print(a)
