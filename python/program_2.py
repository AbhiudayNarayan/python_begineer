while True:
    marks = int(input("Enter your marks: "))

    if marks >= 0 and marks <= 100:
        if marks >= 90:
            print("Your grade is A")
        elif marks >= 80:
            print("Your grade is B")
        elif marks >= 70:
            print("Your grade is C")
        elif marks >= 60:
            print("Your grade is D")
        else:
            print("Your grade is F")
        break  # Exit the loop after valid input
    else:
        print("Invalid marks. Please enter a value between 0 and 100.")

