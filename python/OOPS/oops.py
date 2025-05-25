class Student :
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("adding new student in the data base : ")
s1= Student("John",20)
print(s1.name,s1.age)