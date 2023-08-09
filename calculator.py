forever = True
use = 0
while forever:
    print("A Simple python console calculator ")
    print("")#extra space

    print("OPERATORS") #op
    print("Enter 1 for Addition")
    print("Enter 2 for Subtraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division ")
    print("")

    op = input("Enter your choice: ").lower() #user input
    use += 1
    
    if op == "1": # i use string instead of integer
        print("You choose Addition")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        total = num1 + num2
        print(total)
        again = input("Do you want to use the calculator again? [y/n]: ")
        if again == "n":
            break

    elif op == "2":
        print("You choose Subtraction")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        total = num1 - num2
        print(total)
        again = input("Do you want to use the calculator again? [y/n]: ")
        if again == "n":
            break


    elif op == "3":
        print("You choose Multiplication")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        total = num1 * num2
        print(total)
        again = input("Do you want to use the calculator again? [y/n]: ")
        if again == "n":
            break

    elif op == "4":
        print("You choose Division")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        total = num1 / num2
        print(total)
        again = input("Do you want to use the calculator again? [y/n]: ")
        if again == "n":
            break
print('')#extra space 
print("You use the calculator ", use, " times")            
print("Press enter to enter the program ")
input()
    
