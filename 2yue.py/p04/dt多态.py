class Duck(object):
    def walk(self):
        print('摇摆走')
    def swim(self):
        print('河里游泳')
class People(object):
    def walk(self):
        print('走路四平八稳')
    def swim(self):
        print('花式游泳')
def Quan(obj,o):
    obj.walk()
    obj.swim()
    o.walk()
    o.swim()
p=Duck()
w=People()
Quan(w,p)
#w.walk()
#Quan(w)
