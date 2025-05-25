class Person :
    name = "annonymous"
    @classmethod
    def change_name (cls, name):
        cls.name = name
   #second methodd def change_name(self, name):
       # self.name = name # person.name="ABHIUDAY"
        # will give output
        # ABHIUDAY
        # ABHIUDAY


p1=Person()
p1.change_name("Abhiuday")
print(p1.name)
print(Person.name)