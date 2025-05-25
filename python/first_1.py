name = input("Enter your name:")
password = input("Enter your password:")
while True:
    if(name == "Abhiuday Narayan") and (password == "123456789"):
        print("Successfully logged in")
        break
    else:
        print("wrong id or password")
        name = input("Enter your name:")
        password = input("Enter your password:")


