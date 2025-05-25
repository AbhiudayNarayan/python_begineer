lst=[]
a=int(input("Enter a number of the element in the list:"))
for i in range (0,a):
    lst.append(input("Enter a number of the element in the list:"))
b=lst.copy()
b.reverse()
print(lst)
print(b)
count=0
for i in range (0,a):
    if lst[i]==b[i]:
        count=count+1
    else:
        count=count
if (count==a):
    print("its palidrome")
else:
    print("its not palidrome")
