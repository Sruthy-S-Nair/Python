def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
def calculator():
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            value_01 = float(input("Enter first number: "))
            value_02 = float(input("Enter second number: "))
            if choice == '1':
                print(value_01, "+", value_02, "=", add(value_01, value_02))
            elif choice == '2':
                print(value_01, "-", value_02, "=", subtract(value_01, value_02))
            elif choice == '3':
                print(value_01, "*", value_02, "=", multiply(value_01, value_02))
            elif choice == '4':
                print(value_01, "/", value_02, "=", divide(value_01, value_02))
            break
        else:
            print("Invalid Input")
calculator()