class Employee:
    def __init__(self,role,salary ,department):
        self.role = role
        self.salary = salary
        self.department = department
    def ShowDetails(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)
class Engineer(Employee):
    def __init__(self,name, age):
        self.name = name
        self.age = age
        super().__init__("engineer",80000,"electricL")
eng1 = Engineer("Abhiudady",20)
eng1.ShowDetails()

