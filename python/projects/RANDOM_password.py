import random
import string


pass_len = int(input("Enter password length: "))
char_values = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(char_values, pass_len))
print(password)


