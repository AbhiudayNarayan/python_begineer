class A :
    VarA="welcome to class A"
class B :
    VarB="welcome to class B"
class C :
    VarC="welcome to class C"
class D(A,B,C):
    VarD="welcome to D"
d1=D()
print(d1.VarA)
print(d1.VarB)
print(d1.VarC)
print(d1.VarD)
