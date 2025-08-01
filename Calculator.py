def Add(x, y):
    return x + y

def Subtract(x, y):
    return x - y

def Multiply(x, y):
    return x * y

def Division(x, y):
    if y == 0:
        return "Error: Cannot divide by Zero"
    return x / y

def main():
    print("Welcome to the CLI Calculator")
    while True:
        print("\n Choose an Operation")
        print("1. Addition(+)")
        print("2. Subtraction(-)")
        print("3. Multiplication(*)")
        print("4. Division(/)")
        print("5. Exit")

        choice = input("Enter you choice(1-5):")
        if choice == "5":
            print("Exiting the Calculator. GoodBye!")
            break 

        if choice not in ['1', '2', '3', '4']:
            print("Invalid Input. Please try again")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == '1':
            print(f"Result: {Add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {Subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {Multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {Division(num1, num2)}")

if __name__ =="__main__":
    main()