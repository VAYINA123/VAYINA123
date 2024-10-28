def simple_calculator(num1, num2):
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")



    if choice == "1":
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        print(num1 + num2)

    elif choice == "2":
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        print(num1 - num2)

    elif choice == "3":
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        print(num1 * num2)

    elif choice == "4":
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        print(num1 / num2)

    else:
        print("Invalid Input. Please Enter A Valid Choice (1/2/3/4).")

simple_calculator(1,2)