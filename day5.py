a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
choice = input("Enter operators (+, -, *, /, %, //, **): ")
if choice == "+":
    print(a + b)
elif choice == "-":
    print(a - b)
elif choice == "*":
    print(a * b)
elif choice == "/":
    if b != 0:
        print(a / b)
    else:
        print("Error : Division by zero is not allowed,")
            
elif choice == "%":
    if b != 0:
        print(a % b)
    else:
        print("Error: Division by zero is not allowed.")
elif choice == "//":
    if b != 0:
        print(a // b)
    else:
        print("Error: Division by zero is not allowed.")
elif choice == "**":
    print(a ** b)
else:
    print("Invalid operator. Please choose from +, -, *, /, %, //, **.")

   