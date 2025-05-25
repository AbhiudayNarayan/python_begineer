#inheritance one class
# (child derived) dervives the
# properties & methods of anothe class (parent ?base)
class Car:
    color = "red"
    @staticmethod
    def start():
        print("start")
    @staticmethod
    def stop():
        print("stop")
class Toyota_car(Car):
    def __init__(self, brand):
        self.brand1 = brand
class FordCar(Toyota_car):
    def __init__(self, type):
        self.type = type
car1 = FordCar("Ford")
car1.start()
print(car1.type)