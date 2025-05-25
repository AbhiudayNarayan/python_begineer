class Student :
    college = "AbC college" # class attribute

    def __init__(self,name,age):
        self.name = name # object attribute
        self.age = age
        print("adding new student in the data base : ")
s1= Student("John",20)
print(s1.name,s1.age,s1.college)