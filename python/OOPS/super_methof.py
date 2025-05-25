class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Starting")
    @staticmethod
    def stop():
        print("Stopping")
class ToyotaCar(Car):
    def __init__(self,name, type):
        self.name = name
        super().__init__(type)
        super().start()
car1=ToyotaCar("Toyota","electric")
print(car1.type)
print(car1.name)