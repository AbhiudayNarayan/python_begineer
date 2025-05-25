#ABSTRACTION
#hiding the implemnattion setail of a class
# and only showing the essential feature to the user
class Car() :
    def __int__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("starting")
car1=Car()
car1.start()
