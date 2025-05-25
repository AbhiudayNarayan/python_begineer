class student :
    def __init__(self) :
        self.name = input("enter your name")
        self.age = int(input("enter your age"))
        print ("##")

s1= student()
print(s1.name,s1.age)