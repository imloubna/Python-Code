
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Square")
    
    
    choice = input("Enter choice (1/2/3/4/5/6): ")

    
    if choice in ['1', '2', '3', '4', '5']:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    
    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")                                                                                                                                                                                                                                                                                   
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        print(f"{num1} / {num2} = {num1 / num2}")
    elif choice == '5':
        print(f"{num1} % {num2} = {num1 % num2}")
    elif choice == '6':
        num = int(input("Enter number to square: "))
        print(f"The square of {num} is {num ** 2}")
    else:
        print("Invalid input")
calculator()

    
