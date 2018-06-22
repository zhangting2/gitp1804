class Donkey(object):
    def manzou(seld):
        print('走路满')
    def jiao(self):
        print('驴叫')
class Horse(object):
    def naili(self):
        print('马力足，持久强')
    def jiao(self):
        print('马叫')
class Mule(Donkey,Horse):
    def jiao(self):
        print('骡子唱歌')
xh=Mule()
xh.manzou()
xh.naili()
xh.jiao()
print(Mule.__mro__)
