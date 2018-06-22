class CarStore(object):
    def createCar(self,typeName):
        pass
    def order(self,typeName):
        self.car = self.createCar(typeName)
        self.car.move()
        self.car.stop()
class XiandaiCarStore(CarStore):
    def createCar(self,typeName):
        self.carFactory=CarFactory()
        return self.carFactory.createCar(typeName)
class YilanteCar(object):
    def move(self):
        print('...车在移动.......')
    def stop(self):
        print('..停车...')
class SuonataCar(object):
    def move(self):
        print('......车在移动.......')
    def stop(self):
        print('...停车.....')
class CarFactory(object):
    def createCar(self,typeName):
        self.typeName=typeName
        if self.typeName =='伊兰特':
            self.car=YilanteCar()
        elif self.typeName =='索纳塔':
            self.car= SuonataCar()
        return self.car
suonata=XiandaiCarStore()
suonata.order('索纳塔')
