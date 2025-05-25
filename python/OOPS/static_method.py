class Student :
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    @staticmethod
    def hello():
        print("hello")


    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        pirnt ("hi",self.name,"your avg marks is",sum/3)
