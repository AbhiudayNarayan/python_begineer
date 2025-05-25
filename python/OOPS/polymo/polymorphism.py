class complex :
    def __init__(self , real , imag):
        self.real = real
        self.imag = imag
    def show(self):
        print(self.real,"i +",self.imag,"j")
    def add(self,num2):
        newREAL = self.real + num2.real
        newIMAG = self.imag + num2.imag
        return complex(newREAL,newIMAG)


num1 = complex(1,2)
num1.show()
num2 = complex(3,4)
num2.show()
num3 = num1.add(num2)
num3.show()
