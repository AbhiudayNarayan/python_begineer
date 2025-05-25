# this is programm to guess a number
import random
from socket import EAGAIN


def guess_the_number():
    rand_num=random.randint(1,100)
    print(".......... A RANDOM IS generated..........")

    count = 0
    if (count<10):
        checker = True
    else:
        checker = False
    while checker:

        a=int(input("Enter a your guess no.:"))
        if (a==rand_num):
            print("Congratulations!",rand_num,"you guessed the write number")
            print("The original number is ",rand_num)
            print("The Number of guess you took is ",count)
            break
        elif (rand_num<a):
            print(a,"1is greater than the X guess a smaller number")
            count=count+1
            continue
        elif (rand_num>a):
            print(a,"is less number than the X guess a bigger number")
            print ("try again")
            count = count + 1
            continue
print("PRESS ANY NUMBER 0 TO 9 TO CONTINUE",end="\n")

again=int(input(":"))
if again<=9 :
    guess_the_number()
else:
    print("Thank you for playing")
