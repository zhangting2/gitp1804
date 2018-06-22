class People(object):
    guoji='china'
    @classmethod
    def getguoji(cls):
        return cls.guoji
    @classmethod
    def set_name(cls,guoji):
        cls.guoji=guoji
p=People()
print(p.getguoji())
print(People.getguoji())
p.set_name('灰灰')
print(p.getguoji())
print(People.getguoji())

