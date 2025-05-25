class Student():
    def __init__(self, name, marks):
        self.name = name
        self.mark = marks

    def get_avg(self):
        sum = 0
        for val in self.mark:
            sum += val
        print("hi",self.name,"your avg mark is",sum/3)

s1=Student("abhiuday",[99,98,97])
s1.get_avg()