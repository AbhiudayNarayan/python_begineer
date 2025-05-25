lst=[3 ,7 ,8 , "abhiuday"]
print(lst)
for i in range (0,len(lst)):
    str=lst[i]
    print(str)
    if(len(str)>1):
        print(str.isupper())
